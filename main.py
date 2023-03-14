
class RomanNumberError(Exception):
    pass

diccionario = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

unidades = {
    1: 'I',2: 'II', 3: 'III',
    4: 'IV', 5: 'V', 6:'VI',
    7:'VII', 8:'VIII', 9:'IX'
}
decenas= {
    10: 'X',20: 'XX', 30: 'XXX',
    40: 'XL', 50: 'L', 60:'LX',
    70:'LXX', 80:'LXXX', 90:'XC'
}
centenas = {
    100: 'C',200: 'CC', 300: 'CCC',
    400: 'CD', 500:'D' , 600:'DC',
    700:'DCC', 800:'DCCC', 900:'CM'
}
millares={
    1000: 'M', 2000:'MM', 3000:'MMM'
}



    

def entero_a_romano(numero):
    numero = str(numero) #transformar en cadena
    list_numero = list(numero) # transformar cadena en lista

    for i in range(0, len(list_numero)):       
        if i == 0:
            list_numero[i] = int(list_numero[i])*1000 
        if i == 1:
            list_numero[i] = int(list_numero[i])*100
        if i == 2:
            list_numero[i] = int(list_numero[i])*10
        if i == 3:
            list_numero[i] = int(list_numero[i])     

    return list_numero   

print(entero_a_romano(1991))
    

