# -*- coding: UTF-8 -*-

import json

from utils.excelReader import getBuyProductsArray
from utils.csvReader import getSellProductsArray
from utils.excelWriter import saveAsExcel
from utils.confParser import ConfParser
from stockProduct.stockProduct import StockProduct

class ProductManager(object):

    def __init__(self):
        self.products = {}
        self._confParser = ConfParser()

    def getBuyProducts(self, buyProductsFilePath):
        productsArrayFromExcel = getBuyProductsArray(buyProductsFilePath)

        for excelProducts in productsArrayFromExcel:
            for name, caracteristics in excelProducts.items():
                productProperties = self._confParser.getBuyProductProperties(name)

                if 'cat' in productProperties:
                    name = productProperties['cat']

                if name not in self.products:
                    supp_cond = productProperties['supp_cond'] if 'supp_cond' in productProperties else 1
                    p = StockProduct(name, supp_cond)
                    p.addAchat(caracteristics['quantity'], caracteristics['cond'])
                    self.products[name] = p
                else:
                    self.products[name].addAchat(caracteristics['quantity'], caracteristics['cond'])

    def getStock(self, sellFilePath):
        productsArrayFromCSV = getSellProductsArray(sellFilePath)

        for name, quantity in productsArrayFromCSV.items():
            productProperties = self._confParser.getSellProductProperties(name)

            if productProperties:
                for cat, factor in productProperties.items():
                    if cat not in self.products:
                        print('product {n} not used for cat {c}'.format(n = name, c = cat))
                    else:
                        self.products[cat].addVente(quantity * factor)
            else:
                if name not in self.products:
                    print('no product name {n} selled'.format(n = name))
                else:
                    self.products[name].addVente(quantity)

    def setProductsFormattageProperties(self):
        for name, product in self.products.items():
            formattageProperties = self._confParser.getFormattageProperties(name)

            if formattageProperties:
                for mul, factor in formattageProperties.items():
                    if mul == 'div':
                        self.products[name].setDivFormattage(factor)

    def saveProductsStock(self, saveFilePath):
        saveAsExcel(self.products, saveFilePath)

    def calculateProductsStock(self, buyProductsFilePath, sellFilePath, saveFilePath):
        self.getBuyProducts(buyProductsFilePath)
        self.getStock(sellFilePath)
        self.setProductsFormattageProperties()
        self.saveProductsStock(saveFilePath)
        return self.products



    def resetProducts(self):
        self.products = {}
