palos = ['o', 'c', 'e', 'b']
numeros = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
baraja = []

def creaBaraja():
    for item in palos: 
        for ix in numeros:
            baraja.append(item + ix) 
    return baraja 
    
española = creaBaraja()

print("La española es", española)
