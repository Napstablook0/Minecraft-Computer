


-----------CREDITS-----------

- création de l'ordinateur (hardware)							: 	Raphael HUC
- théorisation de l'assembleur et résolution des problèmes		: 	raph
- écriture des codes en assembleur (software)					:	moi
- réalisation du compilateur									:	moi-même
- organisation du projet										:	toujours moi
- rédaction du mannuel											:	ca change pas
- placement des instruction assembleur dans une liste			:	chatGPT




---------MANNUEL D'UTILISATION DE MON ORDINATEUR MINECRAFT---------

Si vous souhaitez en apprendre d'avantage sur mon ordinateur ou même programmer et faire tourner un code
dessus, c'est ici que j'explique tout.

De manière générale, mon projet est écrit en un mix d'anglais et de français.

Je n'ai que 17 ans et ce projet m'a prit environ 3 mois à réaliser.


-------MANNUEL DES DOSSIER DU PROJET-------


---EXEMPLES DE PROGRAMMES

- Le dossier videos montre mon ordinateur faisant tourner plusieurs programmes
- le fichier assembly_program contient plusieurs scripts en assembleur et leur code en langage machine
compilé

---ASSEMBLEUR ET ECRITURE DE CODE

- Le fichier instruction_set_and_screen_protocol contient le jeu d'instruction (instruction set) de mon
assembleur
- le dossier compiler est le compilateur de mon assembleur, il permet donc de convertir un code assembleur en
son langage machine
interprétable par mon ordinateur. Pour plus de détails, aller lire les commentaires en tête des scripts
python du dossier compiler
- le dossier images contient plusieurs images pour mieux se représenter physiquement à quoi ressemble
l'ordinateur




-------DETAILS DE MON ORDINATEUR-------


C'est un ordinateur 8-bits

---VITESSE de l'ordinateur

- 7,8 Hz/min quand le jeu tourne a vitesse normale : 20 tics/s
- le jeu peut etre artificiellement accéléré en utilisant des commandes et le mod "Carpet",
augmentant ainsi la vitesse de calcul de l'ordinateur

---MEMOIRE de l'ordinateur

- 16 registres de mémoire dont le registre r0 qui est un "0-register" et les registres r14 et r15 qui sont
utilisés pour intéragir avec l'ordinateur, donc en soit, 13 octets de mémoire

---OPERATIONS possibles

- 9 opération mathématiques et arithmétiques au total (voir la fiche "assembly" du fichier
instruction_set_and_screen_protocol)

---INTERACTIONS AVEC L'ECRAN

- Possibilité d'allumer un pixel sur l'écran en utilisant les coordonnées x et y du dit pixel
- possibilité d'éffacer l'écran en entier (mais pas un pixel en particulier)



-------POUR ECRIRE ET FAIRE TOURNER UN PROGRAMME SUR MON ORDINATEUR-------


--- ETAPE 1 : AVOIR UN CODE ASSEMBLEUR

si vous avez déjà votre code en assembleur, passez cette étape

- Pour écrire votre code assembleur, lisez le jeu d'instructions (instruction set) puis écrivez votre code,
si vous devez intéragir avec l'écran, lisez aussi le protocole de l'écran (screen protocol) du même fichier
que le jeu d'instruction (instruction set)

--- ETAPE 2 : PASSER DE L'ASSEMBLEUR A LA LISTE PYTHON

si vous avez déjà votre code compilé, passez à l'étape 4

- Vous devez placer votre script assembleur dans une liste python, chaque valeur de cette liste est une
chaine de caractere contenant une ligne du code, voici un exemple de code assembleur écrit dans une liste :
SCRIPT_EXEMPLE = ["LDI r1 255",
			"LDI r2 40",
			"LDI r3 25",
			"SUB r1 r1 r2",
			"ADD r1 r1 r3",
			"HLT"]
pour faire cela et si votre script est trop long à écrire à la main dans une liste, demandez simplement à une
IA de le faire à votre place

--- ETAPE 3 : COMPILATION DU CODE

- Ouvrez le dossier compiler dans un éditeur de code python
- placez votre liste dans le script exemples.py
- allez dans le script main.py et remplacez la ligne :
	instructions = EXEMPLE
par :
	instructions = VOTRE_LISTE_DEFINIE_DANS_EXEMPLE_PY
- executez ensuite main.py
- vous avez votre code compilé !

--- ETAPE 4 : OUVRIR LE MONDE MINECRAFT

si vous avez déjà le monde minecraft ouvert, passez cette étape

- Lancez le monde minecraft contenant l'ordinateur (le world download du monde est dans la racine du projet,
c'est le dossier "redstone computer")
- pour cela, creez un modpack en 1.21.1 sur le logiciel forge, installez les mods "carpet" et "WorldEdit",
assurez vous de télécharger les versions compatibles avec la 1.21.1
- ensuite, appuyez su les 3 points à gauche du bouton play puis allez dans "open folder" et placez le world 
download dans le dossier save
- fermez le gestionnaire de fichier et lancez le modpack forge en appuyant sur "play"
- dans "solo" vous devriez voir le monde "redstone computer" contenant l'ordinateur, lancez-le

--- ETAPE 5 : ECRIRE LE CODE SUR L'ORDINATEUR MINECRAFT

- Vous voyez le gros bloc vert clair ? c'est la mémoire à instruction (instruction memory) c'est là qu'on va
placer le code (voir l'image instruction_memory du dossier images)
- allez au dessus de la mémoire à instruction, un de ses coins contient un bloc noir, allez vers ce bloc
- chaque colonne (voir l'image "colonnes" dans le dossier images) est un ligne/instruction de langage
machine, le premier bit, celui tout en haut de chaque colonnes est le bit le plus à droite (voir l'image  
bits_colonne dans le dossier images)
- la premiere instruction est la colonne en dessous du bloc noir dans le coin supérieur de la mémoire à
instruction (instruction memory)
- la deuxième est à sa gauche (vue de face), la troisième à la gauche de la deuxième et ainsi de suite
- au bout de 8 instructions, la prochaine instruction à écrire est à placer derrière la toute première (vue
de face)
- en somme, si on regarde la mémoire à instruction de dessus avec le bloc noir placez en haut à gauche, les
instructions doivent être placées dans l'ordre d'écriture (gauche à droite et haut vers le bas), voir l'image
"ordre_ecriture" du dossier images

- pour placer un bit:
	- ouvrez votre inventaire et cherchez un block rouge nommé block de redstone (à ne pas confondre avec un
	block de laine rouge)
	- prenez le et placez-le sur le bloc de laine vert devant le bloc lumineux (voir l'image "placer_bit"
	dans le dossier images)
- les block de redstone représente un 1 et l'absence de block représente un 0

--- ETAPE 6 : EXECUTION DU CODE

- Entre la mémoire à instruction et l'écran, il y a une petite tour jaune (le compteur de programme (program
counter)), allez vers lui (voir l'image program_counter du dossier images)
- appuyez sur le bouton de droite placé au bout du "pont" maron au pied de la tour jaune (voir l'image
bouton_execution du dossier images)
- le programme est maintenant en cours d'éxécution ! Vous pouvez regarder l'écran sur votre gauche (vue face
au bouton)
- quand la boucle formée par le circuit sur le "pont" maron sera arrêtée, c'est que le programme sera finit
d'éxecuter (par l'instruction HALT)
- pour voir les résultat dans les registres, allez vers la grosse construction rose, à droite de l'écran
- chaque block lumineux est un bit, chaque colonne de bit est un octet (et un registre donc) dont le msb
(most significant bit) est celui le plus en haut, voir l'image registres du dossier images
- afin de pouvoir réexecuter l'ordinateur, vous devez remettre à zero le compteur de programme (program
counter), pour cela, revenez devant le bouton qui permet d'éxecuter le programme et appuyez sur l'autre
bouton, placé à sa gauche
- le compteur est maintenant revenu à zero, vous pouvez à nouveau exécuter le programme

