# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 10:05:38 2023

@author: I_Henri
"""
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import Counter

def drop(balls, k, n):
    for i in range(k):
        position = 0
        for _ in range(n):
            position += random.choice([-1,1])
        balls[i] = position

def frequencyCalculator(frequency, n, balls, positions):
    filteredFrequency = []
    filteredPositions = []
    for i in range((2*n)+1):
        frequency [i]= Counter(balls)[positions[i]]
    for i in range((2*n)+1):
        if frequency [i] != 0:
            filteredFrequency.append(frequency[i])
            filteredPositions.append(positions[i])
            
    return filteredFrequency, filteredPositions
    
def plot(positions, n, frequency):
    plt.plot(positions, frequency, 'o', color='black')
    plt.show()
    
def boardSpin():
    print("Esse programa simula um tabuleiro de Galton.\n\nO Tabuleiro de Galton, também conhecido como Quincunx, é um dispositivo inventado por Sir Francis Galton \npara demonstrar o teorema do limite central, em particular, que a distribuição normal é aproximada \nà distribuição binomial. Entre suas aplicações, oferecer ideias sobre regressão para média.\n\nO tabuleiro consiste de uma placa vertical com fileiras entrelaçadas de pinos. Bolas são jogadas a partir do topo; \nao bater nos pinos, elas se distribuem para a esquerda ou para a direita. Caso a probabilidade da bola ir para direita seja \nigual a probabilidade da bola ir para a esquerda, ao cair nas bandejas inferiores, a altura das bolas acumuladas nas \nbandejas, eventualmente, irá simular uma curva em forma de sino.\n")
    n = int(input("Digite o número de fileiras do tabuleiro: "))
    k = int(input("Digite o número de bolas do tabuleiro: "))
    balls = np.zeros(k)
    frequency = np.zeros((2*n)+1) 
    positions = np.zeros((2*n)+1) 
    for i in range((2*n)+1):
        positions[i] = i-n
    drop(balls, k, n)
    filteredFrequency, filteredPositions = frequencyCalculator(frequency, n, balls, positions)
    plot(filteredPositions, n, filteredFrequency)
    
boardSpin()
