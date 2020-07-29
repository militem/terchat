#-*- coding: utf-8 -*-
"""
    Programacion UPS
    Fecha: 15/07/2020
    TerChat (Red Social)
"""
#Modulo para manejar archivos
import os
#Modulo para estilos por consola, Color, Color de fondo.
from colorama import init, Fore, Back, Style

def show_welcome():
    print("""
        ████████╗███████╗██████╗░░█████╗░██╗░░██╗░█████╗░████████╗
        ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║░░██║██╔══██╗╚══██╔══╝
        ░░░██║░░░█████╗░░██████╔╝██║░░╚═╝███████║███████║░░░██║░░░
        ░░░██║░░░██╔══╝░░██╔══██╗██║░░██╗██╔══██║██╔══██║░░░██║░░░
        ░░░██║░░░███████╗██║░░██║╚█████╔╝██║░░██║██║░░██║░░░██║░░░
        ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
        By: Alex Terreros
    """)
    

def main_menu():
    print(Style.BRIGHT+Back.WHITE+Fore.BLACK+"\n   Menu "+Fore.RESET+Back.RESET)
    print("1. Ingresar")
    print("2. Registrarse")
    print("0. Salir")
    option = int(input("Ingresa una opción: "))
    while option < 0 or option > 3:
        print(Fore.RED+"[-]Opcion no valida. Inténtalo otra vez."+Fore.RESET)
        option = int(input("Ingresa una opción: "))
    return option

def second_menu():
    print(Back.WHITE+Fore.BLACK+"\n   Inicio"+Fore.RESET+Back.RESET)
    print("1. Escribir en Muro")
    print("2. Mostrar Muro")
    print("3. Mostrar Perfil")
    print("4. Actualizar Perfil")
    print("5. Agregar Amigo")
    print("6. Escribir Mensaje Privado")
    print("0. Salir")
    option = int(input("Ingresa una opción: "))
    while option < 0 or option > 7:
        print(Fore.RED+"[-]Opcion no valida. Inténtalo otra vez."+Fore.RESET)
        option = int(input("Ingresa una opción: "))
    return option

def auth_users(user, password):
    if os.path.isfile("data/"+user+".user"):
        user_file = open("data/"+user+".user", "r")
        auth_password = user_file.readline()
        if password == auth_password.rstrip('\n'):
            user_file.close()
            return True
        else:
            user_file.close()
            return False
    else:
        return False
#Metodo para registrar usuarios y crear sus distintos archivos para 
#almacenar sus perfiles, mensajes y lista de amigos
def reg_users(name, age, country, city, tel, user, password):
    if os.path.isfile("data/"+user+".user"):
        return False
    else:
        user_file = open("data/"+user+".user", "w")
        user_file.write(password+"\n")
        user_file.write(name+"\n")
        user_file.write(str(age)+"\n")
        user_file.write(country+"\n")
        user_file.write(tel+"\n")
        user_file.close()
        user_msg = open("data/"+user+".msg", "w")
        user_msg.close()
        friends = open("data/"+user+".list", "w")
        friends.close()
        return True

def consult_name():
    name = input("Nombre: ")
    return name

def consult_age():
    age = int(input("Anio de nacimiento: "))
    return 2020-age-1

def consult_country():
    country = input("Pais: ")
    return country

def consult_city():
    city = input("Ciudad: ")
    return city

def consult_tel():
    tel = input("Telefono: ")
    return tel

def msg_muro(user, message):
    old_msg = open("data/"+user+".msg", "r")
    old_msg_read = old_msg.read()
    new_msg = open("data/"+user+".msg", "w")
    new_msg.write(old_msg_read)
    new_msg.write(message+"\n")
    old_msg.close()
    new_msg.close()
    return True

def show_muro(user):
    msg_file = open("data/"+user+".msg", "r")
    msg_file_read = msg_file.readlines()
    for msg in msg_file_read:
        print(msg.rstrip('\n'))
    msg_file.close()

def show_perfil(user):
    perfil_file = open("data/"+user+".user", "r")
    perfil_file_read = perfil_file.readlines()
    for perfil in perfil_file_read:
        print(perfil.rstrip('\n'))
    perfil_file.close()

#Metodo para actualizar perfil del usuario

def update_perfil(name, age, country, city, tel, user, password):
    update_file = open("data/"+user+".user", "w")
    update_file.write(password+"\n")
    update_file.write(name+"\n")
    update_file.write(str(age)+"\n")
    update_file.write(country+"\n")
    update_file.write(city+"\n")
    update_file.write(tel+"\n")
    update_file.close()
    return True

#Metodo para agregar amigos a la lista 

def friends_list(user, friend):
    if os.path.isfile("data/"+friend+".user") and not os.path.isfile("data/"+user+friend+".msg.priv"):
        friends = open("data/"+user+".list", "r")
        friends_read = friends.read()
        add_friend = open("data/"+user+".list", "w")
        add_friend.write(friends_read)
        add_friend.write(friend+"\n")
        friends.close()
        add_friend.close()

        friends = open("data/"+friend+".list", "r")
        friends_read = friends.read()
        add_friend = open("data/"+friend+".list", "w")
        add_friend.write(friends_read)
        add_friend.write(user+"\n")
        friends.close()
        add_friend.close()

        room_priv = open("data/"+user+friend+".msg.priv", "w")
        room_priv.close()
        room_priv2 = open("data/"+friend+user+".msg.priv", "w")
        room_priv2.close()
        return True
    else:
        return False

#Metodo para mostar mensajes privados entre amigos

def show_room_priv(user, friend):
    if os.path.isfile("data/"+user+friend+".msg.priv"):
        show_msg = open("data/"+user+friend+".msg.priv", "r")
        show_msg_read = show_msg.readlines()
        for msg in show_msg_read:
            print(msg.rstrip('\n'))
        show_msg.close()
        return True
    else:
        return False

#Metodo para mensajes privados entre amigos 

def update_room_priv(user, friend, message_priv):
    show_msg = open("data/"+user+friend+".msg.priv", "r")
    show_msg_read = show_msg.read()
    new_msg = open("data/"+user+friend+".msg.priv", "w")
    new_msg.write(show_msg_read)
    new_msg.write(user+": "+message_priv+"\n")
    new_msg.close()
    show_msg.close()

    show_msg = open("data/"+friend+user+".msg.priv", "r")
    show_msg_read = show_msg.read()
    new_msg = open("data/"+friend+user+".msg.priv", "w")
    new_msg.write(show_msg_read)
    new_msg.write(user+": "+message_priv+"\n")
    new_msg.close()
    show_msg.close()
    return True