#/usr/bin/python
#coding: utf-8

import random
import Serpiente
import Tablero

class Granobasico():
	
	def __init__(self,nivel):
		posicion=[random.randint(1,18),random.randint(1,18)]
		self.pos=posicion
		self.nivel=nivel
		
	def comergrano(self,s):
		i=self.nivel
		g=self.pos
		c=s.pos
		if c[len(c)-1]==g:
			if i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7:
				s.pos.append(g)
				return True
			elif i==8 or i==9 or i==10 or i==11 or i==12 or i==13 or i==14:
				s.pos.append(g)
				s.pos.append(g)
				return True
			elif i==15 or i==16 or i==17 or i==18 or i==19 or i==20:
				s.pos.append(g)
				s.pos.append(g)
				s.pos.append(g)
				return True
		else:
			return False 
			

if __name__ == "__main__":
	c=Granobasico(1)
	s=Serpiente.Serpiente()
	score=0
	print c.comergrano(s)
	print score
