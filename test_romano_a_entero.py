from main import romano_a_entero,RomanNumberError,restas
import pytest

def test_romano_a_entero_I():
    assert romano_a_entero("I") == 1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero("IV") == 4    

def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises( RomanNumberError ) as exceptionInfo:
        romano_a_entero("LIIII")
    assert str( exceptionInfo.value ) == "No se puede repetir el valor mas de tres veces seguidas"    

def test_romano_a_entero_no_repetir_caracteres_especiales():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("DD")
        print("aqui",type(exeptionInfo.value))
    assert str(exeptionInfo.value) == "Los caractares D, L y V no se pueden repetir"; 

def test_romano_a_entero_no_repetir_caracteres_especiales():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("VL")
        print("aqui",type(exeptionInfo.value))
    assert str(exeptionInfo.value) == "Los caractares D, L y V no se pueden restar"; 

def test_romano_a_entero_restasI():
    with pytest.raises( RomanNumberError ) as exeptionInfo: 
        romano_a_entero("IL")
    assert str(exeptionInfo.value) == "I solo se puede restar de V y X"

def test_romano_a_entero_restasX():
    with pytest.raises( RomanNumberError ) as exeptionInfo: 
        romano_a_entero("XM")
    assert str(exeptionInfo.value) == "X solo se puede restar de L y C"

