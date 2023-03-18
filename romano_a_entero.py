'''
1-Crear una funcion que pase de entero >0 y <4000 a romano
2-cualquier otra entrada debe dar error

Casos de prueba
a)1994 -> MCMXCIV
b)4000 -> RomanNumberError("El valor debe ser menor de 4000")
c)"unacadena"-> RomanNumberError("Debe ser un entero")
d) 0-> RomanNumberError("El valor debe ser mayor de cero")
e) -3 ->RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")

M → 1000
D → 500
C → 100
L → 50
X → 10
V → 5
I → 1
'''
diccionario={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

dic_entero_a_romanos={
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX',

    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC',

    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM',

    1000:'M',2000:'MM',3000:'MMM'
}

dic_romano_a_entero={
    'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
}


class RomanNumberError(Exception):
    pass

#si el caracter romano es mayor que el anterior, se deben restar el mayor menos el menor
#si el caracter posterior es menor o igual al actual se suman
"""
Los símbolos se suman y ordenan de mayor a menor
Si un símbolo de menor valor antecede a uno de mayor, el de menor valor se resta al de mayor
Solo se puede restar un símbolo de valor pequeño de cualquier símbolo de valor grande.
Los símbolos "I", "X", "C" y "M" se pueden repetir tres veces seguidas, pero no más. (Pueden aparecer más de tres veces si no aparecen secuencialmente, como en XXXIX.) "D", "L" y "V" no se pueden repetir.
Restas
"I" solo se puede restar de "V" y "X".
"X" se puede restar de "L" y "C" solamente. 
"C" se puede restar de "D" y "M" solamente. 
"V", "L" y "D" nunca se pueden restar.
Si se ha producido repetición de “I”, “X” o “C” ya no pueden restarse de sus digitos respectivos. Esto IIX es incorrecto, IX es correcto
Las restas correctas solo pueden realizarse una vez

"""
def romano_a_entero(valor:str)->int:
    lista_romano = list(valor)
    valor_entero=0
    longitud= len(lista_romano)
    contador = 1

    for pos in range(longitud):
        if pos != 0:
            if lista_romano[pos] != lista_romano[pos-1]:
                contador = 1
            else:
                contador +=1
                if contador > 3:
                    return "Error el número romano ingresado no es valido"
        
        
        if pos !=0:
            if dic_romano_a_entero.get(lista_romano[pos-1],0) < dic_romano_a_entero.get(lista_romano[pos],0):
               valor_entero -= dic_romano_a_entero.get(lista_romano[pos-1],0)#restar al valor anterior
               valor_entero +=   ( (dic_romano_a_entero.get(lista_romano[pos],0))  - (dic_romano_a_entero.get(lista_romano[pos-1],0) ) )
            else:
                valor_entero += dic_romano_a_entero.get(lista_romano[pos],0)  
        else:
            valor_entero += dic_romano_a_entero.get(lista_romano[pos],0)
  
    return valor_entero
    

'''
def entero_a_romano(numero:int)->str:
    numero = "{:0>4d}".format(numero)
    list_numero = list(numero)
    valor_romano=""
    longitud= len(list_numero)
    
    for i in range(longitud):
        longitud = longitud-1
        list_numero[i] = list_numero[i]+"0"*longitud
        valor_romano +=dic_entero_a_romanos.get( int(list_numero[i]) ,"")

    return valor_romano
'''
print(romano_a_entero("MCMXCI") )

