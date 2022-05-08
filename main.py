from Clase_menu import Menu
from Clase_manejador import Manejador

if __name__ == '__main__':
    Archivo=open("Planes.csv","r")
    NuevoMenu=Menu()
    NuevoManejador=Manejador()
    NuevoManejador.CargarLista(Archivo)
    bandera=False
    while(bandera!=True):
        Num=int(input("------------Seleccione una opcion:------------\n1_Actualizar el valor del vehículo\n2_Mostrar informacion de un veiculo segun un valor dado\n3_Mostrar el monto que se debe haber pagado para licitar el vehículo\n4_Modificar la cantidad cuotas que debe tener pagas para licitar\n0_Salir\n----------------------------------------------\n"))
        NuevoMenu.Opciones(Num,Archivo,NuevoManejador)
        bandera = int(Num)==0
    Archivo.close()
