# -*- coding: UTF-8 -*-

from stockProduct.productsManager import ProductManager

def getStock():
    productManager = ProductManager()
    productManager.calculateProductsStock('utils/achats.xlsx', 'utils/Export.csv', 'utils/res.xlsx')

getStock()
