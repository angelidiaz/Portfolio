#/usr/bin/python
#coding: utf-8

import threading
import Serpiente
import time
import Granobasico
import Cereza
import Obstaculo
import Raton
from Tkinter import *
from random import *
import Image, ImageTk
from tkMessageBox import *


alto=ancho=20
tiempo=0.2
numgra=5
imagenes=["estrellas.jpg","luigi.png","mario.jpg","marioa.jpg","mariop.jpg","peach.jpg"]
colores=["#509564","#62D533"]
n=["1-Start","2-Easy","3-Alineado","4-Locked!!!!"," 5-Esbástica nazi","6-Cartesian Plane","7-Paredes verticales","8-Lluvia de paredes","9-Cuadricula","10-Ladders","11-Abstraction","12-Lucky!!!","13-Laberinto simétrico","14-Double U","15-Crazy lines","16-Rosca de reyes","17-plus plus","18-Nube de puntos","19-¿Final stage?","20-FINAL STAGE"]

class Tablero(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.serp=Serpiente.Serpiente()
		f=20
		c=20
		t=list()
		for i in range(f):
			t.append([False]*c)
		self.tab=t
		self.nivel=1
		self.score=0
		self.corriendo = False
		self.pausa=False

		
	def ctabtk(self):#crea una lista con los puntos de los cuadritos
		tabtk=[]
		for i in range(20):
			coordenadas=[]
			for j in range(20):
				coordenadas.append([j*ancho,i*alto,(j*ancho)+ancho,(i*alto)+alto])
			tabtk.append(coordenadas)
		return tabtk
		
	def poser(self):#posición serpiente
		p=self.serp
		po=p.pos
		t=self.ctabtk()
		ta=self.tab
		posertk=[]
		for i in range(len(po)):
			ta[po[i][0]][po[i][1]]=True
			posertk.append(t[po[i][0]][po[i][1]])
		return posertk
		
	def cppos(self,ppos):#posicición de la cola
		t1=ppos
		ta=self.tab
		ta[t1[0]][t1[1]]=False
				
	def actposer(self,pospas,g,c):#actualizar posicion de la serpiente
		posnue=self.poser()#la nueva posicion de la serpiente a ser actualizada en la ventana
		if self.serp.pod==False:
			if c%2==0:
				for i in range(len(posnue)):
					tablerof.coords(pospas[i],posnue[i][0],posnue[i][1],posnue[i][2],posnue[i][3])
					if i%2==0:
						tablerof.itemconfig(pospas[i], fill=colores[0])
					else:
						tablerof.itemconfig(pospas[i], fill=colores[1])
			else:
				for i in range(len(posnue)):
					tablerof.coords(pospas[i],posnue[i][0],posnue[i][1],posnue[i][2],posnue[i][3])
					if i%2==0:
						tablerof.itemconfig(pospas[i], fill=colores[1])
					else:
						tablerof.itemconfig(pospas[i], fill=colores[0])
		else:
			cp=["#FFFF00","#FFA500","#FCE005","#FCC505"]
			for i in range(len(posnue)):
				tablerof.coords(pospas[i],posnue[i][0],posnue[i][1],posnue[i][2],posnue[i][3])
				if i%2==0:
					tablerof.itemconfig(pospas[i], fill=cp[randint(0,(len(cp)-1))])
				else:
					tablerof.itemconfig(pospas[i], fill=cp[randint(0,(len(cp)-1))])
		tablerof.itemconfig(g, fill=colores[randint(0,(len(colores)-1))])
			
	def posgb(self):#grano básico
		i=self.nivel
		t=self.tab
		ta=self.ctabtk()
		while True:
			g=Granobasico.Granobasico(i)
			pos=g.pos
			if t[pos[0]][pos[1]]==False:
				t[pos[0]][pos[1]]=True
				cuagra=ta[pos[0]][pos[1]]
				break
		return [g,cuagra]
			
	def poscer(self):#cereza
		t=self.tab
		ta=self.ctabtk()
		while True:
			c=Cereza.Cereza()
			pos=c.pos
			if t[pos[0]][pos[1]]==False:
				t[pos[0]][pos[1]]=True
				cuacer=ta[pos[0]][pos[1]]
				break
		return [c,cuacer]
				
	def posra(self):#ratón
		t=self.tab
		ta=self.ctabtk()
		while True:
			r=Raton.Raton()
			pos=r.pos
			if t[pos[0]][pos[1]]==False:
				t[pos[0]][pos[1]]=True
				cuara=ta[pos[0]][pos[1]]
				break
		return [r,cuara]
		
	def cpared(self):#paredes
		i=self.nivel
		t=self.tab
		l=Obstaculo.Obstaculo(i)
		self.obs=l.paredes()
		cuapa=[]
		ta=self.ctabtk()
		for i in self.obs:
			t[i[0]][i[1]]=True
			cuapa.append(ta[i[0]][i[1]])
		return [self.obs,cuapa]
		
	def cambpared(self,l):
		t=self.tab
		for i in l:
			t[i[0]][i[1]]=True
	
	def aucuaserp(self,cuadritos):#aumenta cuadrados serpiente
		i=self.nivel
		if i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7:
			cuadritos.append(tablerof.create_oval(0, 0, 0 ,0 , fill=colores[randint(0,(len(colores)-1))]))
		elif i==8 or i==9 or i==10 or i==11 or i==12 or i==13 or i==14:
			for i in range(2):
				cuadritos.append(tablerof.create_oval(0, 0, 0 ,0 , fill=colores[randint(0,(len(colores)-1))]))
		else:
			for i in range(3):
				cuadritos.append(tablerof.create_oval(0, 0, 0 ,0 , fill=colores[randint(0,(len(colores)-1))]))
	
	def cambnivel(self):
		i=self.nivel
		self.nivel=i+1
				
	def cambtab(self):#cambiar tablero
		self.cambnivel()
		bortab=[]#limpiar tablero
		f=20
		c=20
		for i in range(f):
			bortab.append([False]*c)
		self.tab=bortab
		self.serp.pos=[[0,0],[0,1],[0,2],[0,3],[0,4]]
		self.serp.di=6
		self.serp.pod=False
	
	def limptab(self,elementos):#"borra" los elementos de la ventana Tk
		s=elementos[0]
		p=elementos[1]
		g=elementos[2]
		c=elementos[3]
		r=elementos[4]
		for i in s:
			tablerof.coords(i,0,0,0,0)
		for i in p:
			tablerof.coords(i,alto*20,ancho*20)
		tablerof.coords(g,0,0,0,0)
		tablerof.coords(c,alto*20,ancho*20)
		tablerof.coords(r,alto*20,ancho*20)
		
	def perdedor(self):
		self.serp.perdedor()
		self.corriendo=False
		time.sleep(0.6)
		tablerof.fondo = ImageTk.PhotoImage(Image.open("perdedor.jpg"))
		tablerof.create_image(0,0,image=tablerof.fondo,anchor=NW)
		time.sleep(1)
		casillas.destroy()

		
			
	def camcor(self,elem,lista):
		tablerof.coords(elem,lista[0], lista[1])
	
	def run(self):
		self.corriendo = True
		j=0
		niv=n[self.nivel-1]
		sc=self.score
		sc=str(sc)
		nu=j
		nu=str(nu)
		texto.set(""+niv+"\nSCORE:"+sc+"  POWER:"+"0"+"\n                POINTS:"+nu+"               ")
		eltabtk=[]#elementos de tablero:serpiente,paredes,grano,cereza,raton
		s=self.serp
		x=s.pos[0]
		coordserp=self.poser()
		cuadserp=[]#cuadritos de la serpiente
		eltabtk.append(cuadserp)
		pared=self.cpared()
		p=pared[0]
		coordpared=pared[1]
		cuadpared=[]#cuadritos de las paredes
		eltabtk.append(cuadpared)
		grano=self.posgb()
		g=grano[0]
		coordgra=grano[1]#coordenadas grano basico
		cereza=self.poscer()
		c=cereza[0]
		coordcer=cereza[1]
		for i in range(len(coordserp)):
			if i%2==0:
				cuadserp.append(tablerof.create_oval(coordserp[i][0], coordserp[i][1],coordserp[i][2] ,coordserp[i][3] , fill=colores[0]))
			else:
				cuadserp.append(tablerof.create_oval(coordserp[i][0], coordserp[i][1],coordserp[i][2] ,coordserp[i][3] , fill=colores[1]))
		tablerof.muro= ImageTk.PhotoImage(Image.open("muro.png"))
		for i in coordpared:
			cuadpared.append(tablerof.create_image(i[0],i[1],image=tablerof.muro,anchor=NW))
		tablerof.cereza= ImageTk.PhotoImage(Image.open("cerezass.png"))
		tablerof.raton= ImageTk.PhotoImage(Image.open("mm1.png"))
		cuadgra=tablerof.create_oval(coordgra[0], coordgra[1],coordgra[2] ,coordgra[3] , fill=colores[randint(0,(len(colores)-1))])#cuadritos grano
		cuadracer=tablerof.create_image(coordcer[0], coordcer[1],image=tablerof.cereza,anchor=NW)#cuadritos cereza
		cuadraton=tablerof.create_image(alto*20,ancho*20,image=tablerof.raton,anchor=NW)#cuadritos raton
		eltabtk.append(cuadgra)
		eltabtk.append(cuadracer)
		eltabtk.append(cuadraton)
		cont=0
		num=30
		k=30
		cont1=0
		time.sleep(tiempo)
		while self.corriendo:
			if self.pausa==False:
				if num>29:
					texto.set(""+niv+"\nSCORE:"+sc+"  POWER:"+"0"+"\n                POINTS:"+nu+"               ")
				else:
					mn=29-num
					mn=str(mn)
					texto.set(niv+"\nSCORE:"+sc+"  POWER:"+mn+"\n                POINTS:"+nu+"               ")
				if j<numgra:
					self.cambpared(p)
					s.perpod(num)
					if s.pod==True:
						self.cppos(x)
						self.serp.cpos()
						cog=g.comergrano(s)
						coc=c.comercereza(s)
						if cog==False:
							if coc==False:
								if s.chocarm()==False:
									pass
								else:
									j=numgra
									self.perdedor()
							else:
								self.score+=150
								cont+=150
								x=self.serp.pos[0]
								cereza=self.poscer()
								c=cereza[0]
								coordcer=cereza[1]
								self.camcor(cuadracer,coordcer)
						else:
							j+=1
							cont+=20
							x=self.serp.pos[0]
							self.score+=20
							self.aucuaserp(cuadserp)
							grano=self.posgb()
							g=grano[0]
							coordgra=grano[1]
							if j!=numgra:
								tablerof.coords(cuadgra,coordgra[0], coordgra[1],coordgra[2] ,coordgra[3])
					else:
						self.cppos(x)
						self.serp.cpos()
						cog=g.comergrano(s)
						coc=c.comercereza(s)
						if cont>1000:
							cont=0
							k=0
							raton=self.posra()
							r=raton[0]
							coordrat=raton[1]
							tablerof.coords(cuadraton,coordrat[0], coordrat[1])
							if cog==False:
								if coc==False:
									if s.chocarm()==False:
										if s.chocarpared(p)==False:
											pass
										else:
											j=numgra
											self.perdedor()
									else:
										j=numgra
										self.perdedor()
								else:
									self.score+=150
									cont+=150
									x=self.serp.pos[0]
									cereza=self.poscer()
									c=cereza[0]
									coordcer=cereza[1]
									self.camcor(cuadracer,coordcer)
							else:
								j+=1
								cont+=20
								x=self.serp.pos[0]
								self.score+=20
								self.aucuaserp(cuadserp)
								grano=self.posgb()
								g=grano[0]
								coordgra=grano[1]
								if j!=numgra:
									tablerof.coords(cuadgra,coordgra[0], coordgra[1],coordgra[2] ,coordgra[3])
						else:
							if k<29:
								if cog==False:
									if coc==False:
										if r.comeraton(s)==False:
											if s.chocarm()==False:
												if s.chocarpared(p)==False:
													pass
												else:
													j=numgra
													self.perdedor()
											else:
												j=numgra
												self.perdedor()
										else:
											self.score+=50
											cont+=50
											x=self.serp.pos[0]
											num=0
											k=30
											r=None
											tablerof.coords(cuadraton,alto*20,ancho*20)
									else:
										self.score+=150
										cont+=150
										x=self.serp.pos[0]
										cereza=self.poscer()
										c=cereza[0]
										coordcer=cereza[1]
										self.camcor(cuadracer,coordcer)
								else:
									j+=1
									cont+=20
									x=self.serp.pos[0]
									self.score+=20
									self.aucuaserp(cuadserp)
									grano=self.posgb()
									g=grano[0]
									coordgra=grano[1]
									if j!=numgra:
										tablerof.coords(cuadgra,coordgra[0], coordgra[1],coordgra[2] ,coordgra[3])
							elif k==29:
								self.cppos(r.pos)
								r=None
								tablerof.coords(cuadraton, alto*20,ancho*20)
								if cog==False:
									if coc==False:
										if s.chocarm()==False:
											if s.chocarpared(p)==False:
												pass
											else:
												j=numgra
												self.perdedor()
										else:
											j=numgra
											self.perdedor()
									else:
										self.score+=150
										cont+=150
										x=self.serp.pos[0]
										cereza=self.poscer()
										c=cereza[0]
										coordcer=cereza[1]
										self.camcor(cuadracer,coordcer)
								else:
									j+=1
									cont+=20
									x=self.serp.pos[0]
									self.score+=20
									self.aucuaserp(cuadserp)
									grano=self.posgb()
									g=grano[0]
									coordgra=grano[1]
									if j!=numgra:
										tablerof.coords(cuadgra,coordgra[0], coordgra[1],coordgra[2] ,coordgra[3])
							else:
								if cog==False:
									if coc==False:
										if s.chocarm()==False:
											if s.chocarpared(p)==False:
												pass
											else:
												j=numgra
												self.perdedor()
										else:
											j=numgra
											self.perdedor()
									else:
										self.score+=150
										cont+=150
										x=self.serp.pos[0]
										cereza=self.poscer()
										c=cereza[0]
										coordcer=cereza[1]
										self.camcor(cuadracer,coordcer)
								else:
									j+=1
									cont+=20
									x=self.serp.pos[0]
									self.score+=20
									self.aucuaserp(cuadserp)
									grano=self.posgb()
									g=grano[0]
									coordgra=grano[1]
									if j!=numgra:
										tablerof.coords(cuadgra,coordgra[0], coordgra[1],coordgra[2] ,coordgra[3])
				else:	
					self.serp.ganador()
					time.sleep(0.5)
					tablerof.fondo = ImageTk.PhotoImage(Image.open("game.PNG"))
					tablerof.create_image(0,0,image=tablerof.fondo,anchor=NW)
					time.sleep(1)
					casillas.destroy()
					break
				if not self.serp.perder:
					cont+=1
					num+=1
					k+=1
					cont1+=1
					self.actposer(cuadserp,cuadgra,cont1)
					x=self.serp.pos[0]
					time.sleep(tiempo/(((0.7*j)+10.0)/10.0))
			else:
				time.sleep(0.2)
			
def teclaArriba(e):
	if s.di!=2:
		s.di = 8
		
def teclaAbajo(e):
	if s.di!=8:
		s.di = 2
		
def teclaIzquierda(e):
	if s.di!=6:
		s.di = 4
		
def teclaDerecha(e):
	if s.di!=4:
		s.di = 6
	
def salir():
	if x.corriendo==True:
		x.corriendo=False
		x.join()
		casillas.destroy()
	else:
		casillas.destroy()

def pausa(e):
	if x.corriendo==True:
		if not x.serp.perder:
			if not x.serp.ganar:
				if x.pausa==True:
					tablerof.pausa = ImageTk.PhotoImage(Image.open("pausa.jpg"))
					tablerof.create_image(400,400,image=tablerof.pausa,anchor=NW)
					x.pausa=False
				else:
					tablerof.pausa = ImageTk.PhotoImage(Image.open("pausa.jpg"))
					tablerof.create_image(100,100,image=tablerof.pausa,anchor=NW)
					x.pausa=True

def nivel1():
	if x.corriendo==False:
		x.nivel=1
		x.start()
def nivel2():
	if x.corriendo==False:
		x.nivel=2
		x.start()
def nivel3():
	if x.corriendo==False:
		x.nivel=3
		x.start()
def nivel4():
	if x.corriendo==False:
		x.nivel=4
		x.start()
def nivel5():
	if x.corriendo==False:
		x.nivel=5
		x.start()
def nivel6():
	if x.corriendo==False:
		x.nivel=6
		x.start()
def nivel7():
	if x.corriendo==False:
		x.nivel=7
		x.start()
def nivel8():
	if x.corriendo==False:
		x.nivel=8
		x.start()
def nivel9():
	if x.corriendo==False:
		x.nivel=9
		x.start()
def nivel10():
	if x.corriendo==False:
		x.nivel=10
		x.start()
def nivel11():
	if x.corriendo==False:
		x.nivel=11
		x.start()
def nivel12():
	if x.corriendo==False:
		x.nivel=12
		x.start()
def nivel13():
	if x.corriendo==False:
		x.nivel=13
		x.start()
def nivel14():
	if x.corriendo==False:
		x.nivel=14
		x.start()
def nivel15():
	if x.corriendo==False:
		x.nivel=15
		x.start()
def nivel16():
	if x.corriendo==False:
		x.nivel=16
		x.start()
def nivel17():
	if x.corriendo==False:
		x.nivel=17
		x.start()
def nivel18():
	if x.corriendo==False:
		x.nivel=18
		x.start()
def nivel19():
	if x.corriendo==False:
		x.nivel=19
		x.start()
def nivel20():
	if x.corriendo==False:
		x.nivel=20
		x.start()

def ins():
	if x.pausa==True:
		x.pausa=False
		tablerof.ins = ImageTk.PhotoImage(Image.open("instrucciones.jpg"))
		tablerof.create_image(400,400,image=tablerof.ins,anchor=NW)
	else:
		x.pausa=True
		tablerof.ins = ImageTk.PhotoImage(Image.open("instrucciones.jpg"))
		tablerof.create_image(0,0,image=tablerof.ins,anchor=NW)
		

if __name__ == "__main__":
	
	casillas=Tk()
	casillas.title("SNAKE")
	x=Tablero()
	niv=x.nivel
	niv=str(niv)
	texto = StringVar()
	texto.set(""+"\n             WELCOME!!!             "+"\nChoose a level")
	t = Label(casillas, textvariable=texto,fg="#344145",bg="#ABD5F2", font=("Liberation Mono", 20))
	t.pack()
	tablerof = Canvas(casillas, width=ancho*20, height=alto*20)
	tablerof.config(bg="black")
	tablerof.pack()
	tablerof.fondo = ImageTk.PhotoImage(Image.open(imagenes[randint(0,(len(imagenes)-1))]))
	tablerof.create_image(0,0,image=tablerof.fondo,anchor=NW)
	s=x.serp
	casillas.bind("<Up>", teclaArriba)
	casillas.bind("<Down>", teclaAbajo)
	casillas.bind("<Left>", teclaIzquierda)
	casillas.bind("<Right>", teclaDerecha)
	casillas.protocol("WM_DELETE_WINDOW", salir)
	casillas.bind("<Return>",pausa)
	f = Frame(casillas)
	f.pack()
	b1 = Button(f, text="LEVEL 1",bg='red',command=nivel1)
	b2 = Button(f, text="LEVEL 2",bg='blue',command=nivel2)
	b3 = Button(f, text="LEVEL 3",bg='green',command=nivel3)
	b4 = Button(f, text="LEVEL 4",bg='yellow',command=nivel4)
	b5 = Button(f, text="LEVEL 5",bg='red',command=nivel5)
	b6 = Button(f, text="LEVEL 6",bg='blue',command=nivel6)
	b7 = Button(f, text="LEVEL 7",bg='green',command=nivel7)
	b8 = Button(f, text="LEVEL 8",bg='yellow',command=nivel8)
	b9 = Button(f, text="LEVEL 9",bg='red',command=nivel9)
	b10 = Button(f, text="LEVEL 10",bg='blue',command=nivel10)
	b11= Button(f, text="LEVEL 11",bg='green',command=nivel11)
	b12 = Button(f, text="LEVEL 12",bg='yellow',command=nivel12)
	b13 = Button(f, text="LEVEL 13",bg='red',command=nivel13)
	b14 = Button(f, text="LEVEL 14",bg='blue',command=nivel14)
	b15 = Button(f, text="LEVEL 15",bg='green',command=nivel15)
	b16 = Button(f, text="LEVEL 16",bg='yellow',command=nivel16)
	b17 = Button(f, text="LEVEL 17",bg='red',command=nivel17)
	b18 = Button(f, text="LEVEL 18",bg='blue',command=nivel18)
	b19 = Button(f, text="LEVEL 19",bg='green',command=nivel19)
	b20 = Button(f, text="LEVEL 20",bg='yellow',command=nivel20)
	b21 = Button(f, text="INSTR",bg='red',command=ins)
	b1.grid(row=1,column=1)
	b2.grid(row=1,column=2)
	b3.grid(row=1,column=3)
	b4.grid(row=1,column=4)
	b5.grid(row=1,column=5)
	b6.grid(row=1,column=6)
	b7.grid(row=1,column=7)
	b8.grid(row=2,column=1)
	b9.grid(row=2,column=2)
	b10.grid(row=2,column=3)
	b11.grid(row=2,column=4)
	b12.grid(row=2,column=5)
	b13.grid(row=2,column=6)
	b14.grid(row=2,column=7)
	b15.grid(row=3,column=1)
	b16.grid(row=3,column=2)
	b17.grid(row=3,column=3)
	b18.grid(row=3,column=4)
	b19.grid(row=3,column=5)
	b20.grid(row=3,column=6)
	b21.grid(row=3,column=7)
	mainloop()
	raw_input("the end")
