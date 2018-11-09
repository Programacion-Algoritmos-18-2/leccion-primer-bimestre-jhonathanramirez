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
public class Empleado_Fijo extends Empleado {

    private double sueldo_fijo = 0;
    private double descuento_seguro = 0;
    private double operacion = 0;

    public void setSueldo_fijo(double nh) {
        sueldo_fijo = nh;
    }

    public void setDescuento_Seguro(double vh) {
        descuento_seguro = vh;
    }

    public void Operacion() {

    }

    public double getNumero_horas() {
        return sueldo_fijo;
    }

    public double getValor_horas() {
        return descuento_seguro;
    }

    public double getOperacion() {
        return operacion;
    }

    @Override
    public String toString() {

        return String.format(" ", super.toString(), getValor_horas(), getNumero_horas(), getOperacion());
    }

}
