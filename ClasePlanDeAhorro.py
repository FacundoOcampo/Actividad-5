class PlanDeAhorro:
    CanPlanT=None
    CanPlanL=None
    def __init__(self,CodPlan,Modelo,VerVei,ValVei):
        self.__CodPLan=CodPlan
        self.__Modelo=Modelo
        self.__VerVei=VerVei
        self.__ValVei=ValVei
    def __str__(self):
        return "{} {} {}".format(self.__CodPLan,self.__Modelo,self.__VerVei)
    def GetVal(self):
        return self.__ValVei
    def NuevoPrecio(self,Num):
        self.__ValVei=Num
    def GetCod(self):
        return self.__CodPLan
