from tkinter import *
import tkinter as tk
import pandas as pd
import numpy as np


class Stack:

    def __init__(self, tipoPokemon):
        archivo = pd.read_csv("./baseDatos/pokedex_dataset.csv", header=0)
        self.tipoPokemon = tipoPokemon
        self.poder = pokePoder(archivo, self.tipoPokemon)
        self.nombre = nombrePoke(archivo, self.tipoPokemon)
        self.ataque = ataque(archivo, self.tipoPokemon)
        self.defensa = defensa(archivo, self.tipoPokemon)
        self.salud = salud(archivo, self.tipoPokemon)
        
        



# Attack,Defense,Sp
def pokePoder(dataTable, typePokemon):
    pokemonesNames = dataTable[dataTable["Type 1"] == typePokemon]
    ordenando = pokemonesNames.sort_values(by='Total',ascending=False)
    final = ordenando["Total"]
    return final


def nombrePoke(dataTable, typePokemon):
    pokemonesNames = dataTable[dataTable["Type 1"] == typePokemon]
    ordenando = pokemonesNames.sort_values(by='Total',ascending=False)
    final = ordenando["Name"]
    return final
    
def ataque(dataTable, typePokemon):
    pokemonesNames = dataTable[dataTable["Type 1"] == typePokemon]
    ordenando = pokemonesNames.sort_values(by='Total',ascending=False)
    nombre = ordenando["Attack"]
    return nombre
    

def defensa(dataTable, typePokemon):
    pokemonesNames = dataTable[dataTable["Type 1"] == typePokemon]
    ordenando = pokemonesNames.sort_values(by='Total',ascending=False)
    defensa = ordenando["Defense"]
    return defensa

def salud(dataTable,typePokemon):
    pokemonesNames = dataTable[dataTable["Type 1"] == typePokemon]
    ordenando = pokemonesNames.sort_values(by='Total',ascending=False)
    salud = ordenando["HP"]
    return salud