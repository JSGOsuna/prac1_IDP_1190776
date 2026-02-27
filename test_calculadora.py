from calculadora import Calculadora
#Método para probar la función add de la clase Calculadora
def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculadora()
    assert calc.subtract(5, 2) == 8

#python -m pytest
#python -m pytest -v