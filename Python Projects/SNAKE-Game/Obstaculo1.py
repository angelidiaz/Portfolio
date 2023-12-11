#/usr/bin/python
#coding: utf-8

import random
class Obstaculo():
	def __init__(self,nivel):
		self.n=nivel
		
	def paredes(self):
		if self.n==3:
			p1=[9,0]
			p2=[10,0]
			p3=[0,9]
			p4=[0,10]
			lista=[p1,p2,p3,p4]
			for i in range(19):
				p1=[9,p1[1]+1]
				p2=[10,p2[1]+1]
				p3=[p3[0]+1,9]
				p4=[p4[0]+1,10]
				lista.append(p1)
				lista.append(p2)
				lista.append(p3)
				lista.append(p4)
			return lista
		elif self.n==1:                                                      
			p1=[random.randint(2,7),random.randint(1,3)]
			p2=[random.randint(2,4),5]
			p4=[random.randint(12,15),5]
			p5=[random.randint(3,8),random.randint(17,19)]
			piv=[p1,p5]
			pih=[p2,p4]
			lista=[]
			for i in piv:
				for j in range(10):
					lista.append([i[0]+j,i[1]])
			for i in pih:
				for j in range(10):
					lista.append([i[0],i[1]+j])
			return lista
		elif self.n==2:
			p1=[random.randint(2,3),3]
			p2=[random.randint(3,5),4]
			p3=[random.randint(9,11),6]
			p4=[random.randint(15,17),5]
			p5=[random.randint(5,6),17]
			piv=[p1,p5]
			pih=[p2,p4]
			lista=[]
			for i in piv:
				for j in range(13):
					lista.append([i[0]+j,i[1]])
			for i in pih:
				for j in range(12):
					lista.append([i[0],i[1]+j])
			for j in range(9):
				lista.append([p3[0],p3[1]+j])
			return lista
		elif self.n==4:
			l=[]
			l1=[]
			p1=[0,0]
			while True:
				p=[2,random.randint(1,18)]
				if p1!=p:
					l.append(p)
					l1.append(p)
					p1=p
					if len(l1)==10:
						break
			l2=[]
			p2=[0,0]
			while True:
				p=[4,random.randint(1,18)]
				if p2!=p:
					l.append(p)
					l2.append(p)
					p2=p
					if len(l2)==10:
						break
			l3=[]
			p3=[0,0]
			while True:
				p=[6,random.randint(1,18)]
				if p3!=p:
					l.append(p)
					l3.append(p)
					p3=p
					if len(l3)==10:
						break
			l4=[]
			p4=[0,0]
			while True:
				p=[8,random.randint(1,18)]
				if p4!=p:
					l.append(p)
					l4.append(p)
					p4=p
					if len(l4)==10:
						break
			l5=[]
			p5=[0,0]
			while True:
				p=[10,random.randint(1,18)]
				if p5!=p:
					l.append(p)
					l5.append(p)
					p5=p
					if len(l5)==10:
						break
			l6=[]
			p6=[0,0]
			while True:
				p=[12,random.randint(1,18)]
				if p6!=p:
					l.append(p)
					l6.append(p)
					p6=p
					if len(l6)==10:
						break
			l7=[]
			p7=[0,0]
			while True:
				p=[14,random.randint(1,18)]
				if p7!=p:
					l.append(p)
					l7.append(p)
					p7=p
					if len(l7)==10:
						break
			l8=[]
			p8=[0,0]
			while True:
				p=[16,random.randint(1,18)]
				if p8!=p:
					l.append(p)
					l8.append(p)
					p8=p
					if len(l8)==10:
						break
			l9=[]
			p9=[0,0]
			while True:
				p=[18,random.randint(1,18)]
				if p9!=p:
					l.append(p)
					l9.append(p)
					p9=p
					if len(l9)==10:
						break
			return l
		elif self.n==5:
			l=[[8,9],[8,10],[9,11],[10,8],[11,9],[11,10]]
			p=[2,5]
			for i in range(4):
				l.append(p)
				p=[p[0]+1,p[1]-1]
			p=[2,8]
			for i in range(7):
				l.append(p)
				p=[p[0]+1,p[1]-1]
			p=[6,8]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]-1]	
			p=[11,13]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]-1]
			p=[11,17]
			for i in range(7):
				l.append(p)
				p=[p[0]+1,p[1]-1]
			p=[14,17]
			for i in range(4):
				l.append(p)
				p=[p[0]+1,p[1]-1]	
			#segunda diagonal
			p=[2,14]
			for i in range(4):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			p=[2,11]
			for i in range(7):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			p=[6,11]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			p=[11,6]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			p=[11,2]
			for i in range(7):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			p=[14,2]
			for i in range(4):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			#diagonales cruzadas
			p=[1,1]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			p=[16,16]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			p=[1,18]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]-1]
			p=[16,4]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]-1]
			return l
			
			
			
			
			
			
if __name__ == "__main__":
	#y=obstaculo(5)
	#print [5,3]==None
	x=True
	for i in range(10):
		if i<5:
			x=False
			print x
		else:
			x=True
			print x
