import csv
from ClasePlanDeAhorro import PlanDeAhorro

class Manejador:
    __Lista=[]
    def __init__(self):
        self.__Lista=[]
    def CargarLista(self,Archivo):
        Reader=csv.reader(Archivo,delimiter=";")
        for fila in Reader:
            Num=int(fila[0])
            Mod=fila[1]
            Ver=fila[2]
            Val=float(fila[3])
            CantT=int(fila[4])
            CantP=int(fila[5])
            NuevoPlan=PlanDeAhorro(Num,Mod,Ver,Val)
            PlanDeAhorro.CanPlanT=CantT
            PlanDeAhorro.CanPlanL=CantP
            self.__Lista.append(NuevoPlan)

    def ModificarPrecio(self):
        print("\nLista de autos:\n")
        for i in range(len(self.__Lista)):
            print("---------",self.__Lista[i],"---------")
            Num=float(input("Ingrese el nuevo Valor del veiculo\n"))
            self.__Lista[i].NuevoPrecio(Num)

    def MostrarLista(self,Num):
        for i in range(len(self.__Lista)):
            PlanTotal=PlanDeAhorro.CanPlanT
            aux=(self.__Lista[i].GetVal()/PlanTotal)+self.__Lista[i].GetVal()*0.10
            if(aux<Num):
                print(self.__Lista[i])

    def CalcValor(self):
        for i in range(len(self.__Lista)):
            aux=PlanDeAhorro.CanPlanT
            Valor=(self.__Lista[i].GetVal()/aux)+self.__Lista[i].GetVal()*0.10
            Total=Valor*PlanDeAhorro.CanPlanL
            print("             ",self.__Lista[i])
            print("Monto a pagar para licitar el veiculo: {:.2f}\n".format(Total))

    def ModCuo(self,Num):
        for i in range(len(self.__Lista)):
            aux=self.__Lista[i].GetCod()
            if Num == aux:
                NuevoL=int(input("Ingrese la nueva cantidad de cuotas a licitar"))
                PlanDeAhorro.CanPlanL=NuevoL

    def MostrarTodo(self):
        for i in range(len(self.__Lista)):
            print(self.__Lista[i])
            print(PlanDeAhorro.CanPlanL)
