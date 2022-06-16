# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Modifizierter Gauss-Algorithmus
from gauss_mod import *

''' Lösung zu Aufgabe 2 vom Hausaufgabenblatt '''

def exakte_loesung(x):
	'''
	Die exakte Lösung des gegebenen Problems
	'''
	return 1.0/12*x**4-1.0/12*x

def fehler(u_exakt, u_approx):
	'''
	Simples Fehlermaß
	'''
	N = len(u_exakt)
	return 1.0/(N)*np.sum([np.abs(u_exakt[i]-u_approx[i]) for i in range(N)])

def visualisieren(x_fein, x_approx, u_exakt, u_approx):
	'''
	Exakte und approximierte Lösung darstellen
	'''
	plt.plot(x_fein, u_exakt, color='blue', label = 'Exakte Loesung')
	plt.plot(x_approx, u_approx, color='red', label = 'Diskrete Loesung')
	plt.legend(loc='upper left')
	plt.show()

def matrix_vektor(N):
	'''
	Gibt Systemmatrix und rechte Seite des Systems zurück
	'''
	# Matrix
	A = np.diag(np.ones(N-1),-1)+np.diag(-2*np.ones(N))+np.diag(np.ones(N-1),1)
	A *= (N+1)**2
	# rechte Seite
	b = np.array([(float(i)/(N+1))**2 for i in range(1,N+1)])

	return (A,b)

def diskrete_loesung(N):
	'''
	Gibt diskrete Lösung für gegebenes N zurück
	'''
	# Systemdaten erhalten
	(A,b) = matrix_vektor(N)
	# Wende modifizierten Gauss Algorithmus an
	u = gauss_algorithmus(A,b)

	# Erweitere Lösung
	loesung = np.zeros(N+2)
	loesung[1:N+1] = u

	return loesung

print(" N |  Fehler  ")      
for n in [4,8,16,32,64]:

	# 2 verschiedene Skalen
	x_approx = np.array([float(i)/(n+1) for i in range(n+2)])
	x_fein = np.linspace(0,1,1000)

	# Berechne Vektor der exakten Werte
	u_exakt_grob = np.array(exakte_loesung(x_approx))
	u_exakt_fein = np.array(exakte_loesung(x_fein))

	# Berechne diskrete Lösung
	u_approx = diskrete_loesung(n)
	
	# Berechne Fehler
	error = fehler(u_exakt_grob, u_approx)
	
	# Visualisiere
	visualisieren(x_fein, x_approx, u_exakt_fein, u_approx)

	# Ausgabe
	print("{0:2d} | {1:<6.5f}".format(n, error))

# Bewertung
print("Desto mehr Stützstellen, desto bessere Annäherung!")
