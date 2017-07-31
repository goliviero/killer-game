# English documentation (french below) :

## General
A killer-game generator
2 modes are available :

- Mode 1 : mission mode
- Mode 2 : item + location mode

## Instructions
1. List players go in `players.txt` with first and last name (1 name by line)

2. Mode 1 : missions go in `missions.txt` (1 entry by line)
   Mode 2 : items go in `items.txt` and locations in `locations.txt` (1 entry by line)

3. Launch the script with the following command : `python murder.py`
   Enter your mode : 1 or 2
   The python script give you a nice, print-ready latex murder game file `murder-out.tex` with a mission for everybody
   Convert the latex document into PDF
   Print and cut
   Play !

# Français :

## Généralités

Un générateur du jeu du killer.
2 'modes' sont disponibles :

- Mode 1 : mode mission
- Mode 2 : mode objet + localisation

## Instructions
1. La liste des joueurs vont dans le fichier `players.txt` avec leur prénom + nom (1 nom par ligne)

2. Pour le mode 1 : les missions vont dans le fichier `missions.txt`  (1 entrée par ligne)
   Pour le mode 2 : les objets vont dans le fichier `items.txt`	et les localisations dans le fichier `locations.txt` (1 entrée par ligne)

3. Lancez le programme avec la commande : `python murder.py`
   Entrer votre mode : 1 ou 2
   Le programme sortira un document entier imprimable latex appelé `murder-out.tex` avec les missions pour chaque personne
   Convertisser le document latex en PDF
   Imprimer et découper
   Jouez !
