# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:15:48 2022

@author: Usuario
"""
import numpy as np

def conditions_occupation(s):
    if ((s['occupation'] == 'Prof-specialty') or (s['occupation'] == 'Exec-managerial') or (s['occupation'] == 'Adm-clerical') or (s['occupation'] == 'Sales') or (s['occupation'] == 'Tech-support')):
        return 'white-collar'
    elif ((s['occupation'] == 'Craft-repair') or (s['occupation'] == 'Machine-op-inspct') or (s['occupation'] == 'Transport-moving') or (s['occupation'] == 'Handlers-cleaners') or (s['occupation'] == 'Farming-fishing') or (s['occupation'] == 'Protective-serv') or (s['occupation'] == 'Priv-house-serv')):
        return 'blue-collar'
    elif ((s['occupation'] == 'Other-service') or (s['occupation'] == 'Armed-Forces')):
        return 'others'
    else:
        return np.nan
    
def conditions_workclass(s):
    if ((s['workclass'] == 'Federal-gov')):
        return 'federal-gov'
    elif ((s['workclass'] == 'State-gov') or (s['workclass'] == 'Local-gov')):
        return 'state-level-gov'
    elif ((s['workclass'] == 'Self-emp-inc') or (s['workclass'] == 'Self-emp-not-inc')):
        return 'self-employed'
    elif ((s['workclass'] == 'Private')):
        return 'privated'
    elif ((s['workclass'] == 'Never-worked') or (s['workclass'] == 'Without-pay')):
        return 'unemployed'
    else:
        return np.nan     

def conditions_education(s):
    if ((s['education'] == 'Preschool')):
        return 'preschool'
    elif ((s['education'] == '1st-4th') or (s['education'] == '5th-6th')):
        return 'elementary-school'
    elif ((s['education'] == '7th-8th') or (s['education'] == '9th') or (s['education'] == '10th') or (s['education'] == '11th') or (s['education'] == '12th') or (s['education'] == 'HS-grad')):
        return 'high-school'
    elif ((s['education'] == 'Assoc-voc') or (s['education'] == 'Assoc-acdm') or (s['education'] == 'Some-college')):
        return 'college'
    else:
        return 'university'
    

def conditions_ms(s):
    if ((s['marital-status'] == 'Married-civ-spouse') or (s['marital-status'] == 'Married-spouse-absent') or (s['marital-status'] == 'Married-AF-spouse')):
        return 'married'
    elif ((s['marital-status'] == 'Divorced')):
        return 'divorced'
    elif ((s['marital-status'] == 'Separated')):
        return 'separated'
    else:
        return 'widowed'

def conditions_continents(s):
    if ((s['native-country'] == 'Germany') or (s['native-country'] == 'England') or (s['native-country'] == 'Italy') or (s['native-country'] == 'Poland') or (s['native-country'] == 'Portugal') or (s['native-country'] == 'Greece') or (s['native-country'] == 'France') or (s['native-country'] == 'Ireland') or (s['native-country'] == 'Hungary') or (s['native-country'] == 'Holand-Netherlands') or (s['native-country'] == 'Yugoslavia') or (s['native-country'] == 'Ireland')):
        return 'europa'
    elif ((s['native-country'] == 'Columbia') or (s['native-country'] == 'United-States') or (s['native-country'] == 'Haiti') or (s['native-country'] == 'Trinadad&Tobago') or (s['native-country'] == 'Mexico') or (s['native-country'] == 'Puerto-Rico') or (s['native-country'] == 'Canada') or (s['native-country'] == 'El-Salvador') or (s['native-country'] == 'Cuba') or (s['native-country'] == 'Jamaica') or (s['native-country'] == 'Dominican-Republic') or (s['native-country'] == 'Guatemala') or (s['native-country'] == 'Nicaragua') or (s['native-country'] == 'Peru') or (s['native-country'] == 'Ecuador') or (s['native-country'] == 'Honduras')):
        return 'america'
    elif ((s['native-country'] == 'Philippines') or (s['native-country'] == 'India') or (s['native-country'] == 'China') or (s['native-country'] == 'Japan') or (s['native-country'] == 'Vietnam') or (s['native-country'] == 'Taiwan') or (s['native-country'] == 'Iran') or (s['native-country'] == 'Thailand') or (s['native-country'] == 'Hong') or (s['native-country'] == 'Cambodia') or (s['native-country'] == 'Laos')):
        return 'asia'
    else:
        return np.nan

def conditions_gender(s):
    if ((s['gender'] == 'Male')):
        return 1
    else:
        return 0

 
def conditions_income(s):
    if ((s['income'] == '>50K')):
        return 1
    else:
        return 0




