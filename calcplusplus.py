#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
from calcoohija import CalculadoraHija

if __name__ == "__main__":

	calculadora = CalculadoraHija()
	nombre_fichero = sys.argv[1]
	with open(nombre_fichero) as texto_archivo:
		lineas = csv.reader(texto_archivo)
		for elementos in lineas:
		    resultado = int(elementos[1])
		    if elementos[0] == "suma":
		        try:
		            for operando in elementos[2:]:
		                resultado = calculadora.sum(resultado, int(operando))
		            print(resultado)
		        except ValueError:
		            print("Un valor es valido")
		    elif elementos[0] == "resta":
		        try:
		            for operando in elementos[2:]:
		                resultado = calculadora.rest(resultado, int(operando))
		            print(resultado)
		        except ValueError:
		            print("Un valor no es valido")
		    elif elementos[0] == "multiplica":
		        try:
		            for operando in elementos[2:]:
		                resultado = calculadora.mult(resultado, int(operando))
		            print(resultado)
		        except ValueError:
		            print("Un valor no es valido")
		    elif elementos[0] == "divide":
		        try:
		            for operando in elementos[2:]:
		                resultado = calculadora.div(resultado, int(operando))
		            print(resultado)
		        except ValueError:
		            print("Un valor no es valido")
		    else:
		        print("Las operaciones son: suma, resta, multiplica y divide")
