##### Variables #####
billetes=[20000,10000,5000,2000,1000]
monedas=[500,100,50,10]
valor_de_compra=25550
vuelto_desglosado={}

while True:
    try: 
        paga=int(input(f"""El valor de su compra corresponde a ${valor_de_compra}
                       
            Ingrese un monto superior a la compra para realizar su pago.
               ¿Con cuanto paga?
                con: $"""))
        if not paga%10==0:
                print("Valor invalido, recuerda que en Chile la moneda de menor valor es 10")
                print("Por lo que se le dara vuelto en monedas de 10 en 10")
                print("Ingrese un monto valido para realizar su compra")
        elif paga >= valor_de_compra:
            break
        else:
            print("Ingrese un valor superior a la compra")
    except ValueError:
        print("Ingrese un valor valido")

vuelto=paga-valor_de_compra
##### Creacion del cajero #####

def cajero(paga):
    while True:
        if paga>=valor_de_compra:
                print(f"""¡Pago exitoso!
                Su vuelto es de: ${vuelto}
                """)
                break
               
        
cajero(paga)

##### Proceso de evaluacion del vuelto#####    
def vuelto(vuelto):
    if vuelto > 990:
        for i in billetes:
            if vuelto >= i:
                vuelto_desglosado[i]=vuelto//i
                vuelto=vuelto%i
            elif vuelto < 990:
                for i in monedas:
                    if vuelto >= i:
                        vuelto_desglosado[i]=vuelto//i
                        vuelto=vuelto%i
    else:
        for i in monedas:
            if vuelto >= i:
                vuelto_desglosado[i]=vuelto//i
                vuelto=vuelto%i
    print("Su vuelto es:")
    for i,j in vuelto_desglosado.items():
        print(f"{j} x ${i}")
    if paga == valor_de_compra:
        print("No le corresponde vuelto, ya que pago con lo justo.")
        
vuelto(paga-valor_de_compra)