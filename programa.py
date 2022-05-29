import os
import random


class extracto():
    def __init__(self, txt):
        print(txt[0])
        if txt[0].find("-") == -1:
            self.titulo = txt[0].split('(')[0]
            self.autor = txt[0].split('(')[1].replace(')', '')
        elif txt[0].find('-') != -1 and len(txt[0].split('-')) == 2:
            self.titulo = txt[0].split('-')[0]
            self.autor = txt[0].split('-')[1]

        if len(txt[1].split('|')) == 3:
            self.pagina = txt[1].split(' ')[6]
            self.posicion = txt[1].split(' ')[9]
            self.fecha = ' '.join(txt[1].split(' ')[14:])
        elif len(txt[1].split('|')) == 2:
            self.posicion = txt[1].split(' ')[6]
            self.fecha = ' '.join(txt[1].split(' ')[11:])

        self.tipo = txt[1].split(' ')[2]

        self.texto = ''
        for i in range(len(txt)-3):
            self.texto = self.texto + txt[i+3] + '\n'

    def crearArchivo(self):
        self.l = []

        self.l.append("/home/juan/notas/Extractos/" +
                      self.titulo.strip()+'-'+' '.join(self.texto.split(" ")[0:4])+".md",)

        f = open("/home/juan/notas/Extractos/" +
                 self.titulo.strip()+'-'+' '.join(self.texto.split(" ")[0:4])+".md", "w")
        f.write('Libro:[['+self.titulo.strip()+']]\n\n' +
                self.texto+'\n'+self.posicion+'\n'+self.fecha)
        f.close()

    def getLista(self):
        return self.l


with open("My Clippings.txt") as file:
    lines = file.readlines()


a = 0
lista = []
for i in range(len(lines)):
    lines[i] = lines[i].replace('\ufeff', '')
    lines[i] = lines[i].replace('\n', '')
    lines[i] = lines[i].replace('\t', ' ')
    lines[i] = lines[i].replace('(Spanish Edition)', '')

    if lines[i] == '==========':
        txt = lines[a:i]
        extr = extracto(txt)
        lista.append(extr)
        a = i + 1

for i in lista:
    i.crearArchivo()
