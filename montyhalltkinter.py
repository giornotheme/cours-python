from tkinter import * 

fenetre = Tk()

fenetre['bg']='white'

# button 1
button1 = Button(fenetre, borderwidth=2, relief=GROOVE)
button1.pack(side=LEFT)

# button 2
button2 = Button(fenetre, borderwidth=2, relief=GROOVE)
button2.pack(side=LEFT)

# button 3
button3 = Button(fenetre, borderwidth=2, relief=GROOVE)
button3.pack(side=RIGHT)

# Ajout de labels
Label(button1, text="Boite 1").pack(padx=10, pady=10)
Label(button2, text="Boite 2").pack(padx=10, pady=10)
Label(button3, text="Boite 3",bg="white").pack(padx=10, pady=10)

fenetre.mainloop()