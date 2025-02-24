import numpy as np

def calMAE(valores_reales,valores_estimados):
    #mide el error medio en los valores unidades de los datos reales
    MAE = np.mean(np.abs(valores_reales-valores_estimados))
    return MAE

def calcMSE(valores_reales,valores_estimados):
    #error cuadratico medio
    MSE =np.mean((valores_reales - valores_estimados)**2)
    return MSE

def calcRSME(valores_reales,valores_estimados): #RAIZ DEL ERROR CUADRATICA MEDIO
    #PENALIZA MAS A LOS ERRORES GRANDES, PONE EL ERROR EN LAS MISMAS UNIDADES QUE LOS DATOS REALES #ES EL MAS USADO
    MSE = calcMSE(valores_reales,valores_estimados)
    RMSE =np.sqrt(MSE)
    return RMSE

def calcMAPE(valores_reales,valores_estimados):#error porcentual
    MAPE = np.mean(np.abs((valores_reales-valores_estimados)/valores_reales))*100
    return MAPE
