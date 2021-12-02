
from tkinter import *
import tkinter as tk
from tkinter.ttk import *


from pandas.core import frame
import estadisticas

class datosGUI():
    
    def __init__(self,nombre,pokePoder,pokeNombre,pokeAtaque,pokeDefensa,pokeVida,rt):
        
        self.titulo = nombre
        ventana = Toplevel()
        ventana.title(self.titulo)
        
        # Primer Frame
        panel1 = tk.LabelFrame(ventana)
        # Canvas
        canvas = tk.Canvas(panel1, bg="white")
        canvas.pack(side="top", fill="x", expand="yes")
        # Ventanas dentro del frame
        frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=frame, anchor=NW)
        panel1.pack(fill="both", expand="yes", padx=0, pady=0)

        # Ver Boton
        # image Pokemon 1
        #****************************************************************************************************************
        ruta = ['./pokeicons/pikachu.png','./pokeicons/pikachus.png','./pokeicons/pikachuss.png']
        
        #ruta2 = []
        #ruta2.append(tk.PhotoImage(file=ruta[0]).zoom(3))
        frm_test = tk.Frame(canvas, padx=1, pady=1)
        frm_test.grid(row=0, column=0)
        TipoRutas = "./pokemonTipos/"+rt;
        img = tk.PhotoImage(file = TipoRutas).subsample(2)
        print(TipoRutas)
        tk.Label(master=frm_test,image=img, relief="groove",bg="white").pack(fill=BOTH)
        Label(master=frm_test,text=self.titulo).pack(fill=X)
        frm_test = tk.Frame(canvas, padx=1, pady=1)
        frm_test.grid(row=0, column=1)
       
        
        rutasImg = []
        for i in range(3):
            rutaImagen = "./pokeicons/"+str(pokeNombre.iloc[i]).lower()+".png"
            rutasImg.append(tk.PhotoImage(file = rutaImagen).zoom(2))


        ImgTipo = tk.Label(frm_test,width=50,height=5,text="Top 3 los mejores Pokemon",font=("Arial", 15),bg="white",fg="black").pack(fill=BOTH)
        print(pokeNombre.iloc[0])
        for i in range(3):
            frm_test = tk.Frame(canvas, padx=2, pady=2)
            frm_test.grid(row=i+1, column=0)
            
            #Agrega las Imagenes
            try:    
                tk.Button(master=frm_test,image=rutasImg[i], relief="flat",bg="white").pack(fill=BOTH)
                tk.Label(master=frm_test,text=pokeNombre.iloc[i]).pack(fill=BOTH)
            except:
                tk.Label(master=frm_test, text="Icon No Found", bg="white",relief=FLAT).pack()
            # Estadisticas pokemones
            #ATAQUE
            frm_test = tk.Frame(canvas, padx=1, pady=1,bg="white")
            frm_test.grid(row=i+1, column=1, pady=10, padx=10)
            pokeA = "Ataque: "+str(pokeAtaque.iloc[i])+" %"
            #BARRA ATAQUE
            tk.Label(master=frm_test, text=pokeA,bg="white", fg="black").pack()
            barra = Progressbar(master=frm_test, orient=HORIZONTAL,value=pokeAtaque.iloc[i], length=500, mode='determinate')
            barra.pack(expand=True,fill=X)
            #DEFENSA
            pokeV = "Defensa: "+str(pokeDefensa.iloc[i])+" %"
            tk.Label(master=frm_test, text=pokeV,
                    bg="white", fg="black").pack()
            #BARRA DEFENSA
            barra = Progressbar(master=frm_test, orient=HORIZONTAL,value=pokeDefensa.iloc[i], length=500, mode='determinate')
            barra.pack(expand=True,fill=X)
            #VIDA
            pokeS = "Salud: "+str(pokeVida.iloc[i])+" %"
            tk.Label(master=frm_test, text=pokeS,
                    bg="white", fg="black").pack()
            #BARRA VIDA
            barra = Progressbar(master=frm_test, orient=HORIZONTAL,value=pokeVida.iloc[i], length=500, mode='determinate')
            barra.pack(expand=True,fill=X)
            #PODER TOTAL
            pokeT = "PODER TOTAL "+str(pokePoder.iloc[i])+" %"
            poderPorcent = int(pokePoder.iloc[i])*0.100
            tk.Label(master=frm_test, text=pokeT,bg="white", fg="black",width=40).pack()
            #BARRA PODER TOTAL
            barra = Progressbar(master=frm_test, orient=HORIZONTAL,value=poderPorcent, length=100, mode='determinate')
            barra.pack(expand=True,fill=X)
        ventana.resizable(False,False)
        ventana.mainloop()
        #****************************************************************************************************************
        
        

class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        Texto_Menu = "Tahoma"
        #panel = Tk()
        self.title("PokeDex Estadisticas")
        #panel.geometry("900x800")
        logo = tk.PhotoImage(file='iconPoke.png')
        self.tk.call('wm','iconphoto', self._w, logo)
        
        contenedorRoot = tk.Frame(master=self, width=900, height=800,bg="white")

        def verEstadisticas(tipoPokemon,tipoIconD):
            nombre = tipoPokemon
            print("Tipo de pokemon: ",nombre)
            poder = estadisticas.Stack(tipoPokemon)
            print("[TABLA DE PODER DE]: ", nombre)
            print(poder.poder)
            print("[TABLA DE NOMBRES DE]: ", nombre)
            print(poder.nombre)
            print("[TABLA DE ATAQUES DE]: ", nombre)
            print(poder.ataque)
           
            print("[TABLA DE DEFENSA DE]:", nombre)
            print(poder.defensa)
            print("[TABLA DE SALUD DE]:", nombre)
            print(poder.salud)
            nuevo = datosGUI(nombre,poder.poder,poder.nombre,poder.ataque,poder.defensa,poder.salud,tipoIconD)  
            

        #Titulo panel
        panelTitulo = tk.Frame(master=contenedorRoot,width=900, height=200)
        frm_panelTipos = tk.Frame(master=contenedorRoot, width=900,height=200, background="white")


        img_logo = tk.PhotoImage(file = 'iconApp.png').subsample(4)
        label_img = tk.Label(panelTitulo, image = img_logo,bg="white").pack()

        #Botones de lo tipos de pokemon
        #Bug
        frame = tk.Frame(master=frm_panelTipos, relief=tk.FLAT)
        frame.grid(row=0, column=0, padx=20, pady=30)
        img_bug = tk.PhotoImage(file = './pokemonTipos/Type_Bicho.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_bug,relief=FLAT,bg="white",command=lambda: verEstadisticas("Bug","Type_Bicho.png")).pack()
        nombre = tk.Label(master=frame,text="Insecto",pady=1).pack()

        #Dark
        frame = tk.Frame(master=frm_panelTipos, relief=tk.FLAT )
        frame.grid(row=0, column=1, padx=20, pady=30)
        img_dark = tk.PhotoImage(file = './pokemonTipos/Type_Acero.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_dark,relief=FLAT,bg="white",command=lambda: verEstadisticas("Dark","Type_Acero.png")).pack()
        nombre_2 = tk.Label(master=frame,text="Acero",pady=1).pack()
        #Dragon
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=0, column=2, padx=20, pady=30)
        img_dragon = tk.PhotoImage(file = './pokemonTipos/Type_Dragon.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_dragon,relief=FLAT,bg="white",command=lambda: verEstadisticas("Dragon","Type_Dragon.png")).pack()
        nombre_3 = tk.Label(master=frame,text="Dragon",pady=1).pack()
        #Electric
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=0, column=3, padx=20, pady=30)
        img_Electric = tk.PhotoImage(file = './pokemonTipos/Type_Electrico.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_Electric,relief=FLAT,bg="white",command=lambda: verEstadisticas("Electric","Type_Electrico.png")).pack()
        nombre = tk.Label(master=frame,text="Electrico",pady=1).pack()
        #Fairy
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=0, column=4, padx=20, pady=30)
        img_fairy = tk.PhotoImage(file = './pokemonTipos/Type_Hada.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_fairy,relief=FLAT,bg="white",command=lambda: verEstadisticas("Fairy","Type_Hada.png")).pack()
        nombre = tk.Label(master=frame,text="Hada",pady=1).pack()
        #Fighting
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=0, column=5, padx=20, pady=30)
        img_fighting = tk.PhotoImage(file = './pokemonTipos/Type_Lucha.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_fighting,relief=FLAT,bg="white",command=lambda: verEstadisticas("Fighting","Type_Lucha.png")).pack()
        nombre = tk.Label(master=frame,text="Lucha",pady=1).pack()
        #Fire
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED)
        frame.grid(row=1, column=0, padx=20, pady=30)
        img_Fire = tk.PhotoImage(file = './pokemonTipos/Type_Fuego.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_Fire,relief=FLAT,bg="white",command=lambda: verEstadisticas("Fire","Type_Fuego.png")).pack()
        nombre = tk.Label(master=frame,text="Fuego",pady=1).pack()
        #Flying
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=1, column=1, padx=20, pady=30)
        img_flying = tk.PhotoImage(file = './pokemonTipos/Type_Volador.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_flying,relief=FLAT,bg="white",command=lambda: verEstadisticas("Flying","Type_Volador.png")).pack()
        nombre = tk.Label(master=frame,text="Volador",pady=1).pack()
        #Ghost
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=1, column=2, padx=20, pady=30)
        img_ghost = tk.PhotoImage(file = './pokemonTipos/Type_Fantasma.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_ghost,relief=FLAT,bg="white",command=lambda: verEstadisticas("Ghost","Type_Fantasma.png")).pack()
        nombre = tk.Label(master=frame,text="Fanstasma",pady=1).pack()
        #Grass
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=1, column=3, padx=20, pady=30)
        img_grass = tk.PhotoImage(file = './pokemonTipos/Type_Planta.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_grass,relief=FLAT,bg="white",command=lambda: verEstadisticas("Grass","Type_Planta.png")).pack()
        nombre = tk.Label(master=frame,text="Planta",pady=1).pack()
        #Ground
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=1, column=4, padx=20, pady=30)
        img_ground = tk.PhotoImage(file = './pokemonTipos/Type_Tierra.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_ground,relief=FLAT,bg="white",command=lambda: verEstadisticas("Ground","Type_Tierra.png")).pack()
        nombre = tk.Label(master=frame,text="Tierra",pady=1).pack()
        #ice
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=1, column=5, padx=20, pady=30)
        img_ice = tk.PhotoImage(file = './pokemonTipos/Type_Hielo.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_ice,relief=FLAT,bg="white",command=lambda: verEstadisticas("Ice","Type_Hielo.png")).pack()
        nombre = tk.Label(master=frame,text="Hielo",pady=1).pack()
        #normal
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=2, column=0, padx=20, pady=30)
        img_normal = tk.PhotoImage(file = './pokemonTipos/Type_Normal.png')
        Boton = tk.Button(master=frame,text=f"Cuadro",image=img_normal,relief=FLAT,bg="white",command=lambda: verEstadisticas("Normal","Type_Normal.png")).pack()
        nombre = tk.Label(master=frame,text="Normal",pady=1).pack()
        #Poison
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=2, column=1, padx=20, pady=30)
        img_poison = tk.PhotoImage(file = './pokemonTipos/Type_Posion.png')
        Boton = tk.Button(master=frame, text=f"Cuadro",image=img_poison,relief=FLAT,bg="white",command=lambda: verEstadisticas("Poison","Type_Posion.png")).pack()
        nombre = tk.Label(master=frame,text="Posion",pady=1).pack()
        #psychic
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=2, column=2, padx=20, pady=30)
        img_psychic = tk.PhotoImage(file = './pokemonTipos/Type_Psiquico.png')
        Boton = tk.Button(master=frame, text=f"Cuadro",image=img_psychic,relief=FLAT,bg="white",command=lambda: verEstadisticas("Psychic","Type_Psiquico.png")).pack()
        nombre = tk.Label(master=frame,text="Psiquico",pady=1).pack()
        #rock
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=2, column=3, padx=20, pady=30)
        img_rock = tk.PhotoImage(file = './pokemonTipos/Type_Roca.png')
        Boton = tk.Button(master=frame, text=f"Cuadro",image=img_rock,relief=FLAT,bg="white",command=lambda: verEstadisticas("Rock","Type_Roca.png")).pack()
        nombre = tk.Label(master=frame,text="Roca",pady=1).pack()
        #stell
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED )
        frame.grid(row=2, column=4, padx=20, pady=30)
        img_stell = tk.PhotoImage(file = './pokemonTipos/Type_Siniestro.png')
        Boton = tk.Button(master=frame, text=f"Cuadro",image=img_stell,relief=FLAT,bg="white",command=lambda: verEstadisticas("Steel","Type_Siniestro.png")).pack()
        nombre = tk.Label(master=frame,text="Siniestro",pady=1).pack()
        #Water
        frame = tk.Frame(master=frm_panelTipos, relief=tk.RAISED)
        frame.grid(row=2, column=5, padx=20, pady=30)
        img_water = tk.PhotoImage(file = './pokemonTipos/Type_Agua.png')
        Boton = tk.Button(master=frame, text=f"Cuadro",image=img_water,relief=FLAT,bg="white",command=lambda: verEstadisticas("Water","Type_Agua.png")).pack()
        nombre = tk.Label(master=frame,text="Agua",pady=1).pack()

        contenedorRoot.pack()
        panelTitulo.pack()
        frm_panelTipos.pack(fill=Y)
        self.resizable(False, False)
        self.mainloop()
        
            
iniciar = GUI()

