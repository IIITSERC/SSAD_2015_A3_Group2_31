#!/usr/bin/python
from __future__ import print_function
import random
import time
import os
import copy
import sys
class Person(object):
	def __init__(self,name,x,y):
		self.name=name
		self.x=x
		self.y=y
class Player(Person):
	def __init__(self,name,x,y):

		super(Player,self).__init__(name,x,y)
		self.score=0
		self.life=3
	def update(self,x,y):
		self.x=x
		self.y=y
	def __go_lefts(self,a,fireballlist,listcoin):
		get=getposition(player)
		if a[get[0]+1][get[1]-1]==' ':
			player.x=player.x+4
		elif a[get[0]][get[1]-1]==' ' or a[get[0]][get[1]-1]=='H' or a[get[0]][get[1]-1]=='O':
			player.y=player.y-1
		elif a[get[0]][get[1]-1]=='C':
			player.update(player.x,player.y-1)
			Collectcoin(get[0],get[1],listcoin)
		checkcollision(a,fireballlist,listcoin)


	def __go_rights(self,a,fireballlist,listcoin):
		get=getposition(player)
		if a[get[0]+1][get[1]+1]==' ':
			player.x=player.x+4
		elif a[get[0]][get[1]+1]==' ' or a[get[0]][get[1]+1]=='H' or a[get[0]][get[1]+1]=='O':
			player.y=player.y+1
		elif a[get[0]][get[1]+1]=='C':
			player.update(player.x,player.y+1)
			Collectcoin(get[0],get[1],listcoin)
		checkcollision(a,fireballlist,listcoin)
	#coins on stairs?
	def __go_ups(self,a,fireballlist,listcoin):
		get=getposition(player)
		# print(a[get[0]-1][get[1]])
		# test = raw_input()
		if a[get[0]-1][get[1]]==' ' and a[get[0]][get[1]-1]!='X':return
		if a[get[0]-1][get[1]] == ' ' and a[get[0]-1][get[1]+1] == 'X' or a[get[0]-1][get[1]]=='H' and a[get[0]-1][get[1]-1]=='X' or a[get[0]-1][get[1]]=='H' and a[get[0]-1][get[1]+1]=='X' or a[get[0]-1][get[1]]=='H' and a[get[0]-2][get[1]]=='H' and a[get[0]-3][get[1]]=='H' or a[get[0]+1][get[1]]=='H' and a[get[0]+2][get[1]]=='H' and a[get[0]+3][get[1]]=='H' or a[get[0]-1][get[1]]=='H' and a[get[0]-2][get[1]]=='H' and a[get[0]+1][get[1]]=='H' or a[get[0]+1][get[1]]=='H' and a[get[0]+2][get[1]]=='H' and a[get[0]-1][get[1]]=='H':
			player.update(player.x-1,player.y)
		checkcollision(a,fireballlist,listcoin)
	def __go_downs(self,a,fireballlist,listcoin):
		get=getposition(player)
		if a[get[0]+1][get[1]]=='X':return
		if a[get[0]-1][get[1]]=='H' and a[get[0]-2][get[1]]=='H' and a[get[0]-3][get[1]]=='H' or a[get[0]+1][get[1]]=='H' and a[get[0]+2][get[1]]=='H' and a[get[0]+3][get[1]]=='H' or a[get[0]-1][get[1]]=='H' and a[get[0]-2][get[1]]=='H' and a[get[0]+1][get[1]]=='H' or a[get[0]+1][get[1]]=='H' and a[get[0]+2][get[1]]=='H' and a[get[0]-1][get[1]]=='H':
			player.update(player.x+1,player.y)
		checkcollision(a,fireballlist,listcoin)
	#what if collide with wall or go into wall
	def __jump_rights(self,a,fireballlist,listcoin):
		os.system('printf "\033c"')
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]+1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		player.update(get[0]-1,get[1]+1)
		Collectcoin(get[0],get[1],listcoin)
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]+1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		time.sleep(0.1)
		os.system('printf "\033c"')
	
		get=getposition(player)
		player.update(get[0]-1,get[1]+1)
		Collectcoin(get[0],get[1],listcoin)
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]+1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		time.sleep(0.1)
		os.system('printf "\033c"')
	
		get=getposition(player)
		player.update(get[0]+1,get[1]+1)
		Collectcoin(get[0],get[1],listcoin)
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]+1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		time.sleep(0.1)
		os.system('printf "\033c"')
		
		get=getposition(player)
		player.update(get[0]+1,get[1]+1)
		Collectcoin(get[0],get[1],listcoin)
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]+1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		checkcollision(a,fireballlist,listcoin)
		time.sleep(0.1)
		os.system('printf "\033c"')
	
	def __jump_lefts(self,a,fireballlist,listcoin):
		os.system('printf "\033c"')
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]-1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		player.update(get[0]-1,get[1]-1)
		Collectcoin(get[0],get[1],listcoin)
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]-1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		time.sleep(0.1)
		os.system('printf "\033c"')
		get=getposition(player)
		player.update(get[0]-1,get[1]-1)
		Collectcoin(get[0],get[1],listcoin)
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]-1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		time.sleep(0.1)
		os.system('printf "\033c"')
		get=getposition(player)
		player.update(get[0]+1,get[1]-1)
		Collectcoin(get[0],get[1],listcoin)
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]-1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		time.sleep(0.1)
		os.system('printf "\033c"')
		get=getposition(player)
		player.update(get[0]+1,get[1]-1)
		Collectcoin(get[0],get[1],listcoin)
		get=getposition(player)
		checkwalll=checkwall(a,get[0],get[1]-1)
		jj=0
		while checkwalll==1 and (player.x%4)!=0:
			player.x=player.x+1
		if checkwalll==1:
			return
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		checkcollision(a,fireballlist,listcoin)
		time.sleep(0.1)
	def go_left(self,a,fireballlist,listcoin):
		player.__go_lefts(a,fireballlist,listcoin)
	def go_right(self,a,fireballlist,listcoin):
		player.__go_rights(a,fireballlist,listcoin)
	def go_up(self,a,fireballlist,listcoin):
		player.__go_ups(a,fireballlist,listcoin)
	def go_down(self,a,fireballlist,listcoin):
		player.__go_downs(a,fireballlist,listcoin)
	def jump_left(self,a,fireballlist,listcoin):
		player.__jump_lefts(a,fireballlist,listcoin)
	def jump_right(self,a,fireballlist,listcoin):
		player.__jump_rights(a,fireballlist,listcoin)
			
	
class Donkey(Person):
	def __init__(self,name, x, y):
		self.x = x
		self.y = y
		self.name = name
	def move(self,a):
		i=random.randrange(0,2,2)
		if(self.y<=15 and i==0):
			self.y=self.y+1
		else:
			self.y=self.y-1

class Queen(Person):
	pass

class coins:
	def __init__(self,name,x,y):
		self.x=x
		self.name=name
		self.y=y
class fireball():
        def __init__(self,name,x,y):
			self.x=x
			self.y=y
			self.name='O'
	                self.floor=1

donkey=Donkey('D',4,4)
queen=Queen('Q',2,18)
player=Player('P',24,6)
def board(a,listcoin,fireballlist):
	for i in range(2,26):
		if (i-1)%4==1 or (i-1)%4==2 or (i-1)%4==3:
			for j in range(2,80):
				a[i][j]=' '

	for i in range(1,26):
		if i==5:
			for j in range(61,80):
				a[i][j]=' '
		if i==9:
	  		for j in range(2,10):
				a[i][j]=' '
		if i==13:
	   		for j in range(65,80):
				a[i][j]=' '
		if i==17:
	 		for j in range(2,15):
				a[i][j]=' '
		if i==21:
	     		for j in range(60,80):
				a[i][j]=' '
	a[2][15]='X'
	a[2][25]='X'
	for j in range(15,24):a[3][j]='X'
	a[3][24]='H'
	a[3][25]='X'
	a[3][26]='X'
	a[4][24]='H'
	a[5][17]='H'
	a[6][17]='H'
	a[8][17]='H'
	a[5][40]='H'
	a[6][40]='H'
	a[7][40]='H'
	a[8][40]='H'
	a[9][27]='H'
	a[10][27]='H'
	a[11][27]='H'
	a[12][27]='H'
	a[13][43]='H'
	a[14][43]='H'
	a[16][43]='H'
	a[13][60]='H'
	a[14][60]='H'
	a[15][60]='H'
	a[16][60]='H'
	a[17][34]='H'
	a[18][34]='H'
	a[19][34]='H'
	a[20][34]='H'
	a[17][47]='H'
	a[18][47]='H'
	a[20][47]='H'
	a[21][55]='H'
	a[22][55]='H'
	a[23][55]='H'
	a[24][55]='H'
	for i in listcoin:
		a[i.y][i.x]=i.name
	for i in fireballlist:
		a[i.x][i.y]=i.name
	a[queen.x][queen.y]=queen.name
	a[player.x][player.y]=player.name
	a[donkey.x][donkey.y]=donkey.name
def makecoins(a,listcoin):
		listcoin[:]=[]
		for j in range(0,4):
			i=4
			while i<26:
				if i/4==1:
					b=random.randrange(2,60,2)
				if i/4==2:
					b=random.randrange(10,80,2)
				
				if i/4==3:
					b=random.randrange(2,64,2)
				
				if i/4==4:
					b=random.randrange(15,80,2)
				if i/4==5:
					b=random.randrange(2,59,2)
				if i/4==6:
					b=random.randrange(2,80,2)
				if a[i][b]==' ':
					coin=coins('C',b,i)
					listcoin.append(coin)
					i=i+4
def makefireball(a,fireballlist):
        #position of donkey is 4,4
        ball=fireball('O',donkey.x,donkey.y+2)
        fireballlist.append(ball)

def movefireball(a,fireballlist):
                # test = raw_input()
                for i in fireballlist:
	                b=random.randrange(1,4)
			if a[i.x+1][i.y]=='X' and i.floor==1:
				i.y=i.y+1
	                elif a[i.x+1][i.y]=='H' and i.floor==1:
	                        if b==1:
	                                i.x=i.x+4
	                        	i.floor=i.floor+1
	                        else:
	                                i.y=i.y+1
	                elif a[i.x+1][i.y]==' ' and i.floor==1:
	                        i.x=i.x+4
	                        i.floor=i.floor+1
	                elif i.floor==2 or i.floor==4:
	
	                        #how to apply loop
	                        b=random.randrange(1,4)
				if a[i.x+1][i.y]=='X':
					i.y=i.y-1
	                        elif a[i.x+1][i.y]=='H':
	                                if b==1:
	                                        i.x=i.x+4
	                                        i.floor=i.floor+1
	                        elif a[i.x+1][i.y]==' ':
	                                i.x=i.x+4
	                                i.floor=i.floor+1
	
	                elif i.floor==3 or i.floor==5:
	                        #how to apply loop
	                        b=random.randrange(1,4)
				if a[i.x+1][i.y]=='X':
					i.y=i.y+1
	                        elif a[i.x+1][i.y]=='H':
	                                if b==1:
	                                        i.x=i.x+4
	                        		i.floor=i.floor+1
	                        elif a[i.x][i.y-1]==' ':
	                                i.x=i.x+4
	                        	i.floor=i.floor+1
			elif i.floor==6:
				if(i.y==2):
					fireballlist.remove(i)
				else:
					i.y=i.y-1
def print_final(a,listcoin):
	for i in range(1,26):
			for j in range(1,81):
				print (a[i][j],end='')
			print ('\n',end='')
	print("LIFE:",player.life,"SCORE:",player.score)

def getposition(player):
	list=[player.x,player.y]
	return list
	os.system('printf "\033c"')


def Collectcoin(x,y,listcoin):
	for i in listcoin:
		print("1")
		if player.x==i.y and player.y==i.x:
			player.update(player.x,player.y)
			listcoin.remove(i)
			player.score=player.score+5
	
		
def checkcollision(a,fireballlist,listcoin):
	for i in fireballlist:
        	if i.x==player.x and i.y==player.y:
			print("1")
			fireballlist[:]=[]
        	        player.score=player.score-25
        	        player.life=player.life-1
			player.x=24
			player.y=6
			donkey.x=4
			donkey.y=4
			makecoins(a,listcoin)
			break
                #restart the egame
def checkwall(a,row,column):
        flag=0
        #chec k x and y of palyer
        if a[row][column]=='X':
		return 1
	else:
		return 0

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch
def lose(a,listcoin,fireballlist,win):
	if win==0:
		lose=input("Play Again?(y/n)") 
		if lose=="n":
			sys.exit()
		player.score=0
	if win==1:
		player.score=player.score+50
	player.life=3
	player.x=24
	player.y=6
	donkey.x=4
	donkey.y=4
	board(a,listcoin,fireballlist)
	makecoins(a,listcoin)
	fireballlist[:]=[]
def main():
	a=[['X' for i in range(0,81)] for j in range(0,26)]
	listcoin=[]
	fireballlist = []
	board(a,listcoin,fireballlist)
	makecoins(a,listcoin)
	# test = raw_input()
	mandar=1
	while 1:
		a=[['X' for i in range(0,81)] for j in range(0,26)]
		board(a,listcoin,fireballlist)
		#os.system('printf "\033c"')
		if mandar%5==0:
			donkey.move(a)
			#makefireball(a,fireballlist)
		movefireball(a,fireballlist)
		# movefireball(a,fireballlist)
		board(a,listcoin,fireballlist)
		print_final(a,listcoin)
		ch = getchar()
		if ch=='a':
			player.go_left(a,fireballlist,listcoin)
		elif ch=='w':
			player.go_up(a,fireballlist,listcoin)
		elif ch=='d':
			player.go_right(a,fireballlist,listcoin)
		elif ch=='s':
			player.go_down(a,fireballlist,listcoin)
		elif ch==' ':
			if player.x==4 and (15<=player.y and player.y<=29):
				pass
			elif player.x==24 or player.x==16 or player.x==8:
				player.jump_right(a,fireballlist,listcoin)
			else:player.jump_left(a,fireballlist,listcoin)
		elif player.life==0:
			lose(a,listcoin,fireballlist,0)
		elif ch=='q':
			break
		if player.x==queen.x:
			lose(a,listcoin,fireballlist,1)
		mandar=mandar+1

main()
