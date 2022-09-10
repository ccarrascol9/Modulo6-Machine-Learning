"""
    metric.py: Implementar las funciones de métrica y evaluación
"""

from sklearn.metrics import mean_squared_error
from sklearn import metrics
import numpy as np
from sklearn import linear_model

def metrica_mean(y_verdad, y_preds):
    
    return metrics.mean_absolute_error(y_verdad, y_preds)

def metrica_mean_squared_error(y_verdad, y_preds):
    
    return metrics.mean_squared_error(y_verdad, y_preds)

def metrica_sqrt(y_verdad, y_preds):
    
    return np.sqrt(metrics.mean_squared_error(y_verdad, y_preds))

from sklearn.linear_model import LinearRegression

def metrica_r2(y_verdad, y_preds):
    
    return metrics.r2_score(y_verdad, y_preds)

from sklearn.linear_model import LinearRegression


def metrica_d2(y_verdad, y_preds):
    
    return metrics.d2_tweedie_score(y_verdad, y_preds)


def metrica_error_mediano(y_verdad, y_preds):
    
    return metrics.median_absolute_error(y_verdad, y_preds)

def metrica_cuartiles(y_verdad, y_preds):
    
    return metrics.mean_pinball_loss(y_verdad, y_preds)






