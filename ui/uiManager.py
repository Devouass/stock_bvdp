# -*- coding: UTF-8 -*-
#!/usr/bin/python

import sys
import os

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

from stockProduct.productsManager import ProductManager
from ui.stockReporter import StockReporter

class UiManager(object):

    def __init__(self):
        self._fenetre = Tk()
        self._productManager = ProductManager()
        self._stockReporter = StockReporter()
        self._achatFilePath = ""
        self._venteFilePath = ""

    #start UI
    def startUi(self):

        self._fenetre.title('Stock Calculateur')
        self._fenetre.geometry("750x500")
        self._fenetre.resizable(0,1)

        Label(self._fenetre, text="Stock buvette du plan de l'aiguille", font='Helvetica 18 bold', height=2).grid(row=0, column=0, columnspan=3)

        Label(text='fichier d\'achat (xls) :', width=15, anchor='w').grid(row=1,column=0,padx=5,pady=10)
        self._achatFilePath = StringVar()
        self._achatFilePath.set("C:/Users/jdevo/Documents/code_bvdp/utils/achats.xlsx")
        Entry(self._fenetre, textvariable=self._achatFilePath, width=80).grid(row=1,column=1,padx=5,pady=10)
        Button(self._fenetre, text="parcourir", command=self.getAchatFileName, width=12).grid(row=1, column=2,padx=5,pady=10)

        Label(text='fichier d\'export (csv) :', width=15, anchor='w').grid(row=2,column=0,padx=5,pady=10)
        self._venteFilePath = StringVar()
        self._venteFilePath.set("C:/Users/jdevo/Documents/code_bvdp/utils/Export.csv")
        Entry(self._fenetre, textvariable=self._venteFilePath, width=80).grid(row=2,column=1,padx=5,pady=10)
        Button(self._fenetre, text="parcourir", command=self.getExportFileName, width=12).grid(row=2, column=2,padx=5,pady=10)

        Button(self._fenetre, text="calcul du stock", command=self.calculateStock, width=12).grid(row=3, column=2,padx=5,pady=20)

        report = StringVar()
        Label(text='Rapport', width=15, anchor='nw', height=15).grid(row=4,column=0,padx=5,pady=10)
        Label(textvariable=report, anchor='w', bg='white', justify='left', height=15, width=82).grid(row=4,column=1,columnspan=2,pady=10)
        self._stockReporter.setStringVar(report)

        self._fenetre.mainloop()

    def getExportFileName(self):
        filename = askopenfilename()
        self._venteFilePath.set(filename)

    def getAchatFileName(self):
        filename = askopenfilename()
        self._achatFilePath.set(filename)

    def error(self, message):
        showerror('format de fichier', message)

    def checkFileValidity(self):
        validity = True
        if not self._achatFilePath.get() or not self._achatFilePath.get().endswith('.xlsx') or not os.path.isfile(self._achatFilePath.get()):
            validity = False
            self.error('veuillez selectionner un fichier d\'achat valide\nun classeur excel au format xlsx')
        else:
            if not self._venteFilePath.get() or not self._venteFilePath.get().endswith('.csv') or not os.path.isfile(self._venteFilePath.get()):
                validity = False
                self.error('veuillez selectionner un fichier d\'export de caisse valide\nun export au format csv')
        return validity

    def calculateStock(self):
        if self.checkFileValidity():
            self._stockReporter.addReport('début du calcul du stock\n')
            self._productManager.calculateProductsStock(self._achatFilePath.get(), self._venteFilePath.get(), 'utils/res.xlsx', self._stockReporter)
