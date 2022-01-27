
import random
import sys

from time import sleep
from random import randrange

curInput = ""

passwrd = ""

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
alpUP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

hash = ['1', '2', '3', '4', '5']

dMode = input("\n   |\n   |   Standard, Key, Or Exit? ( S / K / E ) >> ")

for i in range(randrange(35)):
    curInput += str(randrange(12))

def PassFunc():

    password = ""

    print("   |\n   |   Creating Password... \n   |")

    print("   |   Adding stuff together... \n   |")

    for i in range(12):

        password += str(random.choice(alp))
        password += random.choice(alpUP)

        ran = ['foo', 'larb']
        
        if random.choice(ran) == 'larb':
            password += str(random.choice(hash))  
              
        for i in range(3):
                    password += str(random.choice(hash))

    for i in range(12):
        password += str(random.choice(hash))

    print('   |   Your New Password: \n   | \n   |   ' + password + ' \n   |\n   |   Don\'t tell anybody! \n   |')
    passwrd = password

    Save(password)

def DebugPassFunc(key):

    password = ""

    print("   |\n   |   Creating Password... \n   |")

    print("   |   Thinking of the perfect password... \n   |")

    for i in range(12):

        password += str(random.choice(alp))
        password += random.choice(alpUP)

        i = random.choice(key)

        if i != " ":
            password += i

        ran = ['foo', 'larb']
        
        if random.choice(ran) == 'larb':
            password += str(random.choice(hash))

        for i in range(3):
            password += str(random.choice(hash))

    for i in range(12):
        password += str(random.choice(hash))

    print("   |   Your New Password: \n   | \n   |   " + password + " \n   |\n   |   Don't tell anybody! \n   |")

    Save(password)

def Save(Password):
    with open('CurrentPassword.txt', 'w') as f:
        f.write('Your Latest Password: \n \n     ' + Password + ' \n \nDon\'t tell anybody!|')
    
    print("   |   This Password Has Been Saved To CurrentPassword.txt, you can find your latest password there \n   |")

if dMode.lower() == "s":
    PassFunc()

    print("   |   Exiting in 15 seconds...")
    sleep(10)

elif dMode.lower() == "k":
    dInput = input("   |\n   |   Input Key: ")
    DebugPassFunc(dInput)

    print("   |   Exiting in 15 seconds...")
    sleep(10)

elif dMode.lower() == "e":
    exit()