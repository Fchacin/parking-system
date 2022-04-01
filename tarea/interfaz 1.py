﻿from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import array as ar

def InfoAdicional():
    messagebox.showinfo("Acerca de nuestro proyecto","Nuestro proyecto esta desarrollado mediante software libre, no infrige derechos de autor ni copyright")

def InfoEquipo():
    messagebox.showwarning("Nosotros", "Este programa fue hecho en equipo")

def salirdelapp():
    valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?") 
    if valor=="yes":
       root.destroy() 

def Abrirarchivo():
    archivo=filedialog.askopenfilename(filetypes=(
        ("Ficheros en PDF","*.PDF"),
        ("Todos los ficheros","*.*")
    ), 
    title = "Abrir documento"
)     
    print(archivo)

def abrirform():
    
    regiForm.deiconify()


def salirdelform():
    revalor=messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?") 
    if revalor=="yes":
       regiForm.withdraw()
    else:
        regiForm.deiconify()

def AgregarReserva():
       
        global count
        
        if nameE.get() == "" or carE.get() == "" or modelE.get() == "":
    
            messagebox.showinfo(message="Por favor rellene todos los campos", title="Error")
            regiForm.deiconify()
            

        else:
            info.insert(parent='',index='end', iid=count, text="", values=(nameE.get(), carE.get(), modelE.get()))
             
            count += 1

            nameE.delete(0,END)
            carE.delete(0,END)
            modelE.delete(0,END)
            regiForm.withdraw()

            

root = Tk()

root.geometry("800x800")

root.iconbitmap("volante.ico")

root.config(bg="silver")

root.title("Parking System")

root.attributes('-fullscreen', True)

menubar = Menu(root)
root.config(menu=menubar)

global count

count = 0

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir documento", command=Abrirarchivo)
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=salirdelapp)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Nosotros", command=InfoEquipo)
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...", command=InfoAdicional)

resmenu = Menu(menubar, tearoff=0)
resmenu.add_command(label="Añadir Reserva", command=abrirform)
resmenu.add_command(label="Eliminar Reserva", command=Abrirarchivo)
resmenu.add_command(label="Modificar Reserva")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
menubar.add_cascade(label="Reservas", menu=resmenu)



info = ttk.Treeview(root,show='headings', height=20)
info["columns"]=("Cedula","Nombre y Apellido","Correo Electronico","Marca","Modelo","Color","Año","Placa","Puesto")
info.column("#0", width=0, stretch=NO)
info.column("Cedula", anchor=CENTER, width=80)
info.column("Nombre y Apellido", anchor=CENTER, width=180)
info.column("Correo Electronico", anchor=CENTER, width=180)
info.column("Marca", anchor=CENTER, width=80)
info.column("Modelo", anchor=CENTER, width=80)
info.column("Color", anchor=CENTER, width=80)
info.column("Año", anchor=CENTER, width=80)
info.column("Placa", anchor=CENTER, width=80)
info.column("Puesto", anchor=CENTER, width=80)

info.heading("#0", text="", anchor=CENTER)
info.heading("Cedula", text="Cedula", anchor=CENTER)
info.heading("Nombre y Apellido", text="Nombre y Apellido", anchor=CENTER)
info.heading("Correo Electronico", text="Correo Electronico", anchor=CENTER)
info.heading("Marca", text="Marca", anchor=CENTER)
info.heading("Modelo", text="Modelo", anchor=CENTER)
info.heading("Color", text="Color", anchor=CENTER)
info.heading("Año", text="Año", anchor=CENTER)
info.heading("Placa", text="Placa", anchor=CENTER)
info.heading("Puesto", text="Puesto", anchor=CENTER)
info.pack()

regiForm = tk.Toplevel()
regiForm.geometry("500x500")
regiForm.attributes('-fullscreen', True)
regiForm.withdraw()

regimenubar = Menu(regiForm)
regiForm.config(menu=regimenubar)

global rescount

rescount = 0

operamenu = Menu(regimenubar, tearoff=0)
operamenu.add_command(label="Limpiar")
operamenu.add_command(label="Salir", command=salirdelform)


regimenubar.add_cascade(label="Menu", menu=operamenu)

    
label_0 =Label(regiForm,text="Formulario de Reserva", width=25,font=("bold",20))
label_0.place(x=500,y=60)
    
Id = Label(regiForm ,text = "Cedula", width=20,font=("bold",10))
Id.place(x=240,y=137)

name = Label(regiForm ,text = "Nombre", width=20,font=("bold",10))
name.place(x= 490,y=137)
    
mail = Label(regiForm ,text = "Correo",  width=20,font=("bold",10))
mail.place(x=750,y=137)

model = Label(regiForm ,text = "Marca",  width=20,font=("bold",10))
model.place(x=240,y=197)

model = Label(regiForm ,text = "Modelo",  width=20,font=("bold",10))
model.place(x=490,y=197)

color = Label(regiForm ,text = "Color",  width=20,font=("bold",10))
color.place(x=750,y=197)

year = Label(regiForm ,text = "Año",  width=20,font=("bold",10))
year.place(x=240,y=257)

carid = Label(regiForm ,text = "Placa",  width=20,font=("bold",10))
carid.place(x=490,y=257)

carplace = Label(regiForm ,text = "Puesto",  width=20,font=("bold",10))
carplace.place(x=750,y=257)
   
   
IdE = Entry(regiForm)
IdE.place(x=390,y=140)
nameE = Entry(regiForm)
nameE.place(x=620,y=140)   
mailE = Entry(regiForm)
mailE.place(x=890,y=140)
BrandBox = ttk.Combobox(regiForm,
                        state="readonly",
                        values=["Ford","Toyota","Chevrolet","Jeep","Mercedes-Benz","Ferrari","BMW","Lamborghini","Volkswagen","Nissan"])
BrandBox.place(x=390, y=197)

ModelE = Entry(regiForm)
ModelE.place(x=620,y=197)

ColorBox = ttk.Combobox(regiForm,
                        state="readonly",
                        values=["Rojo","Beige","Gris","Azul","Verde","Morado","Rosado","Blanco","Negro","Marron","Celeste","Amarillo","Naranja","Plateado","Dorado"])
ColorBox.place(x=890, y=197)

yearE = Entry(regiForm)
yearE.place(x=390,y=257)
caridE = Entry(regiForm)
caridE.place(x=620,y=257)

positBox = ttk.Combobox(regiForm,
                        state="readonly",
                        values=["A1","A2","A3","A4","A5","A6","B1","B2","B3","B4","B5","B6","C1","C2","C3"])
positBox.place(x=890, y=257)


btnReserva = Button(regiForm, text='Reservar' ,width=20,bg="dark blue",fg='white', command=AgregarReserva)
btnReserva.place(x=580,y=380)



root.mainloop()
