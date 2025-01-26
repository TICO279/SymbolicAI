import time
import random
import numpy as np
import math
import csv
import os



##########################################################################################
##########################################################################################
##########################################################################################
#                                  ALGORITMO EVOLUTIVO
##########################################################################################
##########################################################################################
##########################################################################################




##########################################################################################
#                                  CLASES
##########################################################################################

"""
En esta parte se definen las clases que se van a utilizar para el proyecto. Aunque se podría hacer sin usar clases como estas, simplifica mucho el proceso ya que hay muchos índices.

"""


"""
La clase Examen es la que se va a utilizar para representar los examenes que se van a realizar. Esta clase representa los elementos de cada INDIVIDUO o SOLUCIÓN.

"""

class Examen:

  def __init__(self, salon, materia, horario):
    self.materia = materia  #En la materia tiene el número de inscritos
    self.salon = salon
    self.horario = horario

  def __str__(self) -> str:
    return str(self.materia) + "  " + str(self.salon) + "  " + str(
        self.horario)


"""
Las siguientes clases son nuestros datos estáticos que se van a utilizar para el proyecto. Estos nos sirven para compara diversos aspectos en nuestra función evlauladora como alumnos que tengan examenes sobrepuestos o incluso salones que no tengan suficiente espacio para alguna materia

"""

class Salon:

  def __init__(self, salon_id, capacidad):
    self.salon_id = salon_id
    self.capacidad = capacidad

  def __str__(self) -> str:
    return (str(self.salon_id))


class Materia:

  def __init__(self, materia_id, inscritos):
    self.materia_id = materia_id
    # self.salon_id = salon_id
    # self.horario_id = horario_id
    self.inscritos = inscritos

  def __str__(self) -> str:
    return (str(Nombresmaterias[self.materia_id][0]))


class Alumno:

  def __init__(self, alumno_id, materias_ids):
    self.alumno_id = alumno_id
    self.materias_ids = materias_ids

  def __str__(self) -> str:
    s = "" + str(self.alumno_id) + ": "
    for x in self.materias_ids:
      s += str(Nombresmaterias[x][0]) + ", "
    return s

"""
Todas las clase cuentan con la implementación de la función __str__ por lo que se les puede imprimir sin problemas.
"""
##########################################################################################

##########################################################################################
#                           LECTURA DE VALORES
##########################################################################################

"En esta sección abrimos el material de datos que proviene de archivos .csv"

Nombresmaterias=[]
carpeta_actual = os.path.abspath(os.path.dirname(__file__))
nombre_archivo = os.path.join(carpeta_actual, 'MateriasItam.csv')
with open(nombre_archivo, 'r', newline='') as archivo_csv:
  reader = csv.DictReader(archivo_csv)
  for row in reader:
    Nombresmaterias.append((row['Clave'],row['Nombre']))

# -------------------------------------------------------------------------------------------------------------
# LECTOR DE ARCHIVOS CSV GUARDADOS QUEDA TODO EN LISTA_ALUMNOS, LISTA_MATERIAS, LISTA_SALONES, LISTA_EXAMENES    
# Llena el arreglo de todos los Salones
def leer_salones_desde_csv(Salones):
    salones = []
    with open(Salones, 'r', newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for row in reader:
            salon_id = int(row['Salon ID'])
            capacidad = int(row['Capacidad'])
            salones.append(Salon(salon_id, capacidad))
    return salones

nombre_archivo = os.path.join(carpeta_actual, 'salones.csv')
lista_salones = leer_salones_desde_csv(nombre_archivo)

# Llena el arreglo de todas las materias
def leer_materias_desde_csv(Materias):
    materias = []
    with open(Materias, 'r', newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for row in reader:
            materia_id = int(row['Materia ID'])
            inscritos = int(row['Inscritos'])
            materias.append(Materia(materia_id, inscritos))
    return materias


nombre_archivo = os.path.join(carpeta_actual, 'materias.csv')
lista_materias = leer_materias_desde_csv(nombre_archivo)

# Llena el arreglo de todos los Alumnos
def leer_alumnos_desde_csv(Alumnos):
    alumnos = []
    with open(Alumnos, 'r', newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for row in reader:
            tira_materias = []
            alumno_id = int(row['Alumno ID'])
            cadena_indices = row['Examenes IDs']  # Cadena de índices
            indices = [int(index.strip()) for index in cadena_indices[1:-1].split(',')]  # Convertir la cadena de índices en una lista de enteros
            for indice in indices:
                tira_materias.append(indice)  # Obtener el examen correspondiente al índice del arreglo de exámenes
            alumnos.append(Alumno(alumno_id, tira_materias))
    return alumnos

nombre_archivo = os.path.join(carpeta_actual, 'alumnos.csv')
lista_alumnos = leer_alumnos_desde_csv(nombre_archivo)

##########################################################################################
#                                  INFORMACIÓN DE LA "UNIVERSIDAD"
##########################################################################################


"""
En esta sección se definen los números de salones, materias, alumnos y examenes que se van a utilizar para el proyecto, esto con base en la información de la universidad

"""

numerodealumnos=100
numMaterias=431
numerodesalones = 100
horasTotalesExamenes=120
horas_indeseadas = [1,8,9,13,14,21,22,26,27,34,35,39,40,47,48,53,60,61,65,66,73,74,78,79,86,87,91,92,99,100,104,105,112,113,117,118,125,126,130]

nombre_archivo = os.path.join(carpeta_actual, 'alumnos.csv')
alumnos=leer_alumnos_desde_csv(nombre_archivo)

nombre_archivo = os.path.join(carpeta_actual, 'materias.csv')
materias=leer_materias_desde_csv(nombre_archivo)

nombre_archivo = os.path.join(carpeta_actual, 'salones.csv')
salones=leer_salones_desde_csv(nombre_archivo)

##########################################################################################

##########################################################################################
#              FUNCIONES DEL ALGORITMO EVOLUTIVO DE HORARIOS
##########################################################################################

"""
Esta función nos ayuda a inicializar la población, es decir, crear examenes de manera aleatoria que contengan la información previamente dada.

"""

def inicializaPoblacionHorario(tamanoPob):
  pobinicial = []
  for i in range(tamanoPob):
    examenes = []
    for i in range(numMaterias):
      examen = Examen(salon=salones[random.randint(0, numerodesalones - 1)],
                      materia=materias[i],
                      horario=random.randint(0, 50))
      examenes.append(examen)
    pobinicial.append(examenes)
  return pobinicial

"""
La función evaluadora es la que va a revisar si un examen es valioso o no. En este caso revisa varias cosas, como si la hora es dentro de las deseadas, la capacidad del salón con respecto a la materia que tendrá su examen ahí y superposición de examenes ya sea en general o para algún alumno.

"""

def funcEvaluadora(solucion, pesoH, pesoC, pesoE, pesoA):
  puntaje_total = 0
  total_errores = 0 #No nada mas nos interesa la calificación sino la cantidad de errores.
  for examen in solucion:
    cursoid = examen.materia.materia_id
    salon_id = examen.salon.salon_id
    hora_inicio = examen.horario

    # Verificar si la hora de inicio es indeseada
    if hora_inicio in horas_indeseadas:
      puntaje_total -= pesoH  # Reducir el puntaje si es hora indeseada
      total_errores += 1

    # Verificar capacidad del salón
    if materias[cursoid].inscritos >= salones[salon_id].capacidad:
      puntaje_total -= pesoC  # Reducir el puntaje si el salón no tiene capacidad suficiente
      total_errores += 1

    # Verificar superposición de exámenes en el mismo salón
    for otro_examen in solucion:
      if otro_examen.salon.salon_id == salon_id and otro_examen.horario == hora_inicio and otro_examen != examen:
        puntaje_total -= pesoE  # Reducir el puntaje si hay superposición de exámenes en el mismo salón
        total_errores += 1
        break

    # Verificar superposición de exámenes para los alumnos
  for alumno in alumnos:
    for cursoid1 in alumno.materias_ids:
      for cursoid2 in alumno.materias_ids:
        if cursoid1 != cursoid2 and solucion[cursoid1].horario == solucion[
            cursoid2].horario:
          puntaje_total -= pesoA  # Reducir el puntaje si hay superposición de exámenes para un alumno
          total_errores += 1

  return puntaje_total, total_errores

"""
La función mutación recibe como parámetro un individuo. La función devuelve un
nuevo individuo al que se le haya modificado el salón o el horario en todos los 
examenes del individuo.
"""

def mutacion(individuo):
 
  nuevoIndividuo = []
  for examen in individuo:
    # Mantener el mismo curso y solo cambiar salón y horario
    if random.choice([True, False]):
      nuevoSalon = random.choice(salones)  # Seleccionar un nuevo salón
      nuevoHorario = examen.horario  # Mantener el mismo horario
    else:
      nuevoSalon = examen.salon  # Mantener el mismo salón (todo el objeto)
      nuevoHorario = random.randint(1, numMaterias)
    # Crear una nueva instancia de Examen con los cambios
    nuevoExamen = Examen(nuevoSalon, examen.materia, nuevoHorario)
    nuevoIndividuo.append(nuevoExamen)
  return nuevoIndividuo

"""
La función cruzamiento recibe como parámetro dos individuos. Devuelve un nuevo 
individuo manteniendo el salón y cambiando el horario o cambiando el salón y manteniendo el horario
"""

def cruzamiento(individuo1, individuo2):
 
  nuevoIndividuo = []
  for i in range(len(individuo1)):
    # Mantener el mismo curso y solo cambiar salón y horario
    if random.choice([True, False]):
      nuevoSalon = individuo2[
          i].salon  # Cambiar el salón (todo el objeto <-- salonid, capacidad)
      nuevoHorario = individuo1[i].horario  # Mantener el mismo horario
    else:
      nuevoSalon = individuo1[
          i].salon  # Mantener el mismo salón (todo el objeto <-- salonid, capacidad)
      nuevoHorario = individuo2[i].horario

    nuevo_examen = Examen(nuevoSalon, individuo1[i].materia, nuevoHorario)
    nuevoIndividuo.append(nuevo_examen)
  return nuevoIndividuo


##########################################################################################

##########################################################################################
#                           ALGORITMO EVOLUTIVO HORARIOS
##########################################################################################
"""
Esta es la función principal del algorimo evolutivo. Nos ayuda a encontrar la mejor solución posible, esto mediante el uso de evaluaciones de nuestra población, mutación y cruzamiento hasta que lleguemos a cierta varianza o un número máximo de generaciones.

"""
def evolutivoHorarios(tamanoPoblacion, numeroGeneraciones, poblacionSoluciones,
                      varianzaLimite, probamutacion, pesoH, pesoC, pesoE,
                      pesoA):
  tot_errores = 0
  varianza = varianzaLimite + 1
  # SI LLEGAMOS AL LIMITE DE GENERACIONES O CONVERGIÓ, REGRESA LOS PARAMETROS NECESARIOS
  while (numeroGeneraciones > 0 and (varianza > varianzaLimite)):
    varianza = 0
    evaluaciones = [] #Aquí es donde guardamos las evaluaciones de cada individuo.
    aptos = [] #Aquí es donde guardamos los aptos que pasarán a la siguiente generación.
    promedio = 0

    # EVALUA TODOS LOS INDIVIDUOS DE LA POBLACIÓN Y GUARDA SUS "CALIFICACIÓNES"
    for i in range(tamanoPoblacion):
      a, _ = funcEvaluadora(poblacionSoluciones[i], pesoH, pesoC, pesoE, pesoA)
      evaluaciones.append(a)
      promedio += evaluaciones[i]

    promedio /= tamanoPoblacion

    # SI SON MEJORES QUE EL PROMEDIO, MANDALOS AL VECTOR DE INDIVIDUOS "APTOS"
    for i in range(tamanoPoblacion):
      if evaluaciones[i] >= promedio:
        aptos.append(poblacionSoluciones[i])
    #evitar errores con varianzas muy pequeñas
    while (len(aptos) < 2):
      aptos.append(poblacionSoluciones[random.randint(0, tamanoPoblacion-1)])

    varianza=np.var(evaluaciones)

    # CREA LA NUEVA GENERACIÓN UTILIZANDO MUTACIÓN Y CRUZAMIENTO. AGREGALOS A EL NUEVO VECTOR "NUEVAGENERACION"

    nuevaGeneracion = []
    n = 0
    while (n < tamanoPoblacion):
      elegidos = random.sample(range(len(aptos)), 2)
      if (random.random() < probamutacion):
        # mutamos
        nuevoIndividuo = mutacion(aptos[elegidos[0]])
      else:
        # cruzamos
        nuevoIndividuo = cruzamiento(aptos[elegidos[0]], aptos[elegidos[1]])

      nuevaGeneracion.append(nuevoIndividuo)
      n += 1

    numeroGeneraciones -= 1

    poblacionSoluciones = nuevaGeneracion #Nuestra nueva población es la nueva generación.

  #EVALUAMOS LA ÚLTIMA GENERACIÓN
  promedio = 0
  maxval = float('-inf')
  posmax = 0
  evaluaciones = []

  for i in range(tamanoPoblacion):
    puntaje, errores = funcEvaluadora(poblacionSoluciones[i], pesoH, pesoC,
                                      pesoE, pesoA)
    evaluaciones.append(puntaje)
    if (evaluaciones[i] > maxval):
      posmax = i
      maxval = evaluaciones[i]
      tot_errores = errores
    promedio += evaluaciones[i]

  promedio /= tamanoPoblacion
  varianza=np.var(evaluaciones)

  return poblacionSoluciones[posmax], varianza, numeroGeneraciones, tot_errores
#Esto nos regresa la mejor solución, la varianza entre la población de soluciones, el número de generaciones y el total de errores.



"""
Esta función Handle calcula los tiempos de ejecución para luego utilizarlos como parámetro en el algoritmo evolutivo general. Además, genera una población inicial aleatoriamente.
"""


#UTILIZA LA FUNCIÓN ANTERIOR PERO AHORA TAMBIÉN REGRESAMOS EL TIEMPO DE EJECUCIÓN PARA EL ALGORITMO EVOLUTIVO GENERAL.

def evolutivoHorariosHandle(tamanoPoblacion, numeroGeneraciones,
                             varianzaLimite, probamutacion,
                            pesoH, pesoC, pesoE, pesoA):

  # Se hace una pobalción inicial aleatoria
  poblacionSoluciones=inicializaPoblacionHorario(tamanoPoblacion)
  inicio = time.time()
  mejorsolucion, varianzafinal, Generaciones, totalError = evolutivoHorarios(
      tamanoPoblacion, numeroGeneraciones, poblacionSoluciones, varianzaLimite,
      probamutacion, pesoH, pesoC, pesoE, pesoA)
  fin = time.time()
  tiempoEjecucion = fin - inicio
  return tiempoEjecucion, mejorsolucion, varianzafinal, numeroGeneraciones - Generaciones, totalError



##########################################################################################
#          FUNCIONES DEL ALGORITMO EVOLUTIVO DE PARAMETROS DE ALGORITMO EVOLUTIVO
##########################################################################################


"""
Esta función nos ayuda a inicializar la población, es decir, crear vectores de 8 elementos de manera aleatoria. Estos vectores contienen nuevos parámetros para el algoritmo evolutivo general. La idea es volver a aplicar un algoritmo evolutivo para encontrar los mejores parámetros de ejecución para los horarios.

"""

def inicializaPoblacionGen(tamanoPoblacion):
  poblacion_sol=[]
  #quiero una lista de vectores de 8 elementos que representan los parametros 
  for i in range(tamanoPoblacion):
    params=[random.randint(1,50),random.randint(1,50),random.randint(1,500),random.random(),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
    poblacion_sol.append(params)
  return poblacion_sol


"""
Esta función es la evaluadora pero ahora de nuevos parámetros. En vez de evaluar examanes, va a premiar soluciónes que tengan la menor candidad de tiempo en ejecución, la menor cantidad de errores y que las soluciones tengan una varianza menor.

"""
  
def funcEvalParams(tiempoEjecucion, totalError, Varianza):
  a = ((math.exp(tiempoEjecucion/10)) / 20) - 0.05
  b = 1
  c = 1
  return (0 - (a) - (b * totalError) - (c * Varianza))


"""
Esta es la mutación para el algoritmo evolutivo general. En este caso para cada uno de los parámetros tiene 50% de probabilidad de cambiar su valor.
"""

def mutacionParametros(params):
  # params tiene (tamanoPob,numeroGeneraciones,VarianzaMaximaConvergencia,ProbabilidadMutar,pesoH,pesoC,pesoE,pesoA)
  # para todos los parametros, 50% de probabilidad de mutar ese parametro

  nuevoIndividuo = []
  # tamañoPob € [1,50]
  if random.choice([True, False]):
    nuevoIndividuo.append(random.randint(1, 50))
  else:
    nuevoIndividuo.append(params[0])
  # Numero Generaciones € [1,50]
  if random.choice([True, False]):
    nuevoIndividuo.append(random.randint(1, 50))
  else:
    nuevoIndividuo.append(params[1])
  # VarianzaMaximaConvergencia € [1,500]
  if random.choice([True, False]):
    nuevoIndividuo.append(random.randint(1, 500))
  else:
    nuevoIndividuo.append(params[2])
  # ProbabilidadMutar € [0,1]
  if random.choice([True, False]):
    nuevoIndividuo.append(random.random())
  else:
    nuevoIndividuo.append(params[3])
  # pesoH € [1,10]
  if random.choice([True, False]):
    nuevoIndividuo.append(random.randint(1, 10))
  else:
    nuevoIndividuo.append(params[4])
  # pesoC € [1,10]
  if random.choice([True, False]):
    nuevoIndividuo.append(random.randint(1, 10))
  else:
    nuevoIndividuo.append(params[5])
  # pesoE € [1,10]
  if random.choice([True, False]):
    nuevoIndividuo.append(random.randint(1, 10))
  else:
    nuevoIndividuo.append(params[6])
  # pesoA € [1,10]
  if random.choice([True, False]):
    nuevoIndividuo.append(random.randint(1, 10))
  else:
    nuevoIndividuo.append(params[7])

  return nuevoIndividuo

"""
Este es el cruzamiento para el algoritmo evolutivo general. En este caso para cada uno de los parámetros tiene 50% de probabilidad de que intercambie con la madre o el padre..
"""

def cruzamientoParametros(params1, params2):
  nuevoIndividuo = []
  # Para cada paramtero, lo toma del padre o lo toma de la madre
  for i in range(len(params1)):
    if random.choice([True, False]):
      nuevoIndividuo.append(params1[i])
    else:
      nuevoIndividuo.append(params2[i])
  return nuevoIndividuo

##########################################################################################


##########################################################################################
#                     ALGORITMO EVOLUTIVO DE PARAMETROS DE ALGORITMO EVOLUTIVO
##########################################################################################


"""
Esta es la función principal del algorimo evolutivo general. Nos ayuda a encontrar la mejor solución posible, esto mediante el uso de evaluaciones de nuestra población, mutación y cruzamiento hasta que lleguemos a cierta varianza o un número máximo de generaciones.

"""

def evolutivoGeneral(tamanoPoblacion, numeroGeneraciones, poblacionSoluciones,
                      varianzaLimite,probamutacion):

  varianza = varianzaLimite + 1
  # SI LLEGAMOS AL LIMITE DE GENERACIONES O CONVERGIÓ, REGRESA LOS PARAMETROS NECESARIOS
  while (numeroGeneraciones > 0 and (varianza > varianzaLimite)):
    varianza = 0
    evaluaciones = []
    aptos = []
    promedio = 0

    # EVALUA TODOS LOS INDIVIDUOS DE LA POBLACIÓN Y GUARDA SUS "CALIFICACIÓNES"
    for i in range(tamanoPoblacion):
      tiempoEjecucion,mejorsolucion,varianzafinal,_,total_errores = evolutivoHorariosHandle(*poblacionSoluciones[i])
      evaluaciones.append(funcEvalParams(tiempoEjecucion,total_errores,varianzafinal))
      promedio += evaluaciones[i]

    promedio /= tamanoPoblacion

    # SI CUMPLEN CON LOS CRITERIOS, MANDALOS AL VECTOR DE INDIVIDUOS APTOS
    for i in range(tamanoPoblacion):
      if evaluaciones[i] >= promedio:
        aptos.append(poblacionSoluciones[i])

    while (len(aptos) < 2):
      aptos.append(poblacionSoluciones[random.randint(0, tamanoPoblacion-1)])

    varianza=np.var(evaluaciones)


    # CREA LA NUEVA GENERACIÓN UTILIZANDO MUTACIÓN Y AGREGALOS A EL NUEVO VECTOR "NUEVAGEN"

    nuevaGeneracion = []
    n = 0
    while (n < tamanoPoblacion):
      #coin toss (le sale 1 o 0)
      elegidos = random.sample(range(len(aptos)), 2)
      if (random.random()<probamutacion):
        # mutamos
        nuevoIndividuo = mutacionParametros(aptos[elegidos[0]])
      else:
        nuevoIndividuo = cruzamientoParametros(aptos[elegidos[0]],aptos[elegidos[1]])

      nuevaGeneracion.append(nuevoIndividuo)
      n += 1

    numeroGeneraciones -= 1

    poblacionSoluciones = nuevaGeneracion

  # mejorsol es la mejor solución del algoritmo evolutivo de los horarios que se encontro con 
  # el parametro que dio una mejor calificación en terminos de la solucíon(evaluada con la función evaluadora)
  maxval = float('-inf')
  posmax = 0
  evaluaciones = []
  for i in range(tamanoPoblacion):
    tiempoEjecucion,mejorsolucion,varianzafinal,_,total_errores = evolutivoHorariosHandle(*poblacionSoluciones[i])
    evaluaciones.append(funcEvalParams(tiempoEjecucion,total_errores,varianzafinal))
    if (evaluaciones[i] > maxval):
      posmax = i
      # evaluación de la "ejecuion" del algoritmo evolutivo sobre los parametros: poblacionSoluciones[i]
      maxval = evaluaciones[i]
      mejorsol=mejorsolucion
      mejortiempo=tiempoEjecucion
      minimoErrores=total_errores

  # poblacionSoluciones[posmax]: La mejor solucion "DE PARAMETROS"
  # maxval: La mejor calificacion "DE LA EVALUADORA DE PARAMETROS"
  # mejorsol: La mejor solución "AL PROBLEMA DE LOS HORARIOS DE EXAMENES FINALES"
  # mejortiempo: El tiempo de ejecución del algoritmo evolutovo de horarios bajo los mejores párametros del algoritmo evolutivo de horarios.
  # minimoErrores: El número de errores en la solución obtenida al utilizar los mejores parámetros del algoritmo evolutivo de horarios.
  return poblacionSoluciones[posmax], maxval,mejorsol,mejortiempo,minimoErrores



"""
Esta función Handle utiliza la función del evolutivo general y agrega el tiempo de ejecución del evolutivo general. Además, genera una  población inicial aleatoriamente.

"""


def evolutivoGeneralHandle(tamanoPoblacion, numeroGeneraciones,
  varianzaLimite,probamutacion):

  poblacionSoluciones=inicializaPoblacionGen(tamanoPoblacion)
  inicio = time.time()
  mejoresParams,mejorCalif,mejorHorario,mejortiempoHorarios,minimoErrores=evolutivoGeneral(tamanoPoblacion, numeroGeneraciones, poblacionSoluciones,
    varianzaLimite,probamutacion)
  fin = time.time()
  tiempoEjecucion = fin - inicio
  return tiempoEjecucion,mejoresParams,mejorCalif,mejorHorario,mejortiempoHorarios,minimoErrores

##########################################################################################

##########################################################################################
#                       EJECUION PRINCIPAL
##########################################################################################


"""
MANUAL DE USUARIO
Este programa contiene la implementación de dos algoritmos evolutivos. Uno de ellos se encarga de asignar
horarios y lugares para los exámenes finales de una institución educativa y el otro de maximizar el rendimiento y la 
calidad de los resultados del algoritmo encargado de los horarios.

Para utilizar el algoritmo evolutivo encargado de asignar horarios y lugares puede llamar a la función evolutivoHorariosHandle().
Esta recibe los siguientes parámetros:
-tamanoPoblacion: un número entero mayor a 0. Tamaño de la población de soluciones.
-numeroGeneraciones: un número entero mayor a 0. Número de ejecuciones a realizar. Se utiliza como condición de paro del algoritmo.
-varianzaLimite: un número entero mayor o igual a 0. Se utiliza como criterio de convergencia del algoritmo.
-probamutacion: un número entre 0 y 1. Determina con qué probabilidad se da mutación. La probabilidad de que se de cruzamiento es el complemento (1-probamutacion)
-pesoH: un número positivo. Determina que tanto influye en la calificación de un horario si realizan exámenes en horarios indeseados (muy temprano, muy tarde o a la hora de la comida).
-pesoC: un número positivo. Determina que tanto influye en la calificación de un horario si se realizan exámenes en salones con capacidad insuficiente.
-pesoE: un número positivo. Determina que tanto influye en la calificación de un horario si se realizan dos exámenes en el mismo salón y a la misma hora.
-pesoA: un número positivo. Determina que tanto influye en la calificación de un horario si se asignan horarios de exámenes que impidan a los estudiantes asistir a todos sus exámenes; 
si un alumno debe estar en varios exámenes a la misma hora.

La función regresa los siguientes parámetros:
-tiempoEjecucion: Es un valor numérico que representa la cantidad de segundos que se tardó en ejecutar el algoritmo.
-mejorsolucion: Es una lista que contiene a todos los exámenes asignados dentro de una solución. Se puede imprimir utilizando un
ciclo for each aprovechándose de que la clase Examen posee una función __str__
-varianzafinal: Es un valor numérico. Indica que tan dispersas son las soluciones (en términos de la función de aptitud).
-numeroGeneraciones: Es un valor numérico positivo. Indica cuantas generaciones pasaron antes de que la ejecución del algoritmo evolutivo parase.
-totalError: Es un valor numérico mayor o igual a 0. Indica el total de errores (aquellos que se encarga de penalizar la función de aptitud) que posee la solución encontrada por el algoritmo.

Se puede utilizar la plantilla proporcionada para realizar varias ejecuciones del algoritmo evolutivo de horarios.
Basta con elegir el número de iteraciones que se quieren realizar y los valores que se quiere que tomen los parámetros de la función evolutivoHorariosHandle().
Los resultados se guardan en un archivo .csv dentro de la misma carpeta dónde se encuentre este archivo .py


Para utilizar el algoritmo evolutivo encargado de encontrar parámetros óptimos para el algoritmo evolutivo de horarios, puede llamar a la función evolutivoGeneralHandle().
Esta recibe los siguientes parámetros:
-tamanoPoblacion: un número entero mayor a 0. Tamaño de la población de soluciones.
-numeroGeneraciones: un número entero mayor a 0. Número de ejecuciones a realizar. Se utiliza como condición de paro del algoritmo.
-varianzaLimite: un número entero mayor o igual a 0. Se utiliza como criterio de convergencia del algoritmo.
-probamutacion: un número entre 0 y 1. Determina con qué probabilidad se da mutación. La probabilidad de que se de cruzamiento es el complemento (1-probamutacion)

La función regresa los siguientes parámetros:
-tiempoEjecuciónTotal: Es un valor numérico que representa la cantidad de segundos que se tardó en ejecutar el algoritmo.
-mejoresParams: Es una lista de 8 parámetros. Son los parámetros que recibe la función evolutivoHorariosHandle().
-mejorCalif: Es un valor numérico. Indica la aptitud de los mejores parámetros encontrados por el algoritmo.
-mejorHorario: Es una lista que contiene a todos los exámenes asignados al ejecutar el algoritmo evolutivo de horarios con los parámetros encontrados
por este algoritmo. Se puede imprimir utilizando un ciclo for each aprovechándose de que la clase Examen posee una función __str__
-mejorTiempo: Es un valor numérico que representa la cantidad de segundos que se tardó en ejecutar el algoritmo evolutivo de horarios utilizando los mejores parámetros
encontrados por el algoritmo.
-minimoErrores: Es un valor numérico mayor o igual a 0. Indica el total de errores (aquellos que se encarga de penalizar la función de aptitud) que posee 
la solución dada por el algoritmo evolutivo de horarios cuando se le ejecuta con los parámetros encontrados por este algoritmo evolutivo.

Se puede utilizar la plantilla proporcionada a continuación para realizar varias ejecuciones del algoritmo evolutivo de algoritmo evolutivo.
Basta con modificar el número de iteraciones y los valores que se quiere que tomen los parámetros de la función evolutivoGeneralHandle() en cada iteración.
Los resultados se guardan en archivos .csv dentro de la misma carpeta dónde se encuentre este archivo .py


En la sección "INFORMACIÓN DE LA UNIVERSIDAD" se pueden modificar los valores que tienen las variables numerodealumnos, numMaterias,numerodesalones,horasTotalesExamenes y horas_indeseadas
para poder aplicar el algoritmo a otras instituciones educativas.
Debe tenerse en cuenta al momento de modificarlos, se deben modificar también los archivos .csv desde los cuales se lee la información de cada uno de ellos.

"""

## PLANTILLA evolutivoHorariosHandle()
# nombre_archivo = os.path.join(carpeta_actual, 'ResultadosMejoresParams.csv')
# for i in  range(1):
#   tiempoEjecucion,mejorsolucion,varianzafinal,_,total_errores=evolutivoHorariosHandle(28,18,70,0.092438951,4,1,1,6)
#   with open(nombre_archivo, mode='a', newline='') as file:
#       writer = csv.writer(file)
#       # Write the new data to the file
#       writer.writerow([tiempoEjecucion,varianzafinal,total_errores])
#       print("vamos en la ",i)

##########################################################################

## PLANTILLA evolutivoGeneralHandle()

# for i in range(40):
#   Gen_tamanoPoblacion=random.randint(1,5)
#   Gen_numeroGeneraciones=random.randint(1,5)
#   Gen_varianzaLimite=random.randint(1,500)
#   Gen_probamutacion=random.random()
#   tiempoEjecuciónTotal,mejoresParams,mejorCalif,mejorHorario,mejorTiempo,minimoErrores=evolutivoGeneralHandle(Gen_tamanoPoblacion,Gen_numeroGeneraciones,Gen_varianzaLimite,Gen_probamutacion)

#   nombre_archivo = os.path.join(carpeta_actual, 'Tiempos_Ejecucion_Resultados.csv')

#   with open(nombre_archivo, mode='a', newline='') as file:
#       writer = csv.writer(file)
#       # Write the new data to the file
#       writer.writerow([tiempoEjecuciónTotal,mejorTiempo])

#   nombre_archivo = os.path.join(carpeta_actual, 'Parametros_Resultados.csv')
#   with open(nombre_archivo, mode='a', newline='') as file:
#       writer = csv.writer(file)
#       # Write the new data to the file
#       writer.writerow(mejoresParams)

#   nombre_archivo = os.path.join(carpeta_actual, 'Calificaciones_Resultados.csv')
#   with open(nombre_archivo, mode='a', newline='') as file:
#       writer = csv.writer(file)
#       # Write the new data to the file
#       writer.writerow([mejorCalif,minimoErrores])

#   print("Vamos en la iteracion: ",i) 