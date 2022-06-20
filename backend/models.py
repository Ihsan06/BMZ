from django.contrib.auth.models import AbstractUser
# from django.shortcuts import render
from django.forms import ModelChoiceField

from django.utils import timezone
from django.db import models

# from django.db.models import Max
from django import forms


# Create your models here.


class User(AbstractUser):
    pass


class Country(models.Model):
    country_name = models.CharField(max_length=64, null=False)  # Pflichtfeld
    iso_code = models.IntegerField()

    def __str__(self):
        return f"{self.country_name}"

    class Meta:
        ordering = ['country_name']


class Country_New(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_name', 'iso_code']
        widgets = {
            'country_name': forms.TextInput(attrs={'class': 'form-control'}),
            'iso_code': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class Country_Change(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_name', 'iso_code']
        widgets = {
            'country_name': forms.TextInput(attrs={'class': 'form-control'}),
            'iso_code': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class Project(models.Model):
    name_project = models.CharField(max_length=64, null=False)  # Pflichtfeld
    description = models.CharField(max_length=500, )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    start_project = models.DateField()
    end_project = models.DateField()
    budget_project = models.FloatField()
    spend_budget_project = models.FloatField()

    def __str__(self):
        return f"{self.name_project}"

    class Meta:
        ordering = ['-budget_project']


class Project_New(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_project', 'description', 'country', 'start_project', 'end_project',
                  'budget_project', 'spend_budget_project']

        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'start_project': forms.DateInput(attrs={'class': 'form-control'}),
            'end_project': forms.DateInput(attrs={'class': 'form-control'}),
            'budget_project': forms.NumberInput(attrs={'class': 'form-control'}),
            'spend_budget_project': forms.NumberInput(attrs={'class': 'form-control'})
        }


class Project_Change(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name_project', 'description', 'country', 'start_project', 'end_project',
                  'budget_project', 'spend_budget_project']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'start_project': forms.DateInput(attrs={'class': 'form-control'}),
            'end_project': forms.DateInput(attrs={'class': 'form-control'}),
            'budget_project': forms.NumberInput(attrs={'class': 'form-control'}),
            'spend_budget_project': forms.NumberInput(attrs={'class': 'form-control'})
        }


