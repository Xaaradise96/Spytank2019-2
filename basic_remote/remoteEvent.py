import click
import spytank
import time 

z  = "z : avancer "
s  = "s : reculer"
q  = "q : tourner a gauche"
d  = "d : tourner a droite"
vp = "+ : plus vite"
vm = "- : moins vite"
x  = "x : stop "
vitesse = 150
direction = ""



print(z,s,q,d,vp,vm,x)

while True :
    lettre = click.getchar()
    if lettre =="z":
        spytank.avance(vitesse)
        direction = 1
    elif lettre =="s":
        spytank.recule(vitesse)
        direction = 2
    elif lettre == "q":
        spytank.gauche(vitesse) 
        direction = 3 
    elif lettre == "d":
        spytank.droite(vitesse)
        direction = 4
    elif lettre == "+":
        if vitesse < 250 :
            vitesse = vitesse +10

        if direction == 1:
            spytank.avance(vitesse)
        elif direction == 2:
            spytank.recule(vitesse)
        elif direction == 3:
            spytank.gauche(vitesse)
        elif direction == 4:
            spytank.droite(vitesse) 

    elif lettre == "-":
        if vitesse > 70 :
            vitesse = vitesse -10

        if direction == 1:
            spytank.avance(vitesse)
        elif direction == 2:
            spytank.recule(vitesse)
        elif direction == 3:
            spytank.gauche(vitesse)
        elif direction == 4:
            spytank.droite(vitesse) 

    elif  lettre=="x":
        spytank.stop()
    
    time.sleep(1)

    print("tu as tapé la lettre:", lettre)