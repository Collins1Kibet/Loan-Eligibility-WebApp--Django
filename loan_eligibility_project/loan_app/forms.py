from django.forms import ModelForm
from . models import approvals
from django import forms

class ApprovalForm(forms.Form):
        First_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
        Last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placehoder': 'Enter Last Name'}))
        Dependents = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of Dependents'}))
        ApplicantIncome = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Monthly Gross Income'}))
        CoapplicantIncome = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Co-applicant Monthly Gross Income'}))
        LoanAmount = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Requested Loan Amount'}))
        Credit_History = forms.ChoiceField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8)])
        Gender = forms.ChoiceField(choices= [('Male', 'Male'), ('Female', 'Female')])
        Married = forms.ChoiceField(choices= [('Yes', 'Yes'), ('No', 'No')])
        Education = forms.ChoiceField(choices= [('Graduate', 'Graduate'), ('NonGraduate', 'NonGraduate')])
        Self_Employed = forms.ChoiceField(choices= [('Yes', 'Yes'), ('No', 'No')])
        Property_Area = forms.ChoiceField(choices= [('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])

class MyForm(ModelForm):
    class Meta:
        model = approvals
        fields = '__all__'