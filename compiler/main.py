"""Ce script converti un programme ecrit en assembleur (assembleur du processeur minecraft) en son langage machine
le script exemples.py contient plusieurs exemples de code en assembleur a convertir,
pour convertir un code assembleur, il faut: le definir dans le script exemples.py, puis modifier la ligne :
INSTRUCTIONS = EXEMPLE_1
du script present pour definir INSTRUCTIONS comme la variable definie dans le script exemples.py"""


from examples import *
from program import Assembly_program


INSTRUCTIONS = EXEMPLE_5


def main():
    print("-"*50)
    assemb_prog = Assembly_program(INSTRUCTIONS)
    converted_to_machine_code = assemb_prog.getMachineCode()
    
    if converted_to_machine_code == "CODE INVALIDE":
        print("CODE INVALIDE")
    else:
        for i in range(len(converted_to_machine_code)):
            print("line " + str(i) + " : " + str(converted_to_machine_code[i]))
    

if __name__ == "__main__":
    main()