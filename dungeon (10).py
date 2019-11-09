start=10
loc=start
loc2=10
end=20
clear=1000
enemy=[8,11,16,4,19,1]
nenemy=6
enemyhealth=[5,5,5,5,10,10]
health=100
key=False
portcullis=True
mushroom=True
fungus=True
down=True
end2=0
enemy2=[4,14,7,21,1,100]
enemyhealth2=[5,5,5,10,10,5]
ended=False
from PIL import Image
yousprite=Image.open(you.jpg)
from PIL import Image
goblinsprite=Image.open(goblin.jpg)
from PIL import Image
greatgoblinsprite=Image.open(greatgoblin.jpg)
from PIL import Image
endgoblinsprite=Image.open(endgoblin.jpg)
from PIL import Image
chefgoblinsprite=Image.open(chefgoblin.jpg)
from PIL import Image
background=Image.open(background.jpg)
print("")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("You grew up in an underground mine.  Not long after you come of age, goblins attack your underground village, killing everyone you ever knew.")
print("You are captured alive but manage to escape and take the sword from one of your captors.  You find yourself in the centre of the goblins' dungeon and must try to escape.")
print("")
print("Controls:")
print("d: move right                           | ")
print("a: move left                    O=======|=======================================>")
print("e: attack right                         |") 
print("q: attack left")
print("")
print("____________________________________________________________________________________________________________________________________________________________________________")
print("")
while ended==False:
	if down==True:
		attf=False
		attb=False
		print("----------------------------------------------------")
		print("Your health is:")
		print(health)
		print("Your location is:")
		print(1,loc)
		next=input("<=======|==o What do you do now? o==|=======>")	
		if next!="a" and next!="d" and next!="q" and next!="e":
			print("Wrong button.")
		block=False
		if next=="d":
			for i in enemy:
				if loc+1==i:
					print("An enemy is there!")
					blockr=True
		elif next=="a":	
			for i in enemy:
				if loc-1==i:
					print("An enemy is there!")
					blockl=True
		elif next=="e":
			attf=True
		elif next=="q":
			attb=True
		if attf==True:
			for i in enemy:
				if loc+1==i:
					for j in [0,1,2,3,4,5]:
						if enemy[j]==i:
							enemyhealth[j]=enemyhealth[j]-1
							print("You deal 1 Damage.")
			for i in [0,1,2,3,4,5]:	
				if enemyhealth[i]==0 and loc==enemy[i]-1:
					enemy[i]=clear
					print("Enemy killed!")
		elif attb==True:
			for i in enemy:
				if loc-1==i:
					for j in [0,1,2,3,4,5]:
						if enemy[j]==i:
							enemyhealth[j]=enemyhealth[j]-1
							print("You deal 1 Damage.")
			for i in [0,1,2,3,4,5]:
				if enemyhealth[i]==0 and loc==enemy[i]+1:
					enemy[i]=clear
					print("Enemy killed!")
		if next=="d" and blockr==False and loc!=20:
			loc=loc+1
		elif next=="a" and blockl==False and loc!=0:
			loc=loc-1
		if loc==18 and enemyhealth[4]==10:
			print("A great goblin stands before you!")
		if loc==2 and enemyhealth[5]==10:
			print("A great goblin stands before you!")
		for i in enemy:
			if loc+1==i:
				if loc-1!=1 and loc+1!=19:
					health=health-1
					print("You are attacked!")
					print("You suffer 1 damage")
				else:
					health=health-2
					print("You are attacked!")
					print("You suffer 2 damage")
			if loc-1==i:
				if loc-1!=1 and loc+1!=19:
					health=health-1
					print("You are attacked!")
					print("You suffer 1 damage")
				else:
					health=health-2
					print("You are attacked!")
					print("You suffer 2 damage")
		if health==0:
			print("You succumb to your injuries and die having never seen the light of day.")
			break
		if loc==0 and key==False:
			print("The tunnel before you has collapsed.  You see something glinting among the fallen rocks...")
			action=input("What do you do now?")
			if action==3:
				print("After pushing the rocks aside you find a rusting metal key.")
				key=True
		if loc==0 and key==True:
			print("The tunnel has collapsed; you will not be able to continue down this path.")
		if loc==end:	
			down=False
			print("You clamber up a ladder to another level of the dungeon.  Torches line the cave and you see that there are two ways you can go: left or right.")
		while ended==False and down==False:
			attf=False
			attb=False
			print("----------------------------------------------------")
			print("Your health is:")
			print(health)
			print("Your location is:")
			print(2,loc2)
			if loc2==21 and enemyhealth2[5]==0:
				print("Having defeated the goblin, you retreat out of the dining hall and back into the cave.")
				loc=19
			next=input("<=======|==o What do you do now? o==|=======>")
			if next!="a" and next!="d" and next!="q" and next!="e":
				print("Wrong button.")
			blockr=False
			blockl=False
			if loc2==1 and portcullis==False and next==1:
				ended=True
			if next=="d":
				for i in enemy:
					if loc2+1==i:
						print("An enemy is there!")
						blockr=True
			elif next=="a":	
				for i in enemy:
					if loc2-1==i:
						print("An enemy is there!")
						blockl=True
			elif next=="e":
				attf=True
			elif next=="q":
				attb=True
			if attf==True:
				for i in enemy2:
					if loc2+1==i:
						for j in [0,1,2,3,4,5]:
							if enemy2[j]==i:
								enemyhealth2[j]=enemyhealth2[j]-1
								print("You deal 1 Damage.")
				for i in [0,1,2,3,4,5]:	
					if enemyhealth2[i]==0 and loc2==enemy2[i]-1:
						enemy2[i]=clear
						print("Enemy killed!")
			elif attb==True:
				for i in enemy2:
					if loc2-1==i:
						for j in [0,1,2,3,4,5]:
							if enemy2[j]==i:
								enemyhealth2[j]=enemyhealth2[j]-1
								print("You deal 1 Damage.")
				for i in [0,1,2,3,4,5]:
					if enemyhealth2[i]==0 and loc2==enemy2[i]+1:
						enemy2[i]=clear
						print("Enemy killed!")
			if next=="d" and blockr==False and loc2+1!=21 and loc2!=21:
				loc2=loc2+1
			elif next=="a" and blockl==False and loc2!=1:
				loc2=loc2-1
			if loc2==2 and enemyhealth2[4]==25:
				print("A great goblin clad in rusting iron armour stands between you and the safety of the overworld!")
			if loc2==1 and next==1 and key==False and portcullis==True:
				print("A primitive portcullis prevents you from leaving.  It is composed of iron bars too thick to cut through and is held in place by a chain and padlock.  If only you had the key...")
				loc=1
			if loc2==1 and next==1 and key==True and portcullis==True:
				print("A primitive portcullis stands between you and freedom.  It is held in place by a chain and padlock.  You try your luck with the rusty key and it works.  With effort, you push the portcullis out of your way.")
				portcullis=False
			if loc2==20 and enemyhealth2[3]==20:
				print("You find yourself in a large hall; this would appear to be where the goblins host their cannibalistic feasts.  A gigantic goblin clad in an apron and wielding a great cleaver sees you and steps forwards.")	
			for i in [0,1,2,3,4,5]:
				if loc2+1==enemy2[i] and enemyhealth2[i]!=0:
					if loc2-1!=1 and loc2+1!=21:
						health=health-1
						print("You are attacked!")
						print("You suffer 1 damage")
					else:
						health=health-3
						print("You are attacked!")
						print("You suffer 3 damage")
				if loc2-1==enemy2[i] and enemyhealth2[i]!=0:
					if loc2-1!=1 and loc2+1!=21:
						health=health-1
						print("You are attacked!")
						print("You suffer 1 damage")
					else:
						health=health-3
						print("You are attacked!")
						print("You suffer 3 damage")
			if health==0 or health==-1 or health==-2 or health==-3:
				print("You succumb to your injuries and die having never seen the light of day.")
				break
			if loc2==20 and enemyhealth2[3]==0 and next=="d":
				cont=True
				loc=20
				print("You explore the hall but find that it is a dead end leading to nothing but the kitchen, where grisly trophies hang from the ceiling, waiting to be eaten.")
				print("Press 1 to search the kitchen for supplies.")
				print("Press 2 to take the body parts down out of respect.")
				print("Press 3 to leave.")
				action=input("What do you do?")
				if action==1 and mushroom==True and cont==True:
					print("Among the body parts and utensils you find some rare cave mushrooms which have a healing effect upon humans.")
					print("Health increased by 50.")
					health=health+50
					mushroom=False
					cont=False
				if action==1 and mushroom==False and cont==True:
					print("You find no more mushrooms.")
					cont=False
				if action==2 and enemyhealth2[5]!=0 and cont==True:
					loc2=21
					print("You lose track of time as you collect the body parts and prepare to cremate them.  A goblin finds you and attacks you from behind.")
					print("You are stabbed in the back")
					print("You lose 2 health.")
					health=health-2
					enemy2=[4,14,7,21,1,22]
					cont=False
				if action==2 and enemyhealth2[5]==0 and fungus==True and cont==True:
					print("As you continue with the cremation you discover some edible fungi growing from the cave floor.  Eating them makes you feel much better.")
					print("Health increased by 50.")
					health=health+50
					fungus=False
					cont=False
				if action==2 and fungus==False and cont==True:
					print("You find no more fungi.")
					cont=False
				if action==3 and cont==True:
					print("You find your way out of the macabre dining hall and back in the cave.  A light is visible in the distance...")
					loc2=20
			if loc2==10:
				descend=input("You find yourself back at the ladder.  Press 5 to descend.  Press any other number not to.")
				if descend==5:
					down=True
					loc=19


		
if ended==True:
	print("You see the light of day for the first time in your life as you find yourself in the overworld, finally free from the goblins and the darkness of the mines.")

