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
public class EmpleadoPorHoras extends Empleado{
    
    private int numero_horas; 
    private int valor_horas; 

    public EmpleadoPorHoras(String nom, String ape, String ced, int com, int num_h, int valor_h) {
        super(nom, ape, ced, com);
        agregarNumero_horas(num_h);
        agregarValor_horas(valor_h);
    }

    

    public int obtenerNumero_horas() {
        return numero_horas;
    }

    public int obtenerValor_horas() {
        return valor_horas;
    }

    public void agregarNumero_horas(int num_h) {
        numero_horas = num_h;
    }

    public void agregarValor_horas(int valor_h) {
        valor_horas = valor_h;
    }
 @Override
    public String toString() {
       String cadena = String.format("\n Numero horas: %s\nValor hora: %s\n Sueldo Final %s" ,
             super.toString(), obtenerNumero_horas(), obtenerValor_horas());
        return cadena;
    }
    
}
