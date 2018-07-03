#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Las dos líneas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from pulp import * # Carga Pulp 
from calculo import *
from tkinter import messagebox
from grafico import *




def ecuacion(): # X = X1  Y = X2
#Tenemos que convertir todos los datos a INT para poder trabajar
#los campos son leidos en forma de stringvar
	
	#Coeficientes Funcion Obejtivo
	
	R1A1 = int
	R1B1 = int
	R1C1 = int
	R2A2 = int
	R2B2 = int
	R2C2 = int
	R3A3 = int
	R3B3 = int
	R3C3 = int
	R1S = int
	R2S = int
	R3S = int
	

	if (OPT == 'MAX'):
		Optimo = LpMaximize
	else:
		Optimo = LpMinimize

	FOX1 = int(OX1.get()) 
	FOX2 = int(OX2.get())

	#Coeficientes Restriccion 1
	R1A1 = int(R1X1.get())
	R1B1 = int(R1X2.get())
	R1C1 = int(R1C.get())
	if (R1Signo.get() == '>='):
		R1S = 1
	else:
		R1S = -1

	#Coeficientes Restriccion 2
	R2A2 = int(R2X1.get())
	R2B2 = int(R2X2.get())
	R2C2 = int(R2C.get())
	if (R2Signo.get() =='>='):
		R2S = 1
	else:
		R2S = -1

	#Coeficientes Restriccion 2
	R3A3 = int(R3X1.get())
	R3B3 = int(R3X2.get())
	R3C3 = int(R3C.get())
	if (R3Signo.get() =='>='):
		R3S = 1
	else:
		R3S = -1
	
	#estos son los capturas en input
	FunObj = [FOX1,FOX2]
	Rest = [[R1A1,R1B1,R1C1,R1S],[R2A2,R2B2,R2C2,R2S], [R3A3,R3B3,R3C3,R3S]]
	
	#estos son los valores constantes
	#coeficienteObjetivo = [3,2]
	#restricciones = [[2,1,18,-1],[2,3,42,-1],[3,1,24,-1]]	
	
	#problema = resolver(coeficienteObjetivo,restricciones,LpMaximize)
	problema = resolver(FunObj,Rest,LpMaximize)
	
	
	
	
	
	
	
	#imprimimos por consola los valores de la funcion objetivo y de las variables
	'''
	print("objective=", problema[0])
	print("x1=", problema[1])
	print("x2=", problema[2])
	
	for v in problema.variables():
		valores.append([(v.name),(v.varValue)])
		print([v.name,v.varValue])
	'''
	
	
	# acá está ventana
	
	root = Tk()
	frame = Frame(root)
	frame.pack()
	bottomframe = Frame(root)
	bottomframe.pack( side = BOTTOM )
			#mostramos el resultado	
	Label(root, text = "El tipo resultado es = " + str(problema[3])).pack()
	Label(root, text = "El Z optimo es = " + str(problema[0])).pack()
	Label(root, text = "x1" + "= " + str(problema[1])).pack()
	Label(root, text = "x1" + "= " + str(problema[2])).pack()
	graficar(Rest, problema)



	


 
  
 


# Define la ventana principal de la aplicación

raiz = Tk()
raiz.geometry('300x300') # anchura x altura
raiz.configure(bg = 'beige')
raiz.title('Programacion Lineal')


#FuncionObjetivo
R1Signo = StringVar()
R2Signo = StringVar()
R3Signo = StringVar()
OPT = StringVar()
OX1 = StringVar()
OX2 = StringVar()
R1X1 = StringVar()
R1X2 = StringVar()
R2X1 = StringVar()
R2X2 = StringVar()
R3X1 = StringVar()
R3X2 = StringVar()
R1C = StringVar()
R2C = StringVar()
R3C = StringVar()

#Funcion Objetivo
funcionObjetivo = Frame(raiz, width = '400', height = '100', bg ='beige' )
funcionObjetivo.pack(side = TOP)
Label(funcionObjetivo, text ="Funcion Objetivo", pady = '5', bg ='beige', font=('12')).pack(side = TOP)
Label(funcionObjetivo, text = " Z =  ").pack(side = LEFT)
Entry(funcionObjetivo, width = '5', textvariable = OX1).pack(side = LEFT)
Label(funcionObjetivo, text = " X1 ").pack(side = LEFT)
Entry(funcionObjetivo, width = '5', textvariable = OX2).pack(side = LEFT)
Label(funcionObjetivo, text = " X2 ").pack(side = LEFT)
combo = ttk.Combobox(funcionObjetivo, values = ('MAX','MIN'), width = '5',textvariable = OPT).pack(side = LEFT)

#Restriccion1
restriccion1 = Frame(raiz, width = '400', height = '100', bg ='beige' )
restriccion1.pack(side = TOP)
Label(restriccion1, text ="Restriccion 1", pady = '5', bg ='beige', font=('12')).pack(side = TOP)
Entry(restriccion1, width = '5',textvariable = R1X1).pack(side = LEFT)
Label(restriccion1, text = " X1 ").pack(side = LEFT)
Entry(restriccion1, width = '5',textvariable = R1X2).pack(side = LEFT)
Label(restriccion1, text = " X2 ").pack(side = LEFT)
ttk.Combobox(restriccion1, values = ('>=','<='), width = '5',textvariable = R1Signo).pack(side = LEFT)
Entry(restriccion1, width = '5', textvariable = R1C).pack(side = LEFT)

#Restriccion2
restriccion2 = Frame(raiz, width = '400', height = '100', bg ='beige' )
restriccion2.pack(side = TOP)
Label(restriccion2, text ="Restriccion 2", pady = '5', bg ='beige', font=('12')).pack(side = TOP)
Entry(restriccion2, width = '5',textvariable = R2X1).pack(side = LEFT)
Label(restriccion2, text = " X1 ").pack(side = LEFT)
Entry(restriccion2, width = '5',textvariable = R2X2).pack(side = LEFT)
Label(restriccion2, text = " X2 ").pack(side = LEFT)
ttk.Combobox(restriccion2, values = ('>=','<='), width = '5', textvariable = R2Signo).pack(side = LEFT)
Entry(restriccion2, width = '5', textvariable = R2C).pack(side = LEFT)

#Restriccion3
restriccion2 = Frame(raiz, width = '400', height = '100', bg ='beige' )
restriccion2.pack(side = TOP)
Label(restriccion2, text ="Restriccion 3", pady = '5', bg ='beige', font=('12')).pack(side = TOP)
Entry(restriccion2, width = '5',textvariable = R3X1).pack(side = LEFT)
Label(restriccion2, text = " X1 ").pack(side = LEFT)
Entry(restriccion2, width = '5',textvariable = R3X2).pack(side = LEFT)
Label(restriccion2, text = " X2 ").pack(side = LEFT)
ttk.Combobox(restriccion2, values = ('>=','<='), width = '5', textvariable = R3Signo).pack(side = LEFT)
Entry(restriccion2, width = '5', textvariable = R3C).pack(side = LEFT)

ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
ttk.Button(raiz, text='Optimizacion', command= ecuacion).pack(side = BOTTOM)


# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de 
# que alguna persona interactúe con ella.

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.

raiz.mainloop()
