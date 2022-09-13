
from logging import exception
import requests
from config import apikey

class ModelError(exception):
    pass


class TodoCoinApiIo:
    def __init__(self):
        self.criptos = []
        self.no_criptos = []

    def trae(self,apikey):
        r = requests.get("https://rest.coinapi.io/v1/assets?apikey={}".format(apikey))
        if r.status_code != 200:
            raise Exception("error en consulta de assets: {}". format(r.status_code))
        
        lista_candidatas = r.json()
        for candidata in lista_candidatas:
            if candidata["type_is_crypto"] == 1:
                self.criptos.append(candidata["asset_id"])
            else:
                self.no_criptos.append(candidata["asset_id"])

class Cambio:
    def __init__(self,cripto):
        self.cripto = cripto
        self.tasa = None
        self.datetime = None

    def actualiza(self,apikey):
        r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}". format(self.cripto, apikey))
        resultado = r.json()
        if r.status_code == 200:
            self.tasa = resultado["rate"]
            self.horafecha = resultado ["time"]
        else:
            raise ModelError("{} - {}".format(r.status_code,r.error))


        



