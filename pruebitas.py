'''
#repaso sobre diccionarios en python
d1={
    "nombre":"Carlos",
    "edad":45,
    "dni":"X2454151",
    10:"X"
}
print(d1)
d2= dict([
    ('nombre','Dulce'),
    ('edad',25),
    ('dni','T389473')
])
print(d2)

#funciones para diccionarios
valor = d1.get(100)
if valor == None:
    print("No existe")
else:
   print("funcion get(): ",valor)

print( d2.get(150,1000))   

#funcion clear, elimina todo el diccionario
d2.clear()
print("funcion clear :",d2)

#funcion items devuelve una lista con los keys y values del diccionario
valores = d1.items()
print("funcion items :",valores)

for key, value in valores:
    print(str(key)+"-"+str(value))
#funcion keys, devolver una lista con todas las keys del diccionario

llaves = d1.keys()
print("funcion key: ",llaves)

#funcion values, devolver una lista con todos los valores del diccionario

valores_dic = d1.values()
print("funcion values: ",valores_dic)

#funcion pop para eliminar key
d1.pop(10)
print("funcion pop: ",d1)

#funcion update para añadir nuevos valores al diccionario
d1.update({'a':100,'b':50,'c':60})
print("funcion update:,",d1)
#popitem() elimina de manera aleatoria un elemento del diccionario
d1.popitem()
print("funcion popitem",d1)


'''
'''
n=3
valor = "{:0>4d}".format(n)
print(valor)

n=str(n)
while len(n)<4:
    n = "0"+n
print("prueba",n)   
'''


'''
lista=['0','3','3','3']

longitud= len(lista)

for i in range(longitud):
     longitud = longitud-1
     lista[i] = lista[i]+"0"*longitud

print(lista)
'''

'''
try:
    division = 10/0
except Exception as e:
    print(e)
''' 
#from main import RomanNumberError

#def pruebaExcepcion():
    #raise RomanNumberError("Esto es mi excepcion")#genera una excepcion

#pruebaExcepcion()
"""
try:
    #division = 10/0
    pruebaExcepcion()
except Exception as e:
    print("ingresa aqui")
   """
"""
dia = 'martes'

if dia == 'sabado':
    print("es sabado")

elif dia == 'viernes':
    print("es viernes")

elif dia =='domingo':
    print("Es domingo")

else:
    print("no es viernes sabado ni domingo") 
"""
'''
frutas=['fresa','manzana','pera','platano']

if 'piña' in frutas:
    print("fresa no se encuentra")
'''

restas = { 'I':('V','X'), 'X':('L','C'),'C':('D','M') }

restas['IL'][0]

if 'L' in restas:
    print("si esta")
