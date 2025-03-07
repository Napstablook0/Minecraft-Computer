""" 
PROGRAMME 1
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

LDI r1 1	# l'acceleration de la balle écrit en complément à 2, 1 si elle avance, 255 si elle recule (voir bas de la page)
LDI r2 31	# bord droit de l'écran
LDI r3 63	# pour enlever les 2 bits de clear et plot du r15
LDI r6 192	# pour afficher la balle (mettre à 1 le bit de plot du r15)

# LIGNE 4 coordonnées d'origine de la balle, effacer l'écran au début et afficher la balle
LDI r15 0
LDI r14 0

LDI r15 93	# 29 + 64	X = 93
LDI r14 133	# 5 + 128	Y = 5


# LIGNE 8 update la balle
AND r15 r3 r15	# on met à 0 les 2 bits de clear et plot
ADD r15 r1 r15	# on avance/recule la balle

# LIGNE 10 afficher la balle
ADD r15 r6 r15

# LIGNE 11 vérifier si on est à un bord
# bord gauche
AND r15 r3 r15	# on met à 0 les 2 bits de clear et plot
SUB r0 r0 r15
JZ 17	# addr mettre r1 à 1

# bord droit
SUB r0 r2 r15
JZ 19	# addr mettre r1 à 255

# ni a gauche ni à droite
JMP 8	# addr update la balle

# LIGNE 17 mettre r1 à 1
LDI r1 1
JMP 8	# addr update la balle

# LIGNE 19 mettre r1 à 255
LDI r1 255
JMP 8	# addr update la balle
"""

EXEMPLE_5 = [
    "LDI r1 1",
    "LDI r2 31",
    "LDI r3 63",
    "LDI r6 192",
    "LDI r15 0",
    "LDI r14 0",
    "LDI r15 93",
    "LDI r14 133",
    "AND r15 r3 r15",
    "ADD r15 r1 r15",
    "ADD r15 r6 r15",
    "AND r15 r3 r15",
    "SUB r0 r0 r15",
    "JZ 17",
    "SUB r0 r2 r15",
    "JZ 19",
    "JMP 8",
    "LDI r1 1",
    "JMP 8",
    "LDI r1 255",
    "JMP 8"
]
