
import pandas as pd

def doc():
    #Leemos el archivo y lo cargamos como un dataset de pandas
    df = pd.read_csv('data/turismo2.csv')
    #Renombraremos las columnas para evitar errores debido a espacios en blanco o nombres extensos
    df.rename(columns = {'Días funcionamiento': 'Dias_func', 'Destino Turístico': 'Dest_turistico', ' Total de Llegadas Chilenos': 'Total_lleg_chilenos',' Total de Pernoctaciones  Chilenos': ' Total_perc_chilenos', ' Total Llegadas Extranjeros': 'Total_lleg_ext', ' Total Pernoctaciones Extranjeros': 'Total_perc_ext', 'Total Llegadas': 'Total_lleg', 'Total Pernoctación': 'Total_perc', 'Factor de Expansión': 'Factor_exp'}, inplace = True )
    return (df)