
from main import entero_a_romano

valor_final = entero_a_romano(1994)

#def test_prueba_entero_a_romano():
    #assert valor_final == [1000,900,90,4]

#test_prueba_entero_a_romano(valor_final)

def test_prueba_entero_a_romano():
    assert valor_final == 'MCMXCIV'