import network
import click 

IP = "10.0.0.184"
PORT = 1111
z  = "z : avancer "
s  = "s : reculer"
q  = "q : tourner a gauche"
d  = "d : tourner a droite"
vp = "+ : plus vite"
vm = "- : moins vite"
x  = "x : stop "
a = "a : allumer ou eteindre les leds"


print(z,s,q,d,vp,vm,x)
while True:
    socket = network.newClientSocket()
    socket.connect((IP,PORT))

    print("Tape la lettre a afficher")
    lettre = click.getchar()
    
    socket.send(lettre.encode())


