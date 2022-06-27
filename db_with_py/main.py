#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:00:14 2022

@author: kevinsdj
"""
import sqlite3

checkTableQuery="""SELECT name FROM sqlite_master WHERE type='table' AND name='Alumnos'"""
initTableAlumno="""CREATE TABLE Alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT,apellido TEXT NOT NULL);"""
viewAllData="""SELECT * FROM Alumnos;"""
srAlumnQuery=lambda strg:f"SELECT * FROM Alumnos WHERE nombre LIKE '%{strg}%';"
def testTable ():
    conn=sqlite3.connect('datos.db')
    cursor= conn.cursor()
    rows=cursor.execute(checkTableQuery).fetchall()
    cursor.close()
    conn.close()
    if rows.__len__():
        return True
    else:
        return False

def iniTable():
    exist=testTable()
    if not exist:
        conn= sqlite3.connect('datos.db')
        cursor= conn.cursor()
        rows=cursor.execute(initTableAlumno)
        cursor.close()
        conn.close()
        return True
    else:
        return False

def regAlumn(n,ap):
    alumn=(None,n,ap)
    insertDataAlumn= """INSERT INTO Alumnos (id,nombre,apellido)  VALUES(?,?,?);"""
    conn=sqlite3.connect('datos.db')
    cursor= conn.cursor()
    rows=cursor.execute(insertDataAlumn,alumn)
    conn.commit()
    cursor.close()
    conn.close()
    print(rows)
def showData():
     conn=sqlite3.connect('datos.db')
     cursor=conn.cursor()
     rows=cursor.execute(viewAllData).fetchall()
     cursor.close()
     conn.close()
     print(rows)

def searchAlumn(pattern):
    conn= sqlite3.connect('datos.db')
    cursor=conn.cursor()
    rows=cursor.execute(srAlumnQuery(pattern)).fetchall()
    cursor.close()
    conn.close()
    print(rows)

def main ():
    nextInsert=True
    result = iniTable()
    result and print('Tabla Alumnos creada') or print('Tabla existente!, accediendo...')
    while nextInsert:
        print('Por favor ingrese los datos solicitados a continuacion...')
        nombre=str(input('Nombre: '))
        apellido= str(input('Apellido: '))
        print('Registrando datos...')
        regAlumn(nombre,apellido)
        ask=str(input('Ingresar otro? si / no   '))
        if ask.lower().startswith('n'):
            nextInsert=False
    print('Datos cargados:\n')
    showData()
    ask=str(input('Quieres buscar un alumno en concreto?  si / no'))
    resp= ask.lower().startswith('s')
    if resp:
        pattern=str(input('Ingresa el nombre o patron del nombre a buscar: '))
        searchAlumn(pattern)


main()
