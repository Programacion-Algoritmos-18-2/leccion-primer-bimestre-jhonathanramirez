/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package leccion;

/**
 *
 * @author Usuario
 */
public class EmpleadoPorSemana {
   private double numero_semanas, valor_semanas;

          
    
    public void setnumero_semanas(double suf) {
        numero_semanas = suf;
    }

    public double getnumero_semanas() {
        return numero_semanas;
    }
    
    public void setvalor_semanas(double suf) {
        valor_semanas = suf;
    }

    
    
    public double getvalor_semanas() {
        return valor_semanas;
    }
    
    public double calcular_suF(){
        double f =valor_semanas* numero_semanas;        
        return f;
        
    }
    @Override
    public String toString(){   
        return String.format("%s Numero Semanas :%f Valor por semana %f Total %f", super.toString(), getnumero_semanas(), getvalor_semanas(), calcular_suF());
    }
    
    
    
} 

