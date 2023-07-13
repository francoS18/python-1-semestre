// Todos los datos extraidos del html se almacenan en variables en JS.

// Aqui se extrae el nombre.
const nombre = document.getElementById('txtnombre');
// Se extrae el peso junto con su valor.
const peso_kg = document.getElementById('numpeso');
// Se extrae el peso junto con su valor.
const altura_m = document.getElementById('numaltura');
// Se extrae la edad .
const edad = document.getElementById('numedad');
// Se extrae el genero ya sea masculino o femenino.
const genero = document.getElementById('gen');
// Se extrae la cantidad de actividad fisica.
const actividad_fisica = document.getElementById('act');
// Se extrae el boton con el cual se interactua para enviar los datos.
const calcular = document.getElementById('boton_calcular');
// Se establece una variable que almacenara el min y el max de los input de tipo numerico.
const limitadores = document.querySelectorAll('input[type="number"]')

// Se recorre dentro de todos los datos que contenga la variable limitadores y se crea una funcion donde se hara el resto del proceso.
limitadores.forEach(function (limitador) {

    // Se agrega un evento donde al recibir un input se ira modificando el valor y con una funcion donde se compararan los datos limitantes  con las variables.
    limitador.addEventListener('input', function prueba(){

        // Se crean las variables donde se almacenan los datos limitantes y el numero ingresado.
        const numero = parseFloat(limitador.value);
        const min = parseFloat(limitador.min);
        const max = parseFloat(limitador.max);
        
        // Se realiza la comparacion donde el numero ingresado es comparado con el numero minimo definido en el HTML.
        if (numero < min) {
            limitador.value = min;
        
        // Se realiza la comparacion donde el numero ingresado es comparado con el numero maximo definifo en el HTML.
        } else if (numero > max){
            limitador.value = max;
        }
    })
})

// Se extraen todos los metodos por los cuales se enviara la informacion para ser exhibida en el html.
const iresultado = document.getElementById('resultado_imc')
const cresultado = document.getElementById('clasificacion_imc')
const aresultado = document.getElementById('actividad_fisica')
const eresultado = document.getElementById('estado_nutricional')

// Aqui lo que hace es realizar una accion cuando el boton calcular tenga interaccion.
calcular.addEventListener('click', calculadora_imc)
// calcular.addEventListener('click', indice_actividad)

// Se crea una funcion donde se hara todo el proceso para calcular el valor del IMC.
function calculadora_imc(){

    // Se transforman los datos desde string a int/float
    peso = parseInt(peso_kg.value)
    alturaa = parseFloat(altura_m.value)

    // Se calcula el valor el IMC realizando la operacion correspondiente.
    let resultado_imc = peso/alturaa**2

    // Se crea una variable donde se almacenara la clasificacion del IMC.
    let clasificacionimc;

    // Se crea una variable donde se almacenara el estado nutricional.
    let estado_nutricional

    // Se inicia un if donde se iran comparando parametro a parametro hasta que alguno se cumpla.
    if (resultado_imc <=18.4){
        clasificacionimc = ('Bajo peso');
        estado_nutricional = ('Necesita atención especializada')
    } else if (resultado_imc>=18.5 && resultado_imc<=24.9){
        clasificacionimc = ('Peso normal');
        estado_nutricional = ('Estado nutricional adecuado')
    } else if (resultado_imc>=25.0 && resultado_imc<=29.9){
        clasificacionimc = ('Sobrepeso');
        estado_nutricional = ('Necesita atencion especializada')
    } else if (resultado_imc>=30.0 && resultado_imc<=34.9){
        clasificacionimc = ('Obesidad grado 1')
        estado_nutricional = ('Necesita atencion especializada')
    } else if (resultado_imc>=35.0 && resultado_imc<=39.9){
        clasificacionimc = ('Obesidad grado 2')
        estado_nutricional = ('Necesita atencion especializada')
    } else if (resultado_imc>40.0){
        clasificacionimc = ('Obesidad grado 3')
        estado_nutricional = ('Necesita atencion especializada')
    }

    // Se extrae el index para saber que numero de opcion eligio el usuario
    let actividadindex = actividad_fisica.selectedIndex;

    // Se utiliza el index para encontrar la opcion seleccionada por el usuario
    let actividadelegida = actividad_fisica.options[actividadindex];

    // Finalmente se guarda en una variable y se cambia a tipo texto para que pueda ser leida como un string
    let opcion_seleccionada = actividadelegida.text;

    // Se define la variable donde se almacenara el resultado de actividad.
    let resultado_act

    // Se inicia un if donde se comparan todos los casos posibles hasta encontrar el que coincide con lo solicitado
    if (opcion_seleccionada == 'Sedentario'){
        resultado_act = peso * 1.2
    } else if (opcion_seleccionada == 'Moderado'){
        resultado_act = peso * 1.55
    } else if (opcion_seleccionada == 'Activo'){
        resultado_act = peso * 1.9
    }

    // Se envia el resultado del IMC al html para ser exhibido en pantalla.
    iresultado.innerText = 'IMC: ' + resultado_imc.toFixed(2)
    cresultado.innerText = 'Clasificacion: ' + clasificacionimc 
    aresultado.innerText = 'Gasto Energetico Diario: ' + resultado_act +' kcal'
    eresultado.innerText = 'Estado Nutricional :' + estado_nutricional
}
