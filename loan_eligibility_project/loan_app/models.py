from django.db import models

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

MARRIED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

GRADUATE_CHOICES = (
    ('Graduate', 'Graduate'),
    ('NonGraduate', 'NonGraduate')
)

SELF_EMPLOYED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

PROPERTY_CHOICES = (
    ('Rural', 'Rural'),
    ('Semiurban', 'Semiurban'),
    ('Urban', 'Urban')
)

class approvals(models.Model):
    First_name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=15)
    Dependents = models.IntegerField(default=0)
    ApplicantIncome = models.IntegerField(default=0)
    CoapplicantIncome = models.IntegerField(default=0)
    LoanAmount = models.IntegerField(default=0)
    Credit_History = models.IntegerField(default=0)
    Gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    Married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    Education = models.CharField(max_length=15, choices=GRADUATE_CHOICES)
    Self_Employed = models.CharField(max_length=15, choices=SELF_EMPLOYED_CHOICES)
    Property_Area = models.CharField(max_length=15, choices=PROPERTY_CHOICES)

def __str__(self):
    return self.First_name, self.Last_name