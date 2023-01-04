# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 03:20:18 2022

@author: Usuario
"""
import pandas as pd
import numpy as np

#estadistica
import scipy.stats as stats
import statsmodels.formula.api as smf

#modelos ml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#metricas ml
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score


def saturated_model(df, dependent, estimation = smf.ols, fit_model=True):
    
    tmp_vars = "+".join(df.columns.drop(dependent))
    tmp_model = estimation(dependent+ '~ '+ tmp_vars, df)
    
    if fit_model is True:
        tmp_model = tmp_model.fit()
    return tmp_model

def concise_summary(mod, estimation='ols', print_fit=True):
    fit=pd.DataFrame({'Statistics':mod.summary2().tables[0][2][2:],
                      'Value':mod.summary2().tables[0][3][2:]})
    #guardamos los parametros estimados por cada regresor
    if estimation is 'ols':
        estimates =pd.DataFrame(mod.summary2().tables[1].loc[:,['Coef','Std.Err.','t']])
    elif estimation is 'logit':
        estimates=pd.DataFrame(mod.summary2().tables[1].loc[:,['Coef','Std.Err.','z']])
        
    #imprimir fit es opcional
    if print_fit is True:
        print("\nGoodness of Fit Statistics\n", fit)
    print("\nPoint Estimates\n\n", estimates)
    