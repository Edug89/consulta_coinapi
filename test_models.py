#15913 de 16132 = 219

from criptoexchange.models import TodoCoinApiIo,Cambio
from config import apikey
import pytest


def test_todocoin(): #definimos funcion
    todas = TodoCoinApiIo() #instanciamos todocoinapio
    assert isinstance(todas,TodoCoinApiIo) #hacemos prueba de todas y todocianapio
    todas.trae(apikey) #llamamos la funcion trae con la apikey para buscar las criptos y no criptos
    assert len(todas.criptos) == 15913 #hacemos prueba del numero de criptos
    assert len(todas.no_criptos) == 219 #hacemos prueba del numero de NOcriptos

def test_cambio_ok(): #definimos funcion
    btcEuro = Cambio("BTC") #instanciamos y llamamos BTC
    assert btcEuro.tasa is None # inicializamos tasa en None,para que no de error
    assert btcEuro.horafecha is None #inicializamos horafecha en None, para que no de error
    btcEuro.actualiza(apikey) #hacemos la llamada a la funcion actualiza,llamando apikey
    assert btcEuro.tasa > 0 #hacemos prueba de que tasa debe ser mayor a 0
    assert isinstance(btcEuro.horafecha, str) #hacemos prueba de que hora fecha debe ser una cadena






