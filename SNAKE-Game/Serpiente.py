#/usr/bin/python
#coding: utf-8

import Obstaculo

class Serpiente():
	
	coord=[[0,0],[0,1],[0,2],[0,3],[0,4]]
	def __init__(self,posicion=coord,poder=False,direccion=6, perder=False,ganar=False):
		self.pos=posicion#lista de coordenadas de las casillas que usa la serpiente
		self.pod=poder
		self.di=direccion
		self.perder= perder
		self.ganar=ganar
		
	def cambiardireccion(self,num):#cambiar en el tablero
		self.di=num
		
	def cpos(self):#cambiar posición
		p=self.pos
		d=self.di
		if d==6:
			c=[]
			for i in range(len(p)-1):
				c.append(p[i+1])
			t=[p[len(p)-1][0],p[len(p)-1][1]+1]
			c.append(t)
			self.pos=c
			if self.pos[len(self.pos)-1][1]==20:
				self.pos[len(self.pos)-1][1]=0
		elif d==2:
			c=[]
			for i in range(len(p)-1):
				c.append(p[i+1])
			t=[p[len(p)-1][0]+1,p[len(p)-1][1]]
			c.append(t)
			self.pos=c
			if self.pos[len(self.pos)-1][0]==20:
				self.pos[len(self.pos)-1][0]=0
		elif d==8:
			c=[]
			for i in range(len(p)-1):
				c.append(p[i+1])
			t=[p[len(p)-1][0]-1,p[len(p)-1][1]]
			c.append(t)
			self.pos=c
			if self.pos[len(self.pos)-1][0]==-1:
				self.pos[len(self.pos)-1][0]=19
		elif d==4:
			c=[]
			for i in range(len(p)-1):
				c.append(p[i+1])
			t=[p[len(p)-1][0],p[len(p)-1][1]-1]
			c.append(t)
			self.pos=c
			if self.pos[len(self.pos)-1][1]==-1:
				self.pos[len(self.pos)-1][1]=19
		else:
			pass
			
	def perpod(self,num):
		if num<30:
			self.pod=True
		else:
			self.pod=False
	
	def chocarm(self):#chocar con él mismo
		p=self.pos
		for i in range(len(p)-1):
			if p[i]==p[len(p)-1]:
				return True
				break
		else:
			return False
	
	def chocarpared(self,l):#chocar con una pared
		s=self.pos[len(self.pos)-1]
		for i in l:
			if s==i:
				return True
		else:
			return False
		
	def perdedor(self):
		self.perder= not self.perder
		
	def ganador(self):
		self.ganar=True
	
			


if __name__ == "__main__":
	x=Serpiente()
	#print x.chocarm()
	#print x.chocar()
	#x.aumentar([8,3])
	x.pos=[0,0]
	print x.pos
	l=[[1,2],[0,0],[0,4]]
	#print x.di
	#print x.pod
	#print x.pos
	#print x.chocarpared(l)
	print x.ganar
	x.ganador()
	print x.ganar
	x=Serpiente()
	print x.pos
	#l=[5,4]
	#l=l*3
	#print l
	

