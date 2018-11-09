

from mipaquete.modelo import *

e = Empleado()
e.agregar_nombre("Luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("1110001")
print(e.presentar_datos())

e1 = EmpleadoPorHoras()
nombre = rew_imput ("Ingrese su nombre\n ")
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.agregar_cedula("112233")
e1.agregar_valor_horas(20.2)
e1.agregar_numero_horas(15)
print (e1.presentar_datos()) 
 
e2 = EmpleadoFijo()
e2.agregar_sueldo(300.2)
e2.descuento_seguro(10)
comision = raw_imput ("Ingrese comision: \n")
comision = float (comision)
e2.agregar_comision_fija(comision)
e2.nombre = "Ana"
e2.apellido = "Diaz"
print (e2.presentar_datos())
