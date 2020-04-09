import random

preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no'],['La capital de Chubut es Comodoro Rivadavia','no'],['San Martín nació en la provincia de Corrientes','si']]
print('Las preguntas deben responderse con si o no \n')
puntaje= 0
def pregun(preguntas,llena,puntaje):
	ran=random.randrange(len(preguntas))
	print(preguntas[ran][0])
	resp= str(input())
	if (resp.lower() == preguntas[ran][1]):
		print('Correcto')
		puntaje=puntaje+1
	else:
		print('Incorrecto')
	preguntas.pop(ran)
	if not preguntas:
		llena=False
	return llena,puntaje

def total(puntaje):
	print('Tu puntaje total:',puntaje)

		

llena=True
while llena:
	tupla= pregun(preguntas,llena,puntaje)
	llena=tupla[0]
	puntaje=tupla[1]
total(puntaje)
	
	

			
