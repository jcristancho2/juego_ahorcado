import random
import os

countries_list = ["Argentina", "Brazil", "Canada", "Denmark", "Egypt", "France", "Germany", "Hungary", "India", "Japan"]

random_number = random.randint(1, len(countries_list))


isPlaying = True
foundLetters = True
attempt = 0

country = countries_list[random_number]
guessed_letters = ['_'] * len(country)

while isPlaying:
    os.system('cls')
    print("Adivina el país")
    for letter in guessed_letters:
        print(letter, end=' ')
    print('\n')
    print(f"Intentos restantes: {3 - attempt}")
    foundLetters = False  
    guess = input("Ingrese letra: ")
    for idx,letra in enumerate(country):
        if letra.upper() == guess.upper():
            guessed_letters[idx] = guess.upper()
            foundLetters = True
            continue
    else:
        if foundLetters == False:
            attempt += 1
    if attempt == 3:
        print("Perdiste")
        isPlaying = False     
    elif ''.join(guessed_letters).upper() == country.upper():
        print(f"Felicidades! Has adivinado el país: {country}")
        isPlaying = False