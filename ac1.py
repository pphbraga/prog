# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:17:50 2023

@author: 202051870257
"""
#Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0. O programa deve pedir os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara. Considere que as raízes são reais. Exemplo: a = 1, b = -6, c = 8 dá como raízes 4 e 2.

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


discriminante = b ** 2 - 4 * a * c


raiz1 = (-b + (discriminante ** 0.5)) / (2 * a)
raiz2 = (-b - (discriminante ** 0.5)) / (2 * a)


print(f"As raízes da equação são: {raiz1} e {raiz2}")



# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:12:23 2023

@author: 202051870257
"""

# Elabore um programa que leia uma variável inteira ano. Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

ano = int(input("Digite um ano: "))


ano_bissexto = (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)


print(f"{ano} é um ano bissexto: {ano_bissexto}")