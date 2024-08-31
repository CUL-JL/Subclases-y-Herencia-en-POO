from actividades.actividad_5 import *

while True:
    try:
        metodo_pago = int(input('Seleccione el metodo de pago:\n1. Tarjeta\n2. Paypal\n3. Criptomoneda\n4. Salir\nIngrese el numero de la opcion: '))
        if metodo_pago == 1:
            while  True:
                try:
                    print('Ingrese el numero de tarjeta en con una longitud de 16 digitos y el monto a pagar.')
                    tarjeta = PagoTarjeta(input('Ingrese el numero de tarjeta: '), input('Ingrese el monto a pagar: '))
                    procesar_pagos(tarjeta)
                    break

                except ValueError as e:
                    print(f'Error: {e}')

        elif metodo_pago == 2:
            while True:
                try:
                    paypal = PagoPaypal(input('Ingrese el email: '), input('Ingrese el monto a pagar: '))
                    procesar_pagos(paypal)
                    break

                except ValueError as e:
                    print(f'Error: {e}')

        elif metodo_pago == 3:
            while True:
                try:
                    print('Ingrese la wallet de 4 digitos y el monto a pagar.')
                    criptomoneda = PagoCriptomoneda(input('Ingrese la wallet: '), input('Ingrese el monto a pagar: '))
                    procesar_pagos(criptomoneda)
                    break

                except Exception as e:
                    print(f'Error: {e}')

        elif metodo_pago == 4:
            break

        else:
            print('Error: Opcion invalida.')

    except ValueError:
        print('Error: Ingrese un valor valido.')
