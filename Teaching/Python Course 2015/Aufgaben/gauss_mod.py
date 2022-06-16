#! /usr/bin/env python
# -*- coding: utf-8 -*-


'''Lösung zu Aufgabe 1 vom Hausaufgabenblatt'''


import numpy as np


def pivoting(A, j):
    '''Suchen des Pivot-Element einer bestimmten Spalte einer Matrix
    
    Argumente
    ---------
    A : numpy.ndarray
        Matrix für das Pivoting
    j : int
        Spalte, in der das Pivot-Element gesucht wird

    Rückgabewert
        Tupel gestehend aus dem Index und dem Wert des Pivotelements
    
    Erklärung
        Das Pivot-Element ist das betragsmäßig größte Element in der j-ten
        Spalte der Matrix auf oder unterhalb der Diagonalen.
    '''

    # speichere die zu untersuchende Spalte
    col = A[j:, j]

    # bestimme Index und Element mit numpy-Methoden
    pivotIndex = np.abs(col).argmax() + j
    pivotElement = np.abs(col).max()

    return (pivotIndex, pivotElement)


def zeilen_tauschen(A, i, j):
    '''Vertauschen zweier Zeilen einer gegebenen Matrix
    
    Argumente
    ---------
    A : numpy.ndarray
        Matrix für das Vertauschen von Zeilen
    i : int
        ein Zeilenindex der Matrix
    j : int
        ein weiterer Zeilenindex der Matrix
    
    Rückgabewert
        Matrix A', aus A durch Vertauschen der Zeilen i und j hervorgehend
    '''

    if i == j:
        # es muss nicht vertauscht werden
        return A
    else:
        # arbeite mit einer Kopie von A
        A = A.copy()

        # führe die Vertauschung durch
        iRow = A[i,:].copy()
        A[i,:], A[j,:] = A[j,:], iRow

        return A


def gauss_algorithmus(A, b):
    '''Durchführen des Gauß-Algorithmus' für gegebene Matrix und rechte Seite
    
    Argumente
    ---------
    A : numpy.ndarray
        Matrix des Gleichungssystems
    b : numpy.ndarray
        rechte Seite des Gleichungssystems
    
    Rückgabewert
        Lösung x des Gleichungssystems Ax = b

    Exceptions
        TypeError
            bei falschen Argumenten
        ValueError
            bei nicht invertierbarer Matrix
    '''

    ##
    # Überprüfung der Argumente
    ##

    # teste, ob die Typen richtig sind
    if type(A) != np.ndarray or type(b) != np.ndarray:
        raise TypeError('A und b müssen numpy arrays sein')    

    # teste, ob die Dimensionen richtig sind
    if len(A.shape) != 2:
        raise TypeError('A muss eine Matrix sein')
    if len(b.shape) != 1:
        raise TypeError('b muss ein Vektor sein')

    # teste, ob die Dimensionen passend gewählt sind
    if A.shape[0] != A.shape[1]:
        raise TypeError('A muss eine quadratische Matrix sein')
    if A.shape[0] != b.shape[0]:
        raise TypeError('A und b müssen die gleich Anzahl an Zeilen haben')

    ##
    # Initialisierung
    ## 
    
    n = A.shape[0]

    # arbeite mit der erweiterten Matrix C = [A|b]
    C = np.hstack((A, b.reshape(n,1)))

    ##
    # Algorithmus Teil 1:
    # Bringe die erweiterte Matrix [A|b] auf Dreiecksform
    ##

    for i in range(n-1):
        # finde das Pivot-Element
        (pivotIndex, pivotElement) = pivoting(C, i)
        if pivotElement == 0:
            raise ValueError('Die Matrix ist nicht invertierbar')

        # tausche ggf. Zeilen
        if pivotIndex != i:
            C = zeilen_tauschen(C, i, pivotIndex)

        # verarbeite verbleibende Zeilen
        for j in range(i+1, i+2):
            if C[j,i] == 0:
                continue
            r = C[j,i] / pivotElement
            C[j] = C[j] + r * C[i]

    ##
    # Algorithmus Teil 2: 
    # Berechne die Lösung
    ##

    # lege Lösungsvektor an
    x = np.zeros(n)

    # bestimme Lösungsvektor
    for i in range(n-1, -1, -1):
        x[i] = C[i,n]
	if i != n-1:
        	for j in range(i+1, i+2):
            		x[i] = x[i] - C[i,j] * x[j]
        x[i] = x[i] / C[i,i]

    return x

