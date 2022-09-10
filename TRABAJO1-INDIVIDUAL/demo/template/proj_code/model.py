"""
    model.py: modulo donde se especifica el modelo
"""
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor


def reg_lineal(X, y):
    """Documentación de este modelo: """
    lr_multiple = linear_model.LinearRegression()
    return lr_multiple.fit(X, y)


def reg_KNN(X, y, num_vecinos=5):
    """Documentación de este modelo: """
    reg = KNeighborsRegressor(n_neighbors=num_vecinos)
    return reg.fit(X, y)



def reg_Forest(X, y):
    """Documentación de este modelo: """
    reg = RandomForestRegressor(n_estimators=20, random_state=0)
    return reg.fit(X, y)



