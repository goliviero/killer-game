#!/usr/bin/env python

import random
mode = raw_input("Tapez 1 pour le mode mission ou tapez 2 pour le mode armes / localisations : ")

# First step, construct a random ring of players
# The ring is a tuple of (killer, victim) that forms a single loop

with open('players.txt', 'r') as f:
    players = [l.strip() for l in f.readlines()]
    random.shuffle(players)

ring = []
for i in range(len(players)):
    if i == len(players) - 1:
        ring.append((players[i], players[0]))
    else:
        ring.append((players[i], players[i+1]))

game = []

# Enter in mode 1 (mission mode)
if mode == str(1):
    print('Mode mission activee, n\'oubliez pas de remplir les fichiers players.txt et missions.txt')

    # Game with mission :
    with open('missions.txt', 'r') as f:
        mission = [l.strip() for l in f.readlines()]

    # Unique mission :
    for p in ring:
        choosed_mission=random.choice(mission)
        pair=[(p, choosed_mission)]
        game.append(pair)
        mission.remove(choosed_mission)

        # Latex output :
        f = open('murder-out.tex', 'w')
        f.write(r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[cm]{fullpage}
\usepackage{array}
\makeatletter
\newcommand{\thickhline}{%
\noalign {\ifnum 0=`}\fi \hrule height 1pt
\futurelet \reserved@a \@xhline
}
\newcolumntype{"}{@{\hskip\tabcolsep\vrule width 1pt\hskip\tabcolsep}}
\makeatother
\begin{document}
\centering
\renewcommand{\arraystretch}{3}
\setlength{\tabcolsep}{10pt}
\large
""")  # python will convert \n to os.linesep
    i=0
    while game:
        if game:
            g = game.pop()
            print("---- Iteration #" + str(i) + "----")
            print("Tueur = " + str(g[0][0][0]))
            print("Cible = " + str(g[0][0][1]))
            print("Mission = " + str(g[0][1]))
            print('')
            i+=1
            f.write(r"""
\begin{tabular}{"c"}""")
            f.write(r"\thickhline")
            f.write(r" Tueur : {} \\ \footnotesize Cible : {}  \\ \footnotesize Mission : {} \\".format(g[0][0][0], g[0][0][1], g[0][1]))
            f.write(r"""
\thickhline
\end{tabular}
                """)

        # Print the latex footer
    f.write(r"""
\end{document}
    """)

    f.close()


# Enter in mode 2 (items / locations mode)
if mode == str(2):
    print('Mode objet / localisation activee, n\'oubliez pas de remplir les fichiers players.txt, items.txt, locations.txt')

    # Game with item and location instead of mission :
    with open('items.txt', 'r') as f:
        items = [l.strip() for l in f.readlines()]

    with open('locations.txt', 'r') as f:
        locations = [l.strip() for l in f.readlines()]

    # Unique pair of item / location
    for p in ring:
        choosed_item=random.choice(items)
        choosed_location=random.choice(locations)
        triplet=[(p, choosed_item, choosed_location)]
        game.append(triplet)
        items.remove(choosed_item)
        locations.remove(choosed_location)

    # Not unique pair of item / location
    #game = [(p, random.choice(locations), random.choice(items)) for p in ring]

    # Sort game to be alphabetical by killer for easier handout
    game.sort(key=lambda g: g[0][0], reverse=True)

    f = open('murder-out.tex', 'w')
    f.write(r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[cm]{fullpage}
\usepackage{array}
\makeatletter
\newcommand{\thickhline}{%
\noalign {\ifnum 0=`}\fi \hrule height 1pt
\futurelet \reserved@a \@xhline
}
\newcolumntype{"}{@{\hskip\tabcolsep\vrule width 1pt\hskip\tabcolsep}}
\makeatother
\begin{document}
\centering
\renewcommand{\arraystretch}{3}
\setlength{\tabcolsep}{10pt}
\large
""")  # python will convert \n to os.linesep
    i=0
    while game:
        if game:
            g = game.pop()
            print("---- Iteration #" + str(i) + "----")
            print("Tueur = " + str(g[0][0][0]))
            print("Cible = " + str(g[0][0][1]))
            print("Objet = " + str(g[0][1]))
            print("Localisation = " + str(g[0][2]))
            print('')

            f.write(r"""
\begin{tabular}{"c"}""")
            f.write(r"\thickhline")
            f.write(r" Tueur : {} \\ \footnotesize Cible : {}  \\ \footnotesize Mission : Le/la tuer avec {} dans {} \\".format(g[0][0][0], g[0][0][1], g[0][1], g[0][2]))
            f.write(r"""
\thickhline
\end{tabular}
""")

    # Print the latex footer
    f.write(r"""
\end{document}
    """)

    f.close()

if mode != str(1) and mode != str(2):
    print ("Mode invalide !")
    print("Relancez le programme et entrez un mode valide (1 ou 2)")
