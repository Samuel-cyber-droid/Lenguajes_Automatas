using System;

class Program{
    static void Main(){
        //uso de var cnado el tipo de variable es evidente
        var mensaje = "Hola"; //el compilador infiere que es un string

        //reutilizacion de variables en bucles
        int suma = 0;
        for (int i = 0; i < 1000; i++){
            suma += i; //reuso de suma
        }

        //usar tipos especificos para valores pequeños
        short pequeño = 100; //short en lugar de int
    }
}