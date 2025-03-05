""" 
EXEMPLE 1
but du programme :
    faire 255 - 40 + 25 = 240
    le resultat est stocke dans le registre r1

"""
EXEMPLE_1 = ["LDI r1 255",
            "LDI r2 40",
            "LDI r3 25",
            "SUB r1 r1 r2",
            "ADD r1 r1 r3",
            "HLT"]


"""PROGRAMME 2
but du programme : faire 4 x 5 = 20
résultat dans le registre 5
"""


EXEMPLE_2 = [
    "LDI r1 6",
    "LDI r2 9",
    "LDI r3 0",
    "LDI r5 0",
    "LDI r6 1",
    "ADD r5 r5 r2",
    "ADD r3 r3 r6",
    "SUB r6 r1 r3",
    "JZ 10",
    "JMP 5",
    "HLT"
]




"""PROGRAMME 3
but du programme :
    afficher un smiley
"""

EXEMPLE_3 = [
    "LDI r15 64",
    "LDI r15 13",
    "LDI r14 141",  # (13 + 128)
    "LDI r15 15",
    "LDI r14 141",  # (13 + 128)
    "LDI r15 12",
    "LDI r14 139",  # (11 + 128)
    "LDI r15 13",
    "LDI r14 138",  # (10 + 128)
    "LDI r15 14",
    "LDI r14 138",  # (10 + 128)
    "LDI r15 15",
    "LDI r14 138",  # (10 + 128)
    "LDI r15 16",
    "LDI r14 139"   # (11 + 128)
]


"""PROGRAMME GAUCHE-DROITE
but du programme : faire rebondir une balle sur l'écran de gauche à droite

en assembleur :

LDI r1 1	# pour vérifier si r4 == 1 et avancer la balle
LDI r2 31	# bord droit de l'écran
LDI r3 63	# pour enlever les 2 bits de clear et plot
LDI r4 1	# 1 si la balle avance, 2 si la balle recule
LDI r5 255	# la valeur a ajouter pour reculer de 1 pixel (pour savoir d'où vient la valeur 255, voir tout en bas de la page)
LDI r6 192	# pour afficher la balle

6# coordonnées d'origine de la balle et effacer l'écran au début et afficher la balle
LDI r15 0
LDI r14 0

LDI r15 93	# 29 + 64	X = 93
LDI r14 133	# 5 + 128	Y = 5

10# bouger la balle
SUB r0 r4 r1
JZ 13	# addr avancer la balle
JMP 16	# addr reculer la balle

13# avancer la balle
AND r15 r3 r15	# on met à 0 les 2 bits de clear et plot
ADD r15 r1 r15	# on avance la balle
JMP 19 		# addr afficher la balle

16# reculer la balle
AND r15 r3 r15	# on met à 0 les 2 bits de clear et plot
ADD r15 r5 r15	# on recule la balle
JMP 19		# addr afficher la balle INUTILE CAR LIGNE DAPRES DEJA AFFICHER LA BALLE


19# afficher la balle
ADD r15 r6 r15

20# vérifier si on est à un bord
#bord gauche
AND r15 r3 r15	# on met à 0 les 2 bits de clear et plot
SUB r0 r0 r15
JZ 27	# addr mettre r4 à 1

23# bord droit
AND r15 r3 r15	# on met à 0 les 2 bits de clear et plot
SUB r0 r2 r15
JZ 29	# addr mettre r4 à 2

JMP 10	# addr bouger la balle

27# mettre r4 à 1
LDI r4 1
JMP 10	# addr bouger la balle

29# mettre r4 à 2
LDI r4 2
JMP 10	# addr bouger la balle
"""

EXEMPLE_5 = [
    "LDI r1 1",
    "LDI r2 31",
    "LDI r3 63",
    "LDI r4 1",
    "LDI r5 255",
    "LDI r6 192",
    "LDI r15 0",
    "LDI r14 0",
    "LDI r15 93",
    "LDI r14 133",
    "SUB r0 r4 r1",
    "JZ 13",
    "JMP 16",
    "AND r15 r3 r15",
    "ADD r15 r1 r15",
    "JMP 19",
    "AND r15 r3 r15",
    "ADD r15 r5 r15",
    "ADD r15 r6 r15",
    "AND r15 r3 r15",
    "SUB r0 r0 r15",
    "JZ 27",
    "AND r15 r3 r15",
    "SUB r0 r2 r15",
    "JZ 29",
    "JMP 10",
    "LDI r4 1",
    "JMP 10",
    "LDI r4 2",
    "JMP 10"
]
