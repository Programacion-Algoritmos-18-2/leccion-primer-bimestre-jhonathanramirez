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
public class Empleado {
    private String nombre;
    private String apellido;
    private String cedula; 
    private int comision_fija;
 

    public String obtenerNombre() {
        return nombre;
    }

    public String obtenerApellido() {
        return apellido;
    }

    public String obtenerCedula() {
        return cedula;
    }

    public int obtenerComision_fija() {
        return comision_fija;
    }

    public void agregarNombre(String n) {
        nombre = n;
    }

    public void agregarApellido(String ape) {
        apellido = ape;
    }

    public void agregarCedula(String ced) {
        cedula = ced;
    }

    public void agregarComision_fija(int com_f) {
        comision_fija = com_f;
    }
 @Override
    public String toString() {
       String cadena = String.format("Informacion de %s %s \n cedula: %s" ,
                obtenerNombre(), obtenerApellido(),obtenerCedula());
        return cadena;
    }
}

