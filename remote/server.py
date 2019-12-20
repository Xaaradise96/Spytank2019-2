import network
import spytank
from gtts import tts
import os 
import detecteur

IP = "10.0.0.184"
PORT = 1111
vitesse = 150 
direction = 1
etatLed = 0
stop = False
continuer = True

socket = network.newServerSocket()
socket.bind((IP,PORT))

threadDetecteur = detecteur.newDetecteur(stop)
threadDetecteur.deamon = True
threadDetecteur.start()

text = "initialisation du programme"
audio = tts.gTTS(text = text, lang = "fr")
audio.save("init.mp3")
os.system("mpg321 init.mp3")

while continuer :
    socket.listen(10)
    print("en ecoute...")

    thread = network.newThread(socket.accept())
    

    message = thread.clientsocket.recv(4096)
    lettre = message.decode("utf-8")
    print("message recu :", lettre)
    if stop == False:
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

        elif  lettre == "x":
            spytank.stop()
        elif lettre == "f":
            continuer = False
            spytank.stop()  
        elif lettre == "a":
            if etatLed == 0 :
                spytank.led(0,1)
                spytank.led(1,1)
                spytank.led(2,1)
                spytank.led(3,1)
                etatLed = 1 
            else:
                spytank.led(0,0)
                spytank.led(1,0)
                spytank.led(2,0)
                spytank.led(3,0)
                etatLed = 0
