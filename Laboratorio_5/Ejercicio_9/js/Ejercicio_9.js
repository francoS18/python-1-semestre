//############# Iniciando variables #############//

//Se seleccionan elementos del documento (HTML) por su id y se guardan en constantes.
const phamburguesa = document.getElementById('hamburguesa');
const ppizza = document.getElementById('pizza');
const photdog = document.getElementById('hot_dog');
const pensalada = document.getElementById('ensalada');
const ppapasfritas = document.getElementById('papas_fritas');

//Se selecciona el boton "Calcular" a travez de su id
const calcular = document.getElementById('boton_calcular');

//Se selecciona todos los elementos "input" del tipo 'number' en el documento (HTML) y los almacena en la constante limitadores.
//Se almacenan con el tipo de dato "NodeList", en este caso, estatico
const limitadores = document.querySelectorAll('input[type="number"]');

//############# Validacion de datos #############// 

//Opera sobre cada uno de los elementos de entrada seleccionados (es decir, cada uno de los campos de entrada numéricos en la página) y 
//ejecuta la función proporcionada para cada uno.
limitadores.forEach(function (limitador) {

    //Agrega un "escuchador de eventos" al elemento actual en la iteración (limitador). Este escuchador se activará cada vez que el usuario modifique 
    //el valor de entrada de este elemento (es decir, cada vez que se dispare el evento 'input').
    limitador.addEventListener('input', function limitadorr() {

        //Extrae el valor actual de las cantidades ingresadas y lo convierte a un número de punto flotante, almacenándolo en la constante numero.
        const numero = parseFloat(limitador.value);
        //Extrae el valor mínimo permitido para este elemento desde su atributo min, convirtiéndolo a un número de punto flotante y almacenándolo en la constante min.
        const min = parseInt(limitador.min);
        //Extrae el valor maximo permitido para este elemento desde su atributo max, convirtiéndolo a un número de punto flotante y almacenándolo en la constante max.
        const max = parseInt(limitador.max);
        
        //Si el valor actual de "numero" es menor que el mínimo permitido, lo ajusta al valor mínimo definido.
        if (numero < min) {
            limitador.value = min;
        }

        //Si el valor actual de "numero" es mayor que el maximo permitido, lo ajusta al valor maximo definido.
        else if (numero > max){
            limitador.value = max;
        }

        //Si "numero" no es un entero, lo ajusta a "1"
        if (!Number.isInteger(numero)) {
            limitador.value = 1
        }
    })
});

//############# Obteniendo los elementos "output" del documento #############//

//Se obtiene el elemento a travez de sus id en el documento y lo almacena en la constante.
//Se espera que muestren los resultados del "valor", "iva", y "valor neto"
const tresultado = document.getElementById('total_resultado');
const iresultado = document.getElementById('iva_resultado');
const vresultado = document.getElementById('valor_resultado');

//############# Declarando la funcion para realizar los calculos #############//

//Declarando la funcion
function calcularPedido() {

    //Intentamos obtener los valores de los elementos seleccionados al incicio del script.
    //Lo convertimos a un número entero. Si no puede ser convertido se asume un valor de 0.
    const valor_hamburguesa = parseInt(phamburguesa.value) || 0;
    const valor_pizza = parseInt(ppizza.value) || 0;
    const valor_hotdog = parseInt(photdog.value) || 0;
    const valor_ensalada = parseInt(pensalada.value) || 0;
    const valor_papasfritas = parseInt(ppapasfritas.value) || 0;
    
    // Se crean variables donde se almacenarán los datos solicitados, para operarlos mas tarde.
    let resultado = 0;
    let iva = 0;
    let valor_final = 0;
    
    // Se realiza la suma de los valores, cuyo resultado será multiplicado por los precios correspondientes.
    resultado += valor_hamburguesa * 3000;
    resultado += valor_pizza * 4200;
    resultado += valor_hotdog * 2500;
    resultado += valor_ensalada * 1600;
    resultado += valor_papasfritas * 2000;
    
    // Se realizan las operaciones solicitadas para obtener el IVA y el valor final.
    iva = resultado * 0.19;
    valor_final = resultado * 1.19;
    
    //Estableciendo los textos a los elementos de salida. Se envían los datos al documento, que le permitirán al usuario visualizar los resultados.
    tresultado.innerText = 'Total del pedido: $' + resultado + ' CLP';
    iresultado.innerText = 'IVA: $' + iva + ' CLP';
    vresultado.innerText = 'Valor neto: $' + valor_final + ' CLP';
}

//Agrega un "escuchador de eventos" al elemento "calcular". Cuando se hace clic en este elemento, se invoca la función calcularPedido.
calcular.addEventListener('click', calcularPedido);



    