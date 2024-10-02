mesos = (0,"Gener","Febrer","Març","Abril","Maig","Juny","Juliol","Agost","Setembre","Octubre","Novembre","Desembre")
numeroUsuari = None

while numeroUsuari != 0:
    numeroUsuari = int(input("Introdueix un numero del 1-12 per escollir un mes"))
    print(mesos[numeroUsuari])

print("S'ha acabat")