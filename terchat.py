#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pymysql
import getpass

def conn(user, pwd, room_code):
    try:
        connect = pymysql.connect(  host='localhost',
                                    user='root',
                                    password='',
                                    db='terchat')
        if(user != None and pwd != None and room_code == 0):
            try: 
                with connect.cursor() as cursor:
                    sql = "SELECT * FROM users WHERE username = (%s)"
                    cursor.execute(sql, (user))
                    users = cursor.fetchall()
                    
                    print(users[0])

                    for auth_pwd in users:
                        if(auth_pwd[2] == pwd):
                            print("Successful auth.")
                            return 1
                        else:
                            print("Incorrect user or password")
                            return 0
            
            finally:
                connect.close()        


    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("OFFLINE ", e)

def main():
    print("""
    ████████╗███████╗██████╗░░█████╗░██╗░░██╗░█████╗░████████╗
    ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║░░██║██╔══██╗╚══██╔══╝
    ░░░██║░░░█████╗░░██████╔╝██║░░╚═╝███████║███████║░░░██║░░░
    ░░░██║░░░██╔══╝░░██╔══██╗██║░░██╗██╔══██║██╔══██║░░░██║░░░
    ░░░██║░░░███████╗██║░░██║╚█████╔╝██║░░██║██║░░██║░░░██║░░░
    ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░""")
    user = input("User: ")
    pwd = getpass.getpass("Password: ")
    auth_user = conn(user, pwd, room_code = 0)
    
main()