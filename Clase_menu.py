class Menu:
    __Switch=None
    def __init__(self):
        self.__Switch={
                1:self.Opcion1,
                2:self.Opcion2,
                3:self.Opcion3,
                4:self.Opcion4,
                0:self.Salir,
        }
    def Opciones(self,Op,Archivo,NuevoManejador):
        Func=self.__Switch.get(Op,lambda:print("Opción incorrecta,Ingrese una nuevamente"))
        if Op==1 or Op==2 or Op==3 or Op==4:
            Func(NuevoManejador)
        else:
            Func()
    def Opcion1(self,NuevoManejador):
        print("----------------------------------------------")
        NuevoManejador.ModificarPrecio()
    def Opcion2(self,NuevoManejador):
        print("----------------------------------------------")
        Num=int(input("Ingrese un precio"))
        NuevoManejador.MostrarLista(Num)
    def Opcion3(self,NuevoManejador):
        print("----------------------------------------------")
        NuevoManejador.CalcValor()
    def Opcion4(self,NuevoManejador):
        print("----------------------------------------------")
        Num=int(input("Ingrese un numero de plan"))
        NuevoManejador.ModCuo(Num)
        NuevoManejador.MostrarTodo()
    def Salir(self):
        print("----------------------------------------------")
        print("Se salio correctamente")
        print("----------------------------------------------")
