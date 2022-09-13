#15913 de 16132 = 219

from criptoexchange.models import TodoCoinApiIo
from config import apikey

def test_todocoin(): #definimos funcion
    todas = TodoCoinApiIo() #instanciamos todocoinapio
    assert isinstance(todas,TodoCoinApiIo) #hacemos prueba de todas y todocianapio
    todas.trae(apikey) #llamamos la funcion trae con la apikey para buscar las criptos y no criptos
    assert len(todas.criptos) == 15913 #hacemos prueba del numero de criptos
    assert len(todas.no_criptos) == 219 #hacemos prueba del numero de NOcriptos




