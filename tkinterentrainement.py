from tkinter import*

#Config fenêtre :
fenetre = Tk()
fenetre.title("Fenêtre Ali")
fenetre.geometry("1920x1080")

#Config texte :
label = Label(fenetre, text="Test Mousmousa", font=("Arial", 40))
label.pack(pady=350)
#Barre de menus : 
barre = Menu(fenetre)
menu1 = Menu(barre, tearoff=0)


#Afficher la page :
fenetre.mainloop()

print("test github")