import requests

apikey = "C5F13376-8383-4620-9AF3-47CEB3F11198"


cripto = input("Introduzca una cripto conocida: ")
while cripto != "":

    r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(cripto,apikey))

    #print(r.status_code)#para ver la respuesta que nos da(Y si da algún error)
    #print(r.text)#para saber que respuesta de texto nos da

    resultado = r.json()
    if r.status_code == 200:
        print("{:.2f} €".format(resultado["rate"]))
    else:
        print(resultado["error"])
    
    cripto = input("Introduzca una cripto conocida: ") 
 #Prueba