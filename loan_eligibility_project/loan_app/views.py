from django.shortcuts import render
from django.contrib import messages
from .forms import MyForm
from rest_framework import viewsets
from rest_framework.response import Response
from .models import approvals
from .serializers import approvalsSerializers
from tensorflow.keras.models import load_model
from keras import backend as B
import numpy as np
import pandas as pd
import pickle

from .forms import ApprovalForm

class ApprovalsViews(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers

def myform(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
        else:
            form = MyForm()


def ohevalue(dataframe):
    ohe_columns_path = 'One_Hot_Encoded_Columns.pkl'
    ohe_columns = pickle.load(open(ohe_columns_path, 'rb'))
    missing_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    dataframe_processed = pd.get_dummies(dataframe, columns=missing_columns)

    new_dictionary = {}
    for c in ohe_columns:
        if c in dataframe_processed.columns:
            new_dictionary[c] = dataframe_processed[c].values
        else:
            new_dictionary[c] = 0
    new_dataframe = pd.DataFrame(new_dictionary)
    return new_dataframe


def approvereject(unitX):
    try:
        model_path = 'Loan_Model.keras'
        scaler_path = 'scaler.pkl'
        mdl = load_model(model_path)
        scaler = pickle.load(open(scaler_path, 'rb'))

        X = scaler.transform(unitX)
        y_predict = mdl.predict(X)
        y_predict = (y_predict > 0.5).astype(int)

        result_df = pd.DataFrame(y_predict, columns=['Status'])
        result_df = result_df.replace({0: 'Approved', 1: 'Rejected'})
        B.clear_session()
        return result_df.values[0][0], X[0]
    except ValueError as e:
        return e.args[0], None
    

def usercontact(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            First_name = form.cleaned_data['First_name']
            Last_name = form.cleaned_data['Last_name']
            Dependents = form.cleaned_data['Dependents']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            LoanAmount = form.cleaned_data['LoanAmount']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']

            myDict = (request.POST).dict()
            dataframe = pd.DataFrame(myDict, index=[0])

            answer = approvereject(ohevalue(dataframe))[0]
            Xscaler = approvereject(ohevalue(dataframe))[1]

            if int(dataframe['LoanAmount']) < 100000:
                messages.success(request, f'Apllication Status: {answer}')
            else:
                messages.success(request, 'Invalid. Your Loan Exceeds the $100,000 Limit')

            

    form = ApprovalForm()

    return render(request, 'myform/userform.html', {'form': form})