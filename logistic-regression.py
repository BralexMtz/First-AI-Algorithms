import numpy as np
from sklearn.linear_model import LogisticRegression

def regresion():
    """
      Pretende separar los datos entre aquellos que tienen probabilidad de aprobar y 
      aquellos que no, dependiendo del número de horas que han gastado.
    """
    #Datos a utilizar
    xlist = [i*0.25 for i in range(2,22)]
    horas = np.array(xlist).reshape(-1,1) 
    # 1 si aprobo, o 0 si reprobo
    aprobado = np.array([0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1]) 

    #Creamos la instancia de la regresion y le damos los datos
    regresion_logistica = LogisticRegression()
    # se entrena la regresion logistica
    regresion_logistica.fit(horas,aprobado)

    #Generamos una nueva lista de horas para hacer una prediccion y se ejecuta
    horas_prediccion = np.array([i for i in range(1,7)]).reshape(-1,1)
    # predict() realiza la predicción sobre los elementos de horas_prediccion para 
    # definir si aprueban o no el curso de acuerdo a las horas de dedicación.
    prediccion = regresion_logistica.predict(horas_prediccion)
    # predict_proba() entrega exactamente cuál es la probabilidad de que alguien no 
    # apruebe o apruebe el curso.
    probabilidad = regresion_logistica.predict_proba(horas_prediccion)

    #Se muestran los resultados
    np.set_printoptions(3)  #Ajustamos la visualizacion
    print('Datos de la prediccion realizada:')
    print('Horas:        {}'.format(horas_prediccion.reshape(1,-1)))
    print('Aprobado:     {}'.format(prediccion))
    print('Probabilidad: {}'.format(probabilidad[:,1]))

if __name__ == '__main__':
    regresion()