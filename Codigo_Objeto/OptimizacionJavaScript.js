// declarar variables con let y const en el ambito correcto

function procesar(){
    const PI = 3.1416; //constante para valores fijos
    let resultado = 0; //varibale con ambito de funcion

    for (let i = 0; i < 1000; i++){
        resultado += i; //suma de los valores de i
    }
    return resultado; //retorna el resultado de la suma
}

// evita declarar varibales inncecesarias en bucles
let i = 0;
while (i < 1000){
    // reutilizar i en lugar de declarar una varibale nueva
    console.log(i); //imprime el valor de i
}