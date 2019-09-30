#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora


class CalculadoraHija(Calculadora):
    def mult(self, op1, op2):
        return(op1 * op2)

    def div(self, op1, op2):
        if op2 == 0:
            sys.exit("Division by zero is not allowed")
        else:  
            return op1 / op2


if __name__ == "__main__":
    calculadora = CalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora.sum(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.rest(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = calculadora.mult(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = calculadora.div(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplica o divide.')

    print(result)
