#/usr/bin/python
#coding: utf-8

import Tablero
import random
import Serpiente

class Cereza():
	
	def __init__(self):
		posicion=[random.randint(1,18),random.randint(1,18)]
		self.pos=posicion
	
	def comercereza(self,s):
		c=s.pos
		g=self.pos
		if c[len(c)-1]==g:
			return True
		else:
			return False
	

#if __name__ == "__main__":

