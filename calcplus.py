#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoohija import CalculadoraHija


if __name__ == "__main__":
    nombre_fichero = sys.argv[1]
    try:
        fichero = open(nombre_fichero)
    except IOError:
        sys.exit("No existe el fichero indicado")
    calculadora = CalculadoraHija()

    for line in fichero.readlines():
        elementos = line.split(',')
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
