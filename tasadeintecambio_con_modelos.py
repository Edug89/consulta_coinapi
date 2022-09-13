from criptoexchange.models import Cambio, ModelError,TodoCoinApiIo
from config import apikey

todas = TodoCoinApiIo()
todas.trae(apikey)

print("{} de {}".format(len(todas.criptos), len(todas.criptos) + len(todas.no_criptos)))

cripto = input("introduzca una cripto conocida: ").upper()
while cripto != "" :
    if cripto in todas.criptos:
        tipoCambio = Cambio(cripto)
        try:
            tipoCambio.actualiza(apikey)  

            print("{2.f:} €".format(tipoCambio.tasa))
        except ModelError as variable: #con este except capaturarmos el mensaje en una variable
            print("Se ha producido el error {}".format(variable))
             
    cripto = input("introduzca una cripto conocida: ").upper()
