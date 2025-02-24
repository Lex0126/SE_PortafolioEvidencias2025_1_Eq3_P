import numpy as np
#valores reales los que quiere el usuario y los estimados son los leidos por el sensor
def calcMAE(valores_reales,valores_estimados): #Medium absolut error (MAE)
    MAE = np.mean(np.abs(valores_reales-valores_estimados))
    return MAE

def calcMSE(valores_reales,valores_estimados): #Medium Squ Error(MSE)
    #Penaliza los errores grandes
    MSE = np.mean((valores_reales-valores_estimados)**2)
    return MSE

def calcRMSE(valores_reales,valores_estimados): #Raiz del error cuadratico medio (RMSE)
    #Personaliza mas a los errores grandes, Pone al error en las mismas unidades que los datos reales
    MSE = calcMSE(valores_reales,valores_estimados)
    RMSE = np.sqrt(MSE)
    return RMSE
def calcMAPE(valores_reales,valores_estimados):
 #Mide el error en porcentaje, facilita la interpretacion en terminos relativos
    MAPE = np.mean(np.abs(valores_reales-valores_estimados)/valores_reales) * 100
    return MAPE


