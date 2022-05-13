#####################################################################
# Docstring
#
#
#####################################################################

# ------------------------- Bibliothèques ------------------------- #

import tkinter as tk

# --------------------------- Constante --------------------------- #
HEIGHT_CANVAS = WIDHT_CANVAS = 600
N = 11
# ----------------------- Varaibles Globale ----------------------- #
xh = HEIGHT_CANVAS/N
yh = HEIGHT_CANVAS/N
xb = HEIGHT_CANVAS/N
yb = WIDHT_CANVAS/N
# ------------------------ Partie Fonction ------------------------ #


def Grille():
    # Création de la grille
    grille = []
    for i in range(0, N):
        intermediaire = []
        for j in range(1, N+1):
            intermediaire.append(canvas.create_rectangle((j-1)*xh, i*yh, j*xb, (i+1)*yb,
                                                         fill="brown",
                                                         outline="black", width=10))
        grille.append(intermediaire)

# ------------------------ Code Principale ------------------------ #
racine = tk.Tk()
# Parrametre de la racine et Canvas
racine.title("SCE")
canvas = tk.Canvas(bg='#f1f1f1', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)


# mainloop
racine.mainloop()
# ----------------------- Fin du programme  ----------------------- #
