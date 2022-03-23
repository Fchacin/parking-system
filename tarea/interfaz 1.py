from tkinter import *
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

   

def AgregarReserva():
       
        global count
        
        if nameE.get() == "" or carE.get() == "" or modelE.get() == "":
    
            messagebox.showinfo(message="Por favor rellene todos los campos", title="Error")

        else:
            info.insert(parent='',index='end', iid=count, text="", values=(nameE.get(), carE.get(), modelE.get()))
             
            count += 1

            nameE.delete(0,END)
            carE.delete(0,END)
            modelE.delete(0,END)

            

root = Tk()

root.geometry("800x600")

root.iconbitmap("volante.ico")

root.config(bg="silver")

root.title("Parking System")

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

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

info = ttk.Treeview(root)
info["columns"]=("Nombre y Apellido","Auto","Modelo")
info.column("#0", width=0, stretch=NO)
info.column("Nombre y Apellido", anchor=CENTER, width=180)
info.column("Auto", anchor=CENTER, width=80)
info.column("Modelo", anchor=CENTER, width=80)

info.heading("#0", text="", anchor=CENTER)
info.heading("Nombre y Apellido", text="Nombre y Apellido", anchor=CENTER)
info.heading("Auto", text="Auto", anchor=CENTER)
info.heading("Modelo", text="Modelo", anchor=CENTER)
info.pack()

addbtn = ttk.Button(root ,text="Reservar estacionamiento", command=abrirform)

addbtn.place(x=340,y=175)

regiForm = tk.Toplevel()
regiForm.geometry("500x500")
regiForm.withdraw()
    
label_0 =Label(regiForm,text="Formulario de Reserva", width=20,font=("bold",20))
label_0.place(x=90,y=60)
    
name = Label(regiForm ,text = "Nombre y Apellido", width=20,font=("bold",10))
name.place(x=80,y=130)
car = Label(regiForm ,text = "Auto", width=20,font=("bold",10))
car.place(x= 80,y=180)
    
model = Label(regiForm ,text = "Modelo",  width=20,font=("bold",10))
model.place(x=80,y=220)
   
nameE = Entry(regiForm)
nameE.place(x=240,y=130)
carE = Entry(regiForm)
carE.place(x=240,y=180)   
modelE = Entry(regiForm)
modelE.place(x=240,y=220)
tempname = nameE.get()

btnReserva = Button(regiForm, text='Reservar' ,width=20,bg="black",fg='white', command=AgregarReserva)
btnReserva.place(x=180,y=380)

root.mainloop()
