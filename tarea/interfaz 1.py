from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

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

root = Tk()

root.geometry("800x600")

root.iconbitmap("volante.ico")

root.config(bg="silver")

root.title("Parking System")

menubar = Menu(root)
root.config(menu=menubar)

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

root.mainloop()