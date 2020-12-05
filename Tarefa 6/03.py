from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse
import os
import math
from matplotlib import pyplot as plt

def buscaImg(listaImg):
    
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    
    ranges = h_ranges + s_ranges 
    channels = [0, 1]
    
    #criando e preenchendo vetor para calculo de hist de cada img do vetor de listaImg
    listaHist = []
    tamList = len(listaImg)
    
    for i in range(0,tamList):
        listaHist.append(cv.calcHist(listaImg[i], channels, None, histSize, ranges, accumulate=False))
        cv.normalize(listaHist[i], listaHist[i], alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    
    #comparando os hist com cada metodo e armazenando tudo em um vetor para cada metodo
    comparacaoCorrelacao = []
    comparacaoChi = []
    comparacaoBha = []
    
    for i in range(0, tamList-1):
        comparacaoCorrelacao.append(1/(cv.compareHist(listaHist[0], listaHist[i+1], 0)) + 0.00001)
        print('Método Correlação: imagem 1 x imagem ',i+2, ": {:.6f}".format(comparacaoCorrelacao[i]))
        
    
    print("\n")
    
    for i in range(0, tamList-1):
        comparacaoChi.append(cv.compareHist(listaHist[0], listaHist[i+1], 1))
        print('Método Chi-Square: imagem 1 x imagem ',i+2, ": {:.6f}".format(comparacaoChi[i]))    
    
    print("\n")
    
    for i in range(0, tamList-1):
        comparacaoBha.append(cv.compareHist(listaHist[0], listaHist[i+1], 3))
        print('Método Bhattacharrya: imagem 1 x imagem ',i+2, ": {:.6f}".format(comparacaoBha[i]))
        
    print("\n")
    
    #calculando as distancias
    calcFinal = []
    
    tamComp = len(comparacaoBha)
    
    for i in range(0, tamComp):
        calcFinal.append(math.sqrt(comparacaoCorrelacao[i]**2 + comparacaoChi[i]**2 + comparacaoBha[i]**2))
        print("Distancia img 1 x img ",i+2,"",calcFinal[i])
        
    print("\n")
    print("Menor distância: ", min(calcFinal), " da comparação entre img 1 e img ", calcFinal.index(min(calcFinal))+2)
    print("\n")
    
    #exibindo hist das imagens
    color = ('b', 'g', 'r')
    
    for j in range (1, tamList+1):
        for i, col in enumerate(color):
            histr = cv.calcHist([listaImg[j-1]], [i], None, [256], [0,256])
            plt.subplot(3,2,j),plt.plot(histr, color = col)
            plt.title(j), plt.xticks([]), plt.yticks([])
            plt.xlim([0, 256]) 
    plt.show()       
        
def main():
    #criando vetor arquivo com nome de todas imgs da pasta
    for _, _, arquivo in os.walk('img/'):
        pass
    
    #preenchendo vetor de imagens e convertendo-as
    listaImg = []
    tamArq = len(arquivo)
    
    for i in range(0,tamArq):
        listaImg.append(cv.imread("img/"+arquivo[i]))
        listaImg[i] = cv.cvtColor(listaImg[i], cv.COLOR_BGR2HSV)
        
    buscaImg(listaImg)      
        
main()      
        
        
        