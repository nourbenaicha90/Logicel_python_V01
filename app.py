from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector

# MySQL Database Configuration
host = 'localhost'
user = 'root'
password = 'nour'
database = 'hopital'

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connected to MySQL Database!")

except mysql.connector.Error as error:
    print("Error connecting to MySQL Database:", error)

if connection.is_connected():
    cursor = connection.cursor()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  ajouter
def ajouter():
    matricule = entrermatricule.get()
    nom = entrernom.get()
    prenom = entrerPrenom.get()
    age = entrerage.get()
    adresse = entreradresse.get()
    telephone = entrertelephone.get()
    remarque = entrerremarque.get()

    # Create the connection
    try:
        cursor.execute("INSERT INTO patient(code, nom, prenom, age, adresse, telephone, remarque) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (matricule, nom, prenom, age, adresse, telephone, remarque))
        connection.commit()
        messagebox.showinfo("Patient ajouté")

    except mysql.connector.Error as error:
        print("Error inserting data:", error)
    refresh_table()

# modifier
def modifier():
    matricule = entrermatricule.get()
    nom = entrernom.get()
    prenom = entrerPrenom.get()
    age = entrerage.get()
    adresse = entreradresse.get()
    telephone = entrertelephone.get()
    remarque = entrerremarque.get()

   
    try:
        cursor.execute("UPDATE patient SET nom=%s, prenom=%s, age=%s, adresse=%s, telephone=%s, remarque=%s WHERE code=%s",
            (nom, prenom, age, adresse, telephone, remarque, matricule))
        connection.commit()
        messagebox.showinfo("Patient Modifié")
    except mysql.connector.Error as error:
        print("Error updating data:", error)
    refresh_table()

#_____________________________________________________________________________________________ supprimer
def supprimer():
    codeSelectionner = table.item(table.selection())['values'][0]

    # Delete the data
    try:
        cursor.execute("DELETE FROM patient WHERE code=%s", (codeSelectionner,))
        connection.commit()
        table.delete(table.selection())
        messagebox.showinfo("Patient Supprimé")

    except mysql.connector.Error as error:
        print("Error deleting data:", error)

#_____________________________________________________________________________________________  refresh_table
def refresh_table():
    # Clear the table
    table.delete(*table.get_children())

    # Fetch data from MySQL and populate the table
    try:
        cursor.execute("SELECT * FROM patient")
        rows = cursor.fetchall()

        for row in rows:
            table.insert('', END, values=row)

    except mysql.connector.Error as error:
        print("Error fetching data:", error)


#titre general
root = Tk()
root.title("Gestion des patient ")
root.geometry("1365x700")

# ... Rest of the GUI code ...
#Ajouter le titre
lbltitre = Label(root,bd = 20, relief = RIDGE, text = "GESTION DES PATIENTS CHEZ JBDEVHOPITAL95", font = ("Arial", 30), bg = "darkblue", fg="white")
lbltitre.place(x = 0, y = 0, width = 1365)

#Liste des patients
lblListePatient = Label(root, text = "LISTES DES PATIENTS ", font = ("Arial", 16), bg = "darkblue", fg="white")
lblListePatient.place(x=600,y=100,width=760)



#text matricule
lblmatricule = Label(root, text = "Matricule Patient", font = ("Arial", 16), bg = "black", fg="white")
lblmatricule.place(x=0,y=100,width=200)
entrermatricule = Entry(root)
entrermatricule.place(x=200,y=100,width=160,height=30)

#text nom
lblnom = Label(root, text = "Nom Patient", font = ("Arial", 16), bg = "black", fg="white")
lblnom.place(x=0,y=150,width=200)
entrernom = Entry(root)
entrernom.place(x=200,y=150,width=200,height=30)

#text prenom
lblPrenom = Label(root, text = "Prenom Patient", font = ("Arial", 16), bg = "black", fg="white")
lblPrenom.place(x=0,y=200,width=200)
entrerPrenom = Entry(root)
entrerPrenom.place(x=200,y=200,width=200,height=30)

#text age
lblage = Label(root, text = "Age Patient", font = ("Arial", 16), bg = "black", fg="white")
lblage.place(x=0,y=250,width=200)
entrerage = Entry(root)
entrerage.place(x=200,y=250,width=100,height=30)

#text adresse
lbladresse = Label(root, text = "Adresse Patient", font = ("Arial", 16), bg = "black", fg="white")
lbladresse.place(x=0,y=300,width=200)
entreradresse = Entry(root)
entreradresse.place(x=200,y=300,width="300",height=30)

#text Telephone
lbltelephone = Label(root, text = "Telephone Patient", font = ("Arial", 16), bg = "black", fg="white")
lbltelephone.place(x=0,y=350,width=200)
entrertelephone = Entry(root)
entrertelephone.place(x=200,y=350,width=200,height=30)

#text remarque
lblremarque = Label(root, text = "Remarque Patient", font = ("Arial", 16), bg = "black", fg="white")
lblremarque.place(x=0,y=400,width=200)
entrerremarque = Entry(root)
entrerremarque.place(x=200,y=400,width=300,height=30)


#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = ajouter)
btnenregistrer.place(x=30, y= 450, width=200)

#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = modifier)
btnmodofier.place(x=270, y= 450, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = supprimer)
btnSupprimer.place(x=150, y= 500, width=200)



# Define the 'table' variable globally
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7), height=5, show="headings")
table.place(x=600, y=150, width=760, height=450)

#Entete
table.heading(1 , text = "CODE")
table.heading(2 , text = "NOM")
table.heading(3 , text = "PRENOM")
table.heading(4 , text = "AGE")
table.heading(5 , text = "ADRESSE")
table.heading(6 , text = "TELEPHONE")
table.heading(7 , text = "REMARQUE")

#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)
table.column(3,width = 150)
table.column(4,width = 50)
table.column(5,width = 150)
table.column(6,width = 100)
table.column(7,width = 150)


def on_select(event):
    selected_item = table.focus()
    if selected_item:
        values = table.item(selected_item, 'values')
        entrermatricule.delete(0, END)
        entrermatricule.insert(0, values[0])

        entrernom.delete(0, END)
        entrernom.insert(0, values[1])

        entrerPrenom.delete(0, END)
        entrerPrenom.insert(0, values[2])

        entrerage.delete(0, END)
        entrerage.insert(0, values[3])

        entreradresse.delete(0, END)
        entreradresse.insert(0, values[4])

        entrertelephone.delete(0, END)
        entrertelephone.insert(0, values[5])

        entrerremarque.delete(0, END)
        entrerremarque.insert(0, values[6])
table.bind("<<TreeviewSelect>>", on_select)

# Display the initial data in the table
refresh_table()

root.mainloop()
