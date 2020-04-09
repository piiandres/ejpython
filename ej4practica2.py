import random


#Inicializa la lista de posibles preguntas con sus respectivas respuestas
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no'],['La capital de Chubut es Comodoro Rivadavia','no'],['San Martín nació en la provincia de Corrientes','si']]


print('Las preguntas deben responderse con si o no \n')

puntaje= 0

def pregun(preguntas,llena,puntaje):
	
	#Selecciona una pregunta random
	ran=random.randrange(len(preguntas))
	print(preguntas[ran][0])
	resp= str(input())
	
	#Compara si la respuesta dada es correcta
	if (resp.lower() == preguntas[ran][1]):
		print('Correcto')
		puntaje=puntaje+1
	else:
		print('Incorrecto')
		
	#Elimina el elemento de la lista	
	preguntas.pop(ran)
	
	#Chequea si hay elementos en la lista
	if not preguntas:
		llena=False
		
	return llena,puntaje



def total(puntaje):
	print('Tu puntaje total:',puntaje)

		
#Comienza el programa 
llena=True
while llena:
	tupla= pregun(preguntas,llena,puntaje)
	llena=tupla[0]
	puntaje=tupla[1]
	
total(puntaje)
	
	

			
