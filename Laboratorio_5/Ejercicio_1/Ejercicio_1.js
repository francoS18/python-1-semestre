// Extraemos los datos desde el html y los almacenamos en una variable.
const pmonto = document.getElementById('monto');
const pseleccion = document.getElementById('propina');
const calcular = document.getElementById('calcular');
const presultado = document.getElementById('presultado')
const tresultado = document.getElementById('tresultado')

// Se le asigna una funcionalidad al boton de calcular
calcular.addEventListener('click', calculadora_propina)

function calculadora_propina(){
    // Extraemos el indice de la opcion seleccionada por el usuario.
    indexseleccion = pseleccion.selectedIndex;

    // Buscamos la seleccion del usuario mediante el indice que se extrajo anteriormente.
    seleccion_usuario = pseleccion.options[indexseleccion];

    // Extraemos el valor del usuario y lo tranformamos a entero.
    porcentaje_propina = seleccion_usuario.text;

    // Se extrae el valor del monto ingresado por el usuario.
    monto_total = parseInt(pmonto.value)

    // Se inicia una cadena de if con la finalidad de encontrar a cuanto equivale la propina.
    if (porcentaje_propina == '10%'){
        propina = monto_total * 0.10
    } else if(porcentaje_propina == '15%'){
        propina = monto_total * 0.15
    } else if (porcentaje_propina == '20%'){
        propina = monto_total * 0.20
    }

    // Se inicia una una cadena de if para comprobar los parametros ingresados y que coincidan con lo solicitado.
    if (porcentaje_propina == '10%'){
        monto_final = monto_total * 1.10
    } else if (porcentaje_propina == '15%'){
        monto_final = monto_total * 1.15
    } else if (porcentaje_propina == '20%'){
        monto_final = monto_total * 1.20
    }

    // Se envia la variable para ser exhibida por HTML.
    presultado.innerText = ('Propina: ' + propina + ' CLP')
    tresultado.innerText = ('Total a pagar: ' + monto_final + ' CLP')
}


