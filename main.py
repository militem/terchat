#-*- coding: utf-8 -*-
"""
    Programacion UPS
    Fecha: 15/07/2020
    TerChat (Red Social)
"""
#Modulo propio
import modules.main_modules as red
#Modulo para estilos por consola, Color, Color de fondo.
from colorama import init, Fore, Back, Style
#Modulo para contrasenias
import getpass
#Modulo para la optener hora, fecha
from datetime import datetime
#Funcion principal
def main():
    red.show_welcome()
    option = 1
    #Bucle principal para ingresar a la red social
    while option != 0:
        option = red.main_menu()
        if option == 1: 
            user = input(Fore.YELLOW+"\nUsuario: "+Fore.RESET)
            password = getpass.getpass(Fore.YELLOW+"Contraseña: "+Fore.RESET)
            auth = red.auth_users(user, password)
            if auth == True:
                print(Fore.GREEN+"\nHola! "+user+Fore.RESET)
                break
            else:
                print(Fore.RED+"\n[-]Credenciales incorrectas."+Fore.RED)
                option = 1
        elif option == 2:
            print(Back.WHITE+Fore.BLACK+"\n    Datos de perfil"+Fore.RESET+Back.RESET)
            name = red.consult_name()
            age = red.consult_age()
            country = red.consult_country()
            city = red.consult_city()
            tel = red.consult_tel()
            print(Back.WHITE+Fore.BLACK+"\n    Datos de la cuenta\n"+Fore.RESET+Back.RESET)
            user = input(Fore.YELLOW+"Usuario: "+Fore.RESET)
            password = getpass.getpass(Fore.YELLOW+"Contraseña: "+Fore.RESET)
            reg = red.reg_users(name, age, country, city, tel, user, password)
            if reg == True:
                print(Fore.GREEN+"\n[+]Registro existoso! Bienvenido "+user+Fore.RESET)
                option = 1
            else:
                print(Fore.RED+"\n[-]El usuario "+user+", ya esta en uso."+Fore.RESET)
                option = 1
        elif option == 0:
            break
    if option == 0:
        print("Saliendo...")
    else:
        #Bucle secundario para usuarios autenticados y registrados
        while option != 0:
            option = red.second_menu()
            if option == 1: 
                print(Back.WHITE+Fore.BLACK+"\nQue estas pensando?\n"+Fore.RESET+Back.RESET)
                message = input(user+": ")
                now = datetime.now()
                message = now.strftime('[%d/%m/%Y||%H:%M:%S]: ') + message
                msg = red.msg_muro(user, message)
                if msg == True:    
                    option = 1
            elif option == 2:
                print(Back.WHITE+Fore.BLACK+"\nMuro\n"+Fore.RESET+Back.RESET)
                red.show_muro(user)
            elif option == 3:
                print(Back.WHITE+Fore.BLACK+"\nPerfil\n"+Fore.RESET+Back.RESET)
                red.show_perfil(user)
            elif option == 4:
                print(Back.WHITE+Fore.BLACK+"\nActualizar Perfil\n"+Fore.RESET+Back.RESET)
                name = red.consult_name()
                age = red.consult_age()
                country = red.consult_country()
                city = red.consult_city()
                tel = red.consult_tel()
                password_new = getpass.getpass("Contraseña: ")
                update = red.update_perfil(name, age, country, city, tel, user, password_new)
                if update == True:
                    print(Fore.GREEN+"\n[+]Datos de perfil actualizados con exito."+Fore.RESET)
            elif option == 5:
                print(Back.WHITE+Fore.BLACK+"\nAgregar Amigo\n"+Fore.RESET+Back.RESET)
                friend = input("Nombre de usuario (No olvides las mayusculas si es el caso): ")
                fd = red.friends_list(user, friend)
                if fd == True:    
                    print(Fore.GREEN+"\n[+]Amigo agregado a tu lista."+Fore.RESET)
                else:
                    print(Fore.RED+"\n[-]El nombre ingresado no existe."+Fore.RESET)
            elif option == 6:
                print(Back.WHITE+Fore.BLACK+"\nMensajes Privados\n"+Fore.RESET+Back.RESET)
                friend = input("Nombre de su amigo (No olvides las mayusculas si es el caso): ")
                room = red.show_room_priv(user, friend)
                if room == True:
                    message_priv = input(user+": ")
                    now = datetime.now()
                    message_priv = now.strftime('[%d/%m/%Y||%H:%M:%S]: ') + message_priv
                    red.update_room_priv(user, friend, message_priv)
                    print(Fore.RED+message_priv+"\n[+]Fue enviado con exito."+Fore.RESET)
                else:
                    print(Fore.RED+"\n[-]El nombre ingresado no existe o ya es tu amigo."+Fore.RESET)
            elif option == 0:
                break
        if option == 0:
            print("Saliendo...")  
if __name__ == "__main__":
    main()