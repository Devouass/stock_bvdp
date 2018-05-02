# -*- coding: UTF-8 -*-

class StockProduct(object):

    def __init__(self, nom, supp_cond = 1):
        self.name = nom
        self._achat = 0
        self._vente = 0
        self._div = 1
        self._supp_cond = supp_cond

    def updateSuppCond(self, supp_cond):
        self._supp_cond = supp_cond

    def setDivFormattage(self, div):
        self._div = div

    def addAchat(self, quantity, cond):
        self._achat += ( quantity * cond * self._supp_cond )

    def addVente(self, vente):
        self._vente += vente

    def getStock(self):
        stock = int((self._achat - self._vente) / self._div)
        if self._supp_cond > 1:
            stock = int(stock / self._supp_cond)
        return stock

    def getDiv(self):
        return self._div

    def getUnitaryStock(self):
        stock = int(self._achat - self._vente)
        if self._supp_cond > 1:
            stock = int(stock / self._supp_cond)
        return stock

    def getAchat(self):
        if self._supp_cond > 1:
            achat = int( (self._achat / self._supp_cond) / self._div)
        else:
            achat = int(self._achat / self._div)
        return achat

    def getUnitaryAchat(self):
        return self._achat / self._supp_cond

    def res(self):
        print('product {name}, quantity {quantity}, vente {stock}'.format(name = self.name, quantity = self._achat, stock = self._vente))
