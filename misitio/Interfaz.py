import requests,json


class Interfaz():

    def __init__(self):
        self.nombre = ""
        self.url = ""
        self.metodo = ""
        self.token = ""
        pass


    
    def modificar (self, **kwargs):
        for key, value in kwargs.items():
            if key == "url":
                self.url = value
            if key == "metodo":
                self.metodo = value


    def establecerNombre(self, nombre):
        self.nombre = nombre
    def obtenerNombre(self):
        return self.nombre





    def enviar(self, *args, **kwargs):
        print ("Dentro de enviar")

        

        if self.metodo == 'GET':
            response = requests.get(self.url)

            #token = response.
        if self.metodo == 'POST':
            response = requests.post(self.url)
            

        if response.status_code == 200:
            print ("Exitoso")
            #print (response.text)
            
            #print (json.loads(response))
            #respuesta = json.loads(str(response.text))

            #self.token = respuesta['csrf_token']
            
        else:
            print ("Fallido")



    def __str__(self):
        return "{} ".format( self.obtenerNombre())

def main():

    interfaz = Interfaz()
    interfaz.establecerNombre("Prueba de interfaz de comunicación")
    interfaz.modificar(url='http://127.0.0.1:8000/hook/', metodo="GET")
    interfaz.modificar(url='http://127.0.0.1:8000/hook/', metodo="POST")

    interfaz.enviar()

    print (interfaz)
    pass

if __name__ == "__main__":
    main()
