#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o el factorial en un rango            *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def factorial_range(start, end):
    for num in range(start, end + 1):
        print("Factorial", num, "! es", factorial(num))

def parse_range(range_str):
    if "-" in range_str:
        start, end = map(int, range_str.split("-"))
        return start, end
    else:
        start = int(range_str.split("-")[0])
        return start, 60

if len(sys.argv) == 1:
    try:
        input_range = input("Ingrese un rango de números (ej. -10 o desde-10): ")
        start, end = parse_range(input_range)
    except ValueError:
        print("Debe ingresar un rango válido en el formato -hasta o desde-.")
        sys.exit()
else:
    start, end = parse_range(sys.argv[1])

factorial_range(start, end)

