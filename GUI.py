# -*- coding: utf-8 -*-

# TODO Rendre la GUI executer quand on l'appelle dans le terminal

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox
import os


#set des variables en fonction de l'OS :
#TODO packager tout ca dans une fonction
os_name = os.name

#meilleures valeurs pour Linux : (TO DEFINE)
#background color
bg_color = "#E8E8E8"
#art
art = "           ________   Renseignez les données d'un patient\n          |           |  /   ou essayez avec un patient de test\n          |   |    |  |\n          |           |\n          |___  ___|\n         ____|  |____\n \n"

if os_name == "nt": #windows
    bg_color = "#F0F0F0"
    art = "          _______ _   Renseignez les données d'un patient\n           |            |  /   ou essayez avec un patient de test\n           |   |    |  |\n           |            |\n           |___  _ __|\n         ____|  |____\n \n"
elif os_name == "posix": #OS X
    bg_color = "#E8E8E8"
    art = "           ________   Renseignez les données d'un patient\n          |           |  /   ou essayez avec un patient de test\n          |   |    |  |\n          |           |\n          |___  ___|\n         ____|  |____\n \n"



# Tooltip sert a donner explication quand on se met sur un bouton
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

            # ===================================================================


def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# Creer
win = tk.Tk()
win.columnconfigure(0, weight=1)

# Modifier Titre
win.title("Visualisation Projet IA")

# win.resizable(0,0)

# Ajouter page--------------------------------------
tabControl = ttk.Notebook(win)

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Heart AI')

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# ---------------Heart GUI Start------------------#
monty3 = ttk.LabelFrame(tab3, text="Données mesurées sur un patient")
monty3.grid(column=0, row=0, padx=10, pady=0)

#FIXME label sur mac comportement bizarre

# TextBox Age
labelText1 = tk.StringVar()
labelText1.set("Age :")
ttk.Label(monty3, width=16, textvariable=labelText1, justify='left').grid(column=0, row=0)

age = tk.DoubleVar()
tk.Entry(monty3, textvariable=age, width=8, justify='left', highlightbackground=bg_color, background=bg_color).grid(
    column=1, row=0, sticky='NW')

labelUnit1 = tk.Label(monty3, text="ans", anchor='w', width=8, justify='right', background=bg_color)
labelUnit1.grid(column=1, row=0)

ttk.Label(monty3, textvariable=labelUnit1, justify='right').grid(column=1, row=0)
ttk.Separator(monty3, orient='horizontal').grid(row=1, columnspan=3, sticky="ew")

# Boutons hommes femmes
labelText2 = tk.StringVar()
labelText2.set("Sexe :")
ttk.Label(monty3, width=16, textvariable=labelText2, justify='left').grid(column=0, row=2)

sex = tk.StringVar()
sex.set('0.0')
tk.Radiobutton(monty3, text="Femme", variable=sex, value='0.0', width=12, justify='left', background=bg_color).grid(
    column=1, row=2, sticky='W')
tk.Radiobutton(monty3, text="Homme", variable=sex, value='1.0', width=12, justify='left', background=bg_color).grid(
    column=2, row=2, sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=3, columnspan=3, sticky="ew")

# Bouton Type de douleur à la poitrine
labelText3 = tk.StringVar()
labelText3.set("Type de douleur \nà la poitrine")
ttk.Label(monty3, width=16, textvariable=labelText3, justify='left').grid(column=0, row=4, rowspan=2)

chestPain = tk.StringVar()
chestPain.set('1.0')
tk.Radiobutton(monty3, text="Angor typique", variable=chestPain, value='1.0', justify='left',
               background=bg_color).grid(column=1, row=4, sticky='W')
tk.Radiobutton(monty3, text="Angor anormale", variable=chestPain, value='2.0', justify='left',
               background=bg_color).grid(column=2, row=4, sticky='W')
tk.Radiobutton(monty3, text="Douleur non relative \n à un angor", variable=chestPain, value='3.0', justify='left',
               background=bg_color).grid(column=1, row=5, sticky='NW')
tk.Radiobutton(monty3, text="Asymptomatique", variable=chestPain, value='4.0', justify='left',
               background=bg_color).grid(column=2, row=5, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=5, columnspan=3, sticky="ews")

# TextBox Pression Sanguine
labelText4 = tk.StringVar()
labelText4.set("Pression Sanguine :")
ttk.Label(monty3, width=16, textvariable=labelText4, justify='left').grid(column=0, row=6)

pression_sang = tk.DoubleVar()
tk.Entry(monty3, textvariable=pression_sang, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=6, sticky='NW')

labelUnit4 = tk.Label(monty3, text="mmHg", anchor='w', width=8, justify='right', background=bg_color)
labelUnit4.grid(column=1, row=6)

ttk.Separator(monty3, orient='horizontal').grid(row=7, columnspan=3, sticky="ew")

# TextBox Choléstérol Sérique
labelText5 = tk.StringVar()
labelText5.set("Choléstérol Sérique :")
ttk.Label(monty3, textvariable=labelText5, justify='left').grid(column=0, row=8)

chol_sterique = tk.DoubleVar()
tk.Entry(monty3, textvariable=chol_sterique, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=8, sticky='NW')

labelUnit5 = tk.Label(monty3, text="mg/dL", anchor='w', width=8, justify='right', background=bg_color)
labelUnit5.grid(column=1, row=8)

ttk.Separator(monty3, orient='horizontal').grid(row=9, columnspan=3, sticky="ew")

# #TextBox glycémie à jeun
labelText6 = tk.StringVar()
labelText6.set("Glycémie à jeun :")
ttk.Label(monty3, width=16, textvariable=labelText6, justify='left').grid(column=0, row=10)

glycemie = tk.DoubleVar()
#tk.Entry(monty3, textvariable=glycemie, width=8, justify='left', highlightbackground=bg_color,
        # background=bg_color).grid(column=1, row=10, sticky='NW')

tk.Radiobutton(monty3, text="> 120 mg/dL", variable=glycemie, value='1.0', justify='left', background=bg_color).grid(
    column=1, row=10, sticky='NW')
tk.Radiobutton(monty3, text="< 120 mg/dL", variable=glycemie, value='0.0', justify='left', background=bg_color).grid(
    column=2, row=10, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=11, columnspan=3, sticky="ew")

# #Bouton ECG au repos
labelText7 = tk.StringVar()
labelText7.set("ECG au repos :")
ttk.Label(monty3, width=16, textvariable=labelText7, justify='left').grid(column=0, row=12)

ecgresult = tk.StringVar()
ecgresult.set('0.0')
tk.Radiobutton(monty3, text="Normal", variable=ecgresult, value='0.0', justify='left', background=bg_color).grid(
    column=1, row=12, sticky='NW')
#Having ST-T wave abnormality (T wave inversions and/or \n ST elevation or depression of > 0.05 mV)"
tk.Radiobutton(monty3, text="Onde ST-T anormale (inversion de l'onde T et\ou \n décalage du segment ST > 0.05 mV)", variable=ecgresult, value='1.0', justify='left',
               background=bg_color).grid(column=1, row=13, sticky='NW', columnspan=2)
tk.Radiobutton(monty3, text="Présence probable ou confirmée \nd'hypertrophie du ventricule gauche "
                            "par le critère d'Estes", variable=ecgresult, value='2.0', justify='left',
               background=bg_color).grid(column=1, row=14, sticky='NW', columnspan=2)

ttk.Separator(monty3, orient='horizontal').grid(row=15, columnspan=3, sticky="ew")

# TextBox Fréquence Cardiaque maximale
labelText8 = tk.StringVar()
labelText8.set("Fréquence Cardiaque Maximale ")
ttk.Label(monty3, textvariable=labelText8, justify='left').grid(column=0, row=16)

fcm = tk.DoubleVar()
tk.Entry(monty3, textvariable=fcm, width=8, justify='left', highlightbackground=bg_color, background=bg_color).grid(
    column=1, row=16, sticky='NW')

labelUnit8 = tk.Label(monty3, text="bts/min", anchor='w', width=8, justify='right', background=bg_color)
labelUnit8.grid(column=1, row=16)

ttk.Separator(monty3, orient='horizontal').grid(row=17, columnspan=3, sticky="ew")

# #Bouton Exercice induit angor
labelText9 = tk.StringVar()
labelText9.set("Angine induite par l'effort :")
ttk.Label(monty3, textvariable=labelText9, justify='left', background=bg_color).grid(column=0, row=18)

exerciseangina = tk.StringVar()
exerciseangina.set("1.0")
tk.Radiobutton(monty3, text="Oui", variable=exerciseangina, value='1.0', justify='left', background=bg_color).grid(
    column=1, row=18, sticky='NW')
tk.Radiobutton(monty3, text="Non", variable=exerciseangina, value='0.0', justify='left', background=bg_color).grid(
    column=2, row=18, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=19, columnspan=3, sticky="ew")

# TextBox ST depression induced by exercise relative to test
labelText10 = tk.StringVar()
labelText10.set("Sous-décalage du \nby segment S-T :")
ttk.Label(monty3, width=20, textvariable=labelText10, justify='left', background=bg_color).grid(column=0, row=20,
                                                                                                 rowspan=1)

st_depression = tk.DoubleVar()
tk.Entry(monty3, textvariable=st_depression, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=20, sticky='W')

labelUnit10 = tk.Label(monty3, text="mV", anchor='w', width=8, justify='right', background=bg_color)
labelUnit10.grid(column=1, row=20)

ttk.Separator(monty3, orient='horizontal').grid(row=21, columnspan=3, sticky="ew")

# Bouton Slope of the peak exercise ST segment
labelText11 = tk.StringVar()
labelText11.set("Pente au sommet \ndu segment S-T \npendant l'effort :")
ttk.Label(monty3, textvariable=labelText11, justify='left', background=bg_color).grid(column=0, row=22, rowspan=2)

peakexercise = tk.StringVar()
peakexercise.set('1.0')

tk.Radiobutton(monty3, text="Ascendante", variable=peakexercise, value='1.0', justify='left',
               background=bg_color).grid(column=1, row=22, sticky='W')
tk.Radiobutton(monty3, text="Plate", variable=peakexercise, value='2.0', justify='left', background=bg_color).grid(
    column=1, row=23, sticky='W')
tk.Radiobutton(monty3, text="Descendante", variable=peakexercise, value='3.0', justify='left',
               background=bg_color).grid(column=1, row=24, sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=25, columnspan=3, sticky="ew")

# Bouton Nombre de vaisseaux
labelText12 = tk.StringVar()
labelText12.set("Nombre de vaisseaux \nprincipaux colorés par \nfluoroscopie/radioscopie :")
ttk.Label(monty3, textvariable=labelText12, justify='left').grid(column=0, row=26, rowspan =2)
nb_vessels = tk.StringVar()
nb_vessels.set("0.0")
tk.Radiobutton(monty3, text="0", variable=nb_vessels, value='0.0', justify='left', background=bg_color).grid(column=1,
                                                                                                              row=26,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="1", variable=nb_vessels, value='1.0', justify='left', background=bg_color).grid(column=2,
                                                                                                              row=26,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="2", variable=nb_vessels, value='2.0', justify='left', background=bg_color).grid(column=1,
                                                                                                              row=27,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="3", variable=nb_vessels, value='3.0', justify='left', background=bg_color).grid(column=2,
                                                                                                              row=27,
                                                                                                              sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=28, columnspan=3, sticky="ew")

# Bouton Thallium Heart Scan
labelText13 = tk.StringVar()
labelText13.set("Examen du coeur au Thallium :")
ttk.Label(monty3, textvariable=labelText13, justify='left').grid(column=0, row=29)
tha_heartscan = tk.StringVar()
tha_heartscan.set('3.0')
tk.Radiobutton(monty3, text="Normal", variable=tha_heartscan, value='3.0', justify='left', background=bg_color).grid(
    column=1, row=29, sticky='W')
tk.Radiobutton(monty3, text="Malformation réversible", variable=tha_heartscan, value='7.0', justify='left',
               background=bg_color).grid(column=1, row=30, sticky='W')
tk.Radiobutton(monty3, text="Malformation irréversible", variable=tha_heartscan, value='6.0', justify='left',
               background=bg_color).grid(column=1, row=31, sticky='W')

ttk.Separator(monty3, orient='vertical').grid(column=4, rowspan=32, sticky="ns")


##Fonctions de remplissage de patient type
def setValPatient1():
    """change toutes les valeurs des inputs avec celles d'un patient du dataset :
     malade type 3 """
    age.set(62.0)
    sex.set("0.0")
    chestPain.set("4.0")
    pression_sang.set(140.0)
    chol_sterique.set(268.0)
    glycemie.set(0.0)
    ecgresult.set("2.0")
    fcm.set(160.0)
    exerciseangina.set("0.0")
    st_depression.set(3.6)
    peakexercise.set("3.0")
    nb_vessels.set("2.0")
    tha_heartscan.set("3.0")


def setValPatient2():
    """change toutes les valeurs des inputs avec celles d'un patient du dataset :
     sain type 0 """
    age.set(44.0)
    sex.set("1.0")
    chestPain.set("2.0")
    pression_sang.set(120.0)
    chol_sterique.set(263.0)
    glycemie.set(0.0)
    ecgresult.set("0.0")
    fcm.set(173.0)
    exerciseangina.set("0.0")
    st_depression.set(0.0)
    peakexercise.set("1.0")
    nb_vessels.set("0.0")
    tha_heartscan.set("7.0")


def setValPatient3():
    """change toutes les valeurs des inputs avec celles d'un patient du dataset :
     malade type 1 """
    age.set(67.0)
    sex.set("1.0")
    chestPain.set("4.0")
    pression_sang.set(120.0)
    chol_sterique.set(229.0)
    glycemie.set(0.0)
    ecgresult.set("2.0")
    fcm.set(129.0)
    exerciseangina.set("1.0")
    st_depression.set(2.6)
    peakexercise.set("2.0")
    nb_vessels.set("2.0")
    tha_heartscan.set("7.0")


def setValPatient4():
    """change toutes les valeurs des inputs avec celles d'un patient du dataset :
         malade type 2 """
    age.set(60.0)
    sex.set("1.0")
    chestPain.set("4.0")
    pression_sang.set(117.0)
    chol_sterique.set(230.0)
    glycemie.set(1.0)
    ecgresult.set("0.0")
    fcm.set(160.0)
    exerciseangina.set("1.0")
    st_depression.set(1.4)
    peakexercise.set("1.0")
    nb_vessels.set("2.0")
    tha_heartscan.set("7.0")


###Fonctions de transtypage
# TODO Améliorer les fonctions de transtypage en vérifiant la petinence des valeurs
def ageProcessor(age):
    age_p = str(age.get())
    return age_p


def pression_sangProcessor(pression_sang):
    pression_sang_p = str(pression_sang.get())
    return pression_sang_p


def chol_steriqueProcessor(chol_sterique):
    chol_sterique_p = str(chol_sterique.get())
    return chol_sterique_p

def glycemieProcessor(glycemie):
    glycemie_p = str(glycemie.get())
    return glycemie_p


def fcmProcessor(fcm):
    fcm_p = str(fcm.get())
    return fcm_p


def st_depressionProcessor(st_depression):
    st_depression_p = str(st_depression.get())
    return st_depression_p


def dataPreprocessor(age, sex, chestPain, pression_sang, chol_sterique, glycemie, ecgresult, fcm, exerciseangina,
                     st_depression, peakexercise, nb_vessels, tha_heartscan):
    # Transtype toutes les données et les mets en forme pour le modèle de prediction
    processed_vars = []
    processed_vars.append(ageProcessor(age))
    processed_vars.append(sex.get())
    processed_vars.append(chestPain.get())
    processed_vars.append(pression_sangProcessor(pression_sang))
    processed_vars.append(chol_steriqueProcessor(chol_sterique))
    processed_vars.append(glycemieProcessor(glycemie))
    processed_vars.append(ecgresult.get())
    processed_vars.append(fcmProcessor(fcm))
    processed_vars.append(exerciseangina.get())
    processed_vars.append(st_depressionProcessor(st_depression))
    processed_vars.append(peakexercise.get())
    processed_vars.append(nb_vessels.get())
    processed_vars.append(tha_heartscan.get())

    data_string = ''
    c = 1
    for var in processed_vars:
        if c == 13:
            data_string += var
            print(var)
        else:
            data_string += var + ' '
            c += 1
    print(data_string)
    return data_string


def HeartAIModel(data_string, algo=0):
    "Fonction qui vérifie la pertinence des données"
    """Transtype les données du form puis 
    Appelle un algorithme de prédiction avec les données renseignées et renvoie son résultat """
    print(data_string)
    if algo == 0:
        from HeartAI import main
        output = main(data_string)
    return output


def predict():
    # FIXME verifier qu'aucune valeur n'est vide normalement
    # FIXME QUICKFIX initialiser toutes les variables mais ca n'empeche pas de supprimer les variables récupérées dans des Entry
    data_string = dataPreprocessor(age, sex, chestPain, pression_sang, chol_sterique, glycemie, ecgresult, fcm,
                                   exerciseangina, st_depression, peakexercise, nb_vessels, tha_heartscan)
    output = HeartAIModel(data_string)
    print(output)
    #prediction.set(output)  #je trouve que la boite de dialogue est pas mal
    #mBox.showinfo("Prédiction de l'angiographie", output)
    output_mBox=output+ "\n \n Valider le résultat ?"
    #FIXME pas possible de choisir les libellés, il faudrait créer une box soit même
    mBox.askquestion("Prédiction de l'angiographie", output_mBox, default='yes')


labelText14 = tk.StringVar()
labelText14.set("Patients de test :")
text14 = ttk.Label(monty3, width=25, textvariable=labelText14, background=bg_color, anchor='center')
text14.grid(column=6, row=0, sticky="EW", columnspan=4)

action1 = ttk.Button(monty3, text="Patient Type 1", width=20, command=setValPatient1)
action1.grid(column=6, row=2, columnspan=2)

action2 = ttk.Button(monty3, text="Patient Type 2", width=20, command=setValPatient2)
action2.grid(column=8, row=2, columnspan=2)

action3 = ttk.Button(monty3, text="Patient Type 3", width=20, command=setValPatient3)
action3.grid(column=6, row=4, columnspan=2)

action4 = ttk.Button(monty3, text="Patient Type 4", width=20, command=setValPatient4)
action4.grid(column=8, row=4, columnspan=2)

labelText15 = tk.StringVar()
labelText15.set("Prédiction du résultat de l'angiographie :")
text15 = ttk.Label(monty3, width=25, textvariable=labelText15, background=bg_color, anchor='center')
text15.grid(column=6, row=5, sticky="EW", columnspan=4)

s = ttk.Style().configure("cta.TButton", foreground='#562742', font=('Sans', '12', 'bold'))
action3 = ttk.Button(monty3, text="Tenter la prédiction", width=40, command=predict, style="cta.TButton")
action3.grid(column=6, row=6, rowspan=1, columnspan=4, sticky="EW")

# prediction = tk.StringVar()
# prediction.set(art)
# text16 = ttk.Label(monty3, width=40, textvariable=prediction, background=bg_color, anchor='w', justify='left')
# text16.grid(column=6, row=7, sticky="EW", columnspan=4, rowspan=7)


# ---------------Example 3 End------------------#


# ----------------menu-------------------#
# Exit GUI
def _quit():
    win.quit()
    win.destroy()
    exit()


# creation menubar
menuBar = Menu(win)
win.config(menu=menuBar)

# ajouter des items dans un menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Creer")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="Fichier", menu=fileMenu)


# Montrer un message
def _msgBox1():
    mBox.showinfo('Python Message Info Box', 'Programme marche')


def _msgBox2():
    mBox.showwarning('Python Message Warning Box', 'Alert:')


def _msgBox3():
    mBox.showwarning('Python Message Error Box', 'Erreur')


def _msgBox4():
    answer = mBox.askyesno("Python Message Dual Choice Box", "V/F?")
    if answer == True:
        mBox.showinfo('choix effectue', 'Vous avez choisit "oui"')
    else:
        mBox.showinfo('choix effectue', 'VOus avez choisit "non"')

        # Ajouter un autre menu


msgMenu = Menu(menuBar, tearoff=0)
msgMenu.add_command(label="notification Box", command=_msgBox1)
msgMenu.add_command(label="warning Box", command=_msgBox2)
msgMenu.add_command(label="error Box", command=_msgBox3)
msgMenu.add_separator()
msgMenu.add_command(label="vrai ou faux", command=_msgBox4)
menuBar.add_cascade(label="message", menu=msgMenu)
# ----------------菜单栏介绍-------------------#

# ======================
# Start GUI  
# ======================
win.mainloop()  
