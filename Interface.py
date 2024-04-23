from Robo import Robo
from tkinter import *
import os


class Interface(Robo):
    def __init__(self):
        self.diretorio_atual = os.getcwd()
        self.icone = os.path.join(self.diretorio_atual, 'Imagens-interface', 'icon_nelson.ico')

        self.backgroundimg = os.path.join(self.diretorio_atual, 'Imagens-interface', 'background.png')
        self.img0 = os.path.join(self.diretorio_atual, 'Imagens-interface', 'img0.png')
        self.img1 = os.path.join(self.diretorio_atual, 'Imagens-interface', 'img1.png')
        self.img2 = os.path.join(self.diretorio_atual, 'Imagens-interface', 'img2.png')
        self.img3 = os.path.join(self.diretorio_atual, 'Imagens-interface', 'img3.png')
        self.img4 = os.path.join(self.diretorio_atual, 'Imagens-interface', 'img4.png')
        self.img5 = os.path.join(self.diretorio_atual, 'Imagens-interface', 'img5.png')
        self.img6 = os.path.join(self.diretorio_atual, 'Imagens-interface', 'img6.png')

    
    def btn_clicked():
        print("Button Clicked")


    def criar_interface(self):
        window = Tk()
        window.title('Sistema de Automações')
        window.iconbitmap(self.icone)
        window.geometry("365x335")
        window.configure(bg = "#FFFFFF")
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 335,
            width = 365,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = self.backgroundimg)
        background = canvas.create_image(
            182.5, 167.5,
            image=background_img)

        img0 = PhotoImage(file = self.img0)
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.arrumar_estoque,
            relief = "flat")

        b0.place(
            x = 15, y = 270,
            width = 160,
            height = 30)

        img1 = PhotoImage(file = self.img1)
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tratar_estoque,
            relief = "flat")

        b1.place(
            x = 190, y = 221,
            width = 160,
            height = 30)

        img2 = PhotoImage(file = self.img2)
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.emitir_nota_efluente,
            relief = "flat")

        b2.place(
            x = 15, y = 221,
            width = 160,
            height = 30)

        img3 = PhotoImage(file = self.img3)
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.baixar_nota,
            relief = "flat")

        b3.place(
            x = 190, y = 172,
            width = 160,
            height = 30)

        img4 = PhotoImage(file = self.img4)
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.comprar_material,
            relief = "flat")

        b4.place(
            x = 15, y = 172,
            width = 160,
            height = 30)

        img5 = PhotoImage(file = self.img5)
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.fazer_manutencao_comprar,
            relief = "flat")

        b5.place(
            x = 190, y = 123,
            width = 160,
            height = 30)

        img6 = PhotoImage(file = self.img6)
        b6 = Button(
            image = img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.fazer_manutencao,
            relief = "flat")

        b6.place(
            x = 15, y = 123,
            width = 160,
            height = 30)

        window.resizable(False, False)
        window.mainloop()
