import spytank 

while True:
    lettre=input(">>>")
    if lettre =="z":
        spytank.avance(150)
    elif lettre =="s":
        spytank.recule(150) 
    elif  lettre=="x":
        spytank.stop()      
 