
class Empleado:
	def __init__(self):
        self.nombre = ""
	self.apellido = ""
	self.cedula = ""
	self.comision_fija = 0
	
	def agregar_comision_fija (self , comision):
		self.comision_fija = comision
	def obtener_comision_fija (self):
		return self.comision_fija 
	def agregar_nombre (self , n):
		self.nombre = n
	def obtener_nombre (self):
		return self.nombre 
	def agregar_apellido (self, a):
		self.apellido = a
	def obtener_apellido (self):
		return self.apellido
	def agregar_cedula (self, c):
		self.cedula = c
	def obtener_cedula (self):
		return self.cedula  
	
	def presentar_datos (self):
		cadena = "Informaci? de %s %s\n  cedula:%s" %(self.nombre , self.apellido, self.cedula)
               
class EmpleadoPorHoras(Empleado)
        def __init__(self):
         super(EmpleadoPorHoras, self).__init__()
         self numero_horas = 0
         self valor_horas = 0
         

        def agregar_numero_horas(self, num_h):  
         self.numero_horas = num_h

        def obtener_numero_hora(self):
         return self.numero_horas
        
        def agregar_valor_horas(self, val_h):  
         self.valor_horas = val_h

        def obtener_valor_horas(self):
         return self.valor_horas

        def calcular_valor_sueldo(self)
          sueldo_final = 0
          sueldo_final = self.obtener_numero_hora() * self.obtener_valor_horas()
          sueldo_final = sueldo_final + self.obtener_comision_fija()
          return sueldo_final

        def presentar_datos(self)
         cadena : "%s \n Numero horas: %s\nValor hora: %s\n Sueldo Final %s" %(super(EmpleadoPorHoras, self),
         presentar_datos(),self.obtener_numero_horas(),self.obtener_valor_horas(),self.calcular_valor_sueldo()) 
       
class EmpleadoFijo(Empleado)
        def __init__(self):
        super(EmpleadoFijo,self).__init__()
        self sueldo_fijo = 0
        self descuento_seguro = 0

    def agregar_sueldo_fijo(self, s):
        self.sueldo_fijo = s

    def obtener_sueldo_fijo(self):
        return self.sueldo_fijo

    def agregar_descuento_seguro(self, des):
        self.descuento_seguro = des

    def obtener_descuento_seguro(self):
        return self.descuento_seguro

    def presentar_datos(self):
        cadena = "%s \nSueldo Fijo: %s \nDescuento seguro: %s \nSueldo final: %s" %
        (super(EmpleadoFijo,self).presentar_datos(), self.obtener_sueldo_fijo(), self.obtener_descuento_seguro(),
         self.calcular_valor_sueldo())

    def calcular_valor_sueldo(self):
        print(self.sueldo_fijo)
        print(self.descuento_seguro)
        print(self.comision_fija)

        
class EmpleadoPorSemana(Empleado)
        def __init__(self):
         super(EmpleadoPorSemana, self).__init__()
         self numero_semana = 0
         self valor_semana = 0
         

        def agregar_numero_semana(self, num_s):  
         self.numero_horas = num_s

        def obtener_numero_semana(self):
         return self.numero_horas
        
        def agregar_valor_semana(self, val_s):  
         self.valor_semana = val_s

        def obtener_valor_semana(self):
         return self.valor_semana

        def calcular_valor_sueldo(self)
          sueldo_final = 0
          sueldo_final = self.obtener_numero_semana() * self.obtener_valor_semana()
          sueldo_final = sueldo_final + self.obtener_comision_fija()
          return sueldo_final

        def presentar_datos(self)
         cadena : "%s \n Numero Semanas: %s\nValor por Semana: %s\n Sueldo Final %s" %(super(EmpleadoPorHoras, self),
         presentar_datos(),self.obtener_numero_semana(),self.obtener_valor_semana(),self.calcular_valor_sueldo()) 
       


	   
