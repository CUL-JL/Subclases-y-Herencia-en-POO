## Ejercicio 1

### Implementación Básica de Herencia
Implementa una clase base llamada `Vehiculo` con un atributo `marca` y un método 
`acelerar()` que imprime **"El vehículo está acelerando"**. 
Luego, crea dos subclases llamadas `Coche` y `Motocicleta` que hereden de `Vehiculo`. En la 
subclase `Coche`, agrega un método llamado `tocar_claxon()` que imprima "¡Beep beep!" y 
en la subclase `Motocicleta`, agrega un método llamado `hacer_caballito()` que imprima "La 
motocicleta está haciendo un caballito". Escribe un programa que cree instancias de 
`Coche` y `Motocicleta` y llame a todos sus métodos.

## Ejercicio 2
### Polimorfismo con Animales
Crea una clase base llamada `Animal` que tenga un método `hacer_sonido()` que no esté 
implementado (puede usar pass). 
Luego, implementa dos subclases, `Perro` y `Gato`, que sobrescriban el método 
`hacer_sonido()` con las impresiones "Guau guau" para `Perro` y "Miau miau" para `Gato`. 
Crea una función llamada `hacer_ruido(animal)` que reciba un objeto de tipo `Animal` y 
llame al método `hacer_sonido()`. Escribe un programa que demuestre el uso de 
polimorfismo llamando a `hacer_ruido()` con diferentes tipos de animales.

## Ejercicio 3

### Subclase y Herencia:
Crea una subclase llamada `UsuarioPremium` que herede de la clase `Usuario`. Añade un atributo `adicional nivel_premium` (que puede ser "Oro", "Plata" o "Bronce") y un método `obtener_descuento()` que retorne un porcentaje de descuento basado en el nivel premium (Oro: 20%, Plata: 15%, Bronce: 10%). ¿Cómo implementarías esta subclase y cómo podrías crear un objeto de esta nueva clase?

## Ejercicio 4

### Polimorfismo:
Modifica la clase Usuario para incluir un método `mostrar_info()` que muestre el username y el email. Luego, en la subclase `UsuarioPremium`, sobrescribe este método para que también muestre el nivel premium. Crea una función `imprimir_informacion_usuario` (usuario) que acepte tanto objetos Usuario como `UsuarioPremium` y llame a su método `mostrar_info()`. ¿Cómo demostrarías el polimorfismo con esta implementación?

## Ejercicio 5

### Sistema de Pago con Herencia, Polimorfismo y Excepciones:
Implementa un sistema de pago básico utilizando **herencia**, **polimorfismo** y manejo de 
**excepciones**. Crea una clase base llamada `Pago` con un método `procesar_pago()` que no esté 
implementado. Luego, crea tres subclases llamadas `PagoTarjeta`, `PagoPaypal`, y 
`PagoCriptomoneda`, cada una implementando su propio `procesar_pago()`. Asegúrate de 
que `PagoTarjeta` valide que el número de tarjeta tiene **16 dígitos**, que `PagoPaypal` 
verifique que el correo electrónico tenga un formato válido, y que `PagoCriptomoneda` 
capture cualquier excepción genérica relacionada con la transacción. Escribe un 
programa que simule pagos utilizando cada uno de estos métodos y maneje cualquier 
excepción que pueda ocurrir