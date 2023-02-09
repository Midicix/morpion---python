from tkinter import *
import tkinter.messagebox

#####################################
# Creation de l'interface graphique #
#####################################
fenetre = Tk()
fenetre.title("Morpion")

etiquette1 = Label(fenetre, text="Joueur 1:", font='Times 20 bold', bg='red',
                   fg='white', height=1, width=8)
etiquette1.grid(row=1, column=0)

etiquette2 = Label(fenetre, text="Joueur 2:", font='Times 20 bold', bg='blue',
                   fg='white', height=1, width=8)
etiquette2.grid(row=2, column=0)

# Création de variables de type modifiable et géré par tkinter
nom_j1 = StringVar()
nom_j2 = StringVar()

# Création des champs de saisie de texte
saisie1 = Entry(fenetre, textvariable=nom_j1, bd=5)
saisie1.grid(row=1, column=1, columnspan=2)
saisie2 = Entry(fenetre, textvariable=nom_j2, bd=5)
saisie2.grid(row=2, column=1, columnspan=2)

# Création des boutons
bouton1 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton1))
bouton1.grid(row=3, column=0)

bouton2 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton2))
bouton2.grid(row=3, column=1)

bouton3 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton3))
bouton3.grid(row=3, column=2)

bouton4 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton4))
bouton4.grid(row=4, column=0)

bouton5 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton5))
bouton5.grid(row=4, column=1)

bouton6 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton6))
bouton6.grid(row=4, column=2)

bouton7 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton7))
bouton7.grid(row=5, column=0)

bouton8 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton8))
bouton8.grid(row=5, column=1)

bouton9 = Button(fenetre, font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8,
                 command=lambda: clic_bouton(bouton9))
bouton9.grid(row=5, column=2)

liste_bouton = [bouton1, bouton2, bouton3, bouton4, bouton5, bouton6, bouton7, bouton8, bouton9]


# initialisation des variables
trait_j1 = True  # booléen précisant si le trait(tour de jeu) est au joueur 1.
tour = 0  # indice du tour de jeu


def eteindre_bouton():
    """désactive tous les boutons
    """
    for bouton in liste_bouton:
        bouton.configure(state=DISABLED)


def clic_bouton(bouton):
    """gere le clic sur le bouton 'bouton'
    """
    global trait_j1, tour

    if bouton["text"] != "":
        tkinter.messagebox.showinfo("Morpion", "Bouton déja cliqué !")
    else:
        if trait_j1 is True:
            nom_j = nom_j1
            bouton["text"] = "X"
            bouton["bg"] = 'red'
        else:
            nom_j = nom_j2
            bouton["text"] = "O"
            bouton["bg"] = 'blue'

        test_gain = verifier_gain()

        if test_gain == "gain":
            eteindre_bouton()
            tkinter.messagebox.showinfo("Morpion", nom_j.get()+" gagne !")
        elif test_gain == "nul":
            eteindre_bouton()
            tkinter.messagebox.showinfo("Morpion", "Match nul !")
        else:
            trait_j1 = not(trait_j1)
            tour += 1


def verifier_gain():
    """ vérifie s'il y a un gain et renvoie "gain", "nul" ou "continue"
    """
    if (bouton1['text'] == 'X' and bouton4['text'] == 'X' and bouton7['text'] == 'X' or
        bouton2['text'] == 'X' and bouton5['text'] == 'X' and bouton8['text'] == 'X' or
        bouton3['text'] == 'X' and bouton6['text'] == 'X' and bouton9['text'] == 'X' or
        bouton1['text'] == 'X' and bouton2['text'] == 'X' and bouton3['text'] == 'X' or
        bouton1['text'] == 'X' and bouton5['text'] == 'X' and bouton9['text'] == 'X' or
        bouton3['text'] == 'X' and bouton5['text'] == 'X' and bouton7['text'] == 'X' or
        bouton4['text'] == 'X' and bouton5['text'] == 'X' and bouton6['text'] == 'X' or
        bouton7['text'] == 'X' and bouton8['text'] == 'X' and bouton9['text'] == 'X' ):
        return "gain"

    elif (bouton1['text'] == 'O' and bouton4['text'] == 'O' and bouton7['text'] == 'O' or
        bouton2['text'] == 'O' and bouton5['text'] == 'O' and bouton8['text'] == 'O' or
        bouton3['text'] == 'O' and bouton6['text'] == 'O' and bouton9['text'] == 'O' or
        bouton1['text'] == 'O' and bouton2['text'] == 'O' and bouton3['text'] == 'O' or
        bouton1['text'] == 'O' and bouton5['text'] == 'O' and bouton9['text'] == 'O' or
        bouton3['text'] == 'O' and bouton5['text'] == 'O' and bouton7['text'] == 'O' or
        bouton4['text'] == 'O' and bouton5['text'] == 'O' and bouton6['text'] == 'O' or
        bouton7['text'] == 'O' and bouton8['text'] == 'O' and bouton9['text'] == 'O' ):
        return "gain"

    elif(tour == 8):
        return "nul"

    else:
        return "continue"


fenetre.mainloop()
