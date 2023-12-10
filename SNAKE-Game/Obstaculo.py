#/usr/bin/python
#coding: utf-8

import random
class Obstaculo():
	def __init__(self,nivel):
		self.n=nivel
		
	def paredes(self):
		if self.n==6:######################################### Plano cartesiano NIVEL 6
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
			
			
			return lista
		elif self.n==2:###################################### Easy NIVEL 2                                                  
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
		elif self.n==3: ##################################### Alineado NIVEL 3
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
		elif self.n==18: ####################################### Nube de puntos NIVEL 18
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
		elif self.n==20:######################### FINAL STAGE NIVEL 20
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
			p=[16,3]
			for i in range(3):
				l.append(p)
				p=[p[0]+1,p[1]-1]
			return l
		elif self.n==5:################################## Esbastica nazi #NIVEL 5
			l=[]
			p=[2,2]
			for i in range(9):
				l.append(p)
				p=[2,p[1]+1]
			p=[3,2]
			for i in range(9):
				l.append(p)
				p=[3,p[1]+1]
			p=[9,2]
			for i in range(16):
				l.append(p)
				p=[9,p[1]+1]
			p=[10,2]
			for i in range(16):
				l.append(p)
				p=[10,p[1]+1]
			p=[16,9]
			for i in range(9):
				l.append(p)
				p=[16,p[1]+1]
			p=[17,9]
			for i in range(9):
				l.append(p)
				p=[17,p[1]+1]
			p=[11,2]
			for i in range(7):
				l.append(p)
				p=[p[0]+1,2]
			p=[11,3]
			for i in range(7):
				l.append(p)
				p=[p[0]+1,3]
			p=[2,16]
			for i in range(7):
				l.append(p)
				p=[p[0]+1,16]
			p=[2,17]
			for i in range(7):
				l.append(p)
				p=[p[0]+1,17]
			p=[4,9]
			for i in range(5):
				l.append(p)
				p=[p[0]+1,9]
			p=[4,10]
			for i in range(5):
				l.append(p)
				p=[p[0]+1,10]
			p=[11,9]
			for i in range(5):
				l.append(p)
				p=[p[0]+1,9]
			p=[11,10]
			for i in range(5):
				l.append(p)
				p=[p[0]+1,10]
			return l
		elif self.n==4:################################ Encerrado!!!! NIVEL 4
			l=[]
			p=[19,0]
			for i in range(19):
				l.append(p)
				p=[19,p[1]+1]
			p=[1,0]
			for i in range(18):
				l.append(p)
				p=[p[0]+1,0]
			p=[1,19]
			for i in range(19):
				l.append(p)
				p=[p[0]+1,19]
			return l
		elif self.n==15:##################### Crazy lines #NIVEL 15
			l=[]
			p=[1,1]		
			for i in range(5):
				for j in range(9):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[1,p[1]+2]
			p=[11,11]		
			for i in range(5):
				for j in range(8):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[11,p[1]+2]
			p=[1,11]		
			for i in range(5):
				for j in range(8):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[p[0]+2,11]
			p=[11,1]		
			for i in range(5):
				for j in range(9):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[p[0]+2,1]
			return l
		elif self.n==19:###########################  ¿Final stage? NIVEL 19 
			l=[]
			p=[1,1]
			for i in range(18):
				l.append(p)
				p=[p[0]+1,p[1]+1]
			p=[1,18]
			for i in range(18):
				l.append(p)
				p=[p[0]+1,p[1]-1]
			p=[1,5]			
			for i in range(2):
				for j in range(10):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[18,5]
			p=[2,9]			
			for i in range(2):
				for j in range(5):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[2,10]
			p=[13,9]			
			for i in range(2):
				for j in range(5):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[13,10]
			p=[8,2]
			for i in range(2):
				for j in range(4):
					l.append(p)
					p=[8,p[1]+1]
				p=[8,14]
			p=[11,2]
			for i in range(2):
				for j in range(4):
					l.append(p)
					p=[11,p[1]+1]
				p=[11,14]
			return l
		elif self.n==12:################################### Lucky!!! NIVEL 12
			l=[]
			p=[1,12]
			for i in range(2):
				for j in range(12):
					l.append(p)
					p=[p[0]+1,p[1]-1]
				p=[7,18]
			p=[1,9]
			for i in range(2):
				for j in range(9):
					l.append(p)
					p=[p[0]+1,p[1]-1]
				p=[10,18]
			p=[1,6]
			for i in range(2):
				for j in range(6):
					l.append(p)
					p=[p[0]+1,p[1]-1]
				p=[13,18]
			p=[1,3]
			for i in range(2):
				for j in range(3):
					l.append(p)
					p=[p[0]+1,p[1]-1]
				p=[16,18]
			p=[13,1]
			for i in range(6):
				l.append(p)
				p=[p[0]+1,1]
			p=[1,18]
			for i in range(6):
				l.append(p)
				p=[p[0]+1,18]
			return l
		elif self.n==10:###################################### Escaleras NIVEL 10
			l=[]
			p=[1,1]
			for i in range(8):
				for j in range(4):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[p[0]+2,p[1]-2]
			p=[5,1]
			for i in range(6):
				for j in range(4):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-2,p[1]+2]
			p=[1,13]
			for i in range(3):
				for j in range(6):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-4,p[1]+2]
			p=[13,0]
			for i in range(3):
				for j in range(3):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[p[0]+2,p[1]-1]
			return l
		elif self.n==8:###################################### Lluvia de paredes NIVEL 8
			l=[]
			p=[1,1]
			for i in range(3):
				for j in range(2):
					for k in range(4):
						l.append(p)
						p=[p[0]+1,p[1]]
					p=[p[0]-2,p[1]+3]
				p=[p[0]-3,p[1]]
			p=[7,2]
			for i in range(3):
				for j in range(2):
					for k in range(4):
						l.append(p)
						p=[p[0]+1,p[1]]
					p=[p[0]-2,p[1]+3]
				p=[p[0]-3,p[1]]
			p=[12,1]
			for i in range(3):
				for j in range(2):
					for k in range(4):
						l.append(p)
						p=[p[0]+1,p[1]]
					p=[p[0]-2,p[1]+3]
				p=[p[0]-3,p[1]]
			return l	
		elif self.n==9:####################################### Cuadricula NIVEL 9
			l=[[1,2],[1,9],[1,16],[4,3],[4,10],[4,17],[8,2],[8,9],[8,16],[11,3],[11,10],[11,17],[15,2],[15,9],[15,16],[18,3],[18,10],[18,17]]
			n=0
			for k in range(3):
				p=[1,1+n]
				for i in range(2):
					for j in range(4):
						l.append(p)
						p=[p[0]+1,p[1]]
					p=[p[0]-4,p[1]+3]
				n=n+7
			n=0
			for k in range(3):
				p=[8,1+n]
				for i in range(2):
					for j in range(4):
						l.append(p)
						p=[p[0]+1,p[1]]
					p=[p[0]-4,p[1]+3]
				n=n+7
			n=0
			for k in range(3):
				p=[15,1+n]
				for i in range(2):
					for j in range(4):
						l.append(p)
						p=[p[0]+1,p[1]]
					p=[p[0]-4,p[1]+3]
				n=n+7
			return l
		elif self.n==14:################################# Doble U NIVEL 14
			l=[]
			p=[2,0]
			for i in range(2):
				for j in range(15):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[p[0]+6,p[1]-15]
			p=[11,5]
			for i in range(2):
				for j in range(15):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[p[0]+6,p[1]-15]
			p=[3,14]
			for i in range(5):
				l.append(p)
				p=[p[0]+1,p[1]]
			p=[12,5]
			for i in range(5):
				l.append(p)
				p=[p[0]+1,p[1]]
			for i in range(6):
				l.append([4,random.randint(1,8)])
			for i in range(6):
				l.append([6,random.randint(1,8)])
			for i in range(6):
				l.append([13,random.randint(7,15)])
			for i in range(6):
				l.append([15,random.randint(7,15)])
			return l
		elif self.n==1:################################## Start NIVEL 1
			l=[]
			p=[9,0]
			for i in range(20):
				l.append(p)
				p=[9,p[1]+1]
			p=[10,0]
			for i in range(20):
				l.append(p)
				p=[10,p[1]+1]
			return l
		elif self.n==7:################################# Paredes verticales NIVEL 7
			l=[]
			p=[1,1]
			for i in range(2):
				for j in range(18):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-18,p[1]+17]
			p=[4,4]
			for i in range(2):
				for j in range(12):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-12,p[1]+11]
			p=[7,7]
			for i in range(2):
				for j in range(6):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-6,p[1]+5]
			return l
		elif self.n==16:################################## Rosca de reyes NIVEL 16
			l=[]
			p=[1,1]
			for i in range(2):
				for j in range(18):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-18,p[1]+17]
			p=[4,4]
			for i in range(2):
				for j in range(12):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-12,p[1]+11]
			p=[7,7]
			for i in range(2):
				for j in range(6):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-6,p[1]+5]
			p=[1,2]
			for i in range(14):
				l.append(p)
				p=[1,p[1]+1]
			p=[18,2]
			for i in range(16):
				l.append(p)
				p=[18,p[1]+1]
			p=[4,7]
			for i in range(8):
				l.append(p)
				p=[4,p[1]+1]
			p=[15,5]
			for i in range(10):
				l.append(p)
				p=[15,p[1]+1]
			p=[7,8]
			for i in range(4):
				l.append(p)
				p=[7,p[1]+1]
			p=[12,8]
			for i in range(2):
				l.append(p)
				p=[12,p[1]+1]
			return l
		elif self.n==13:################################### Laberinto simetrico NIVEL 13
			l=[]
			p=[1,1]
			for i in range(3):
				for j in range(3):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-3,p[1]+4]
			p=[16,10]
			for i in range(3):
				for j in range(3):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-3,p[1]+4]
			p=[6,2]
			for i in range(2):
				for j in range(11):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[3,17]
			p=[8,5]
			for i in range(2):
				for j in range(11):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[1,14]
			p=[1,11]
			for i in range(2):
				for j in range(4):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[15,8]
			p=[5,2]
			for i in range(2):
				for j in range(10):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[14,8]
			p=[8,5]
			for i in range(2):
				for j in range(7):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[11,8]
			p=[18,1]
			for i in range(2):
				for j in range(4):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[1,15]
			return l
		elif self.n==17:############################### plus plus NIVEL 17
			l=[]
			p=[[2,1],[2,7],[2,13],[4,4],[4,10],[4,16],[6,1],[6,7],[6,13],[8,4],[8,10],[8,16],[10,1],[10,7],[10,13],[12,4],[12,10],[12,16],[14,1],[14,7],[14,13],[16,4],[16,10],[16,16],[18,1],[18,7],[18,13]]
			a=[]
			r=[10]
			for i in range(25):
				k=random.randint(0,26)
				for j in r:
					if r!=k:
						v=p[k]
						a.append(v)
			for i in range(len(a)):
				v=a[i]
				
				l.append([a[i][0]-1,a[i][1]+1])
				l.append([a[i][0]+1,a[i][1]+1])
				for j in range(3):
					l.append(a[i])
					a[i]=[a[i][0],a[i][1]+1]
			return l
		elif self.n==11:######################################## Abstraccion NIVEL 11
			l=[]
			p=[2,2]
			for i in range(2):
				for j in range(16):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[18,2]
			p=[4,4]
			for i in range(2):
				for j in range(12):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[16,4]
			p=[7,8]
			for i in range(3):
				for j in range(4):
					l.append(p)
					p=[p[0],p[1]+1]
				p=[p[0]+3,8]
			p=[6,3]
			for i in range(2):
				for j in range(9):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-9,p[1]+3]
			p=[6,13]
			for i in range(2):
				for j in range(9):
					l.append(p)
					p=[p[0]+1,p[1]]
				p=[p[0]-9,p[1]+3]
			
			return l
			
					
				
					
		
	
		
				
			
		
			
			
			
		
			
				
			
			
			
				
			
			
			
			
			
			
			
			
			
if __name__ == "__main__":
	#y=obstaculo(5)
	#print [5,3]==None
	y=Obstaculo(1)
	print y.paredes()
