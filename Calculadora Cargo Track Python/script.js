// --- Funciones de la Calculadora --- //

// Función para convertir kilogramos a libras
function convertKgToLb() {
    let kgInput = document.getElementById("kilos").value;
    const lbInput = document.getElementById("libras");

    // Reemplazar comas por puntos y forzar el cálculo
    kgInput = kgInput.replace(',', '.');

    if (kgInput !== "") {
        const kilos = parseFloat(kgInput);
        lbInput.value = (isNaN(kilos) ? "" : (kilos * 2.20462262185).toFixed(5)); // Conversión más precisa de kg a lb
    } else {
        lbInput.value = ""; // Limpiar el campo si no hay valor en kg
    }
}

// Función para convertir libras a kilogramos
function convertLbToKg() {
    let lbInput = document.getElementById("libras").value;
    const kgInput = document.getElementById("kilos");

    // Reemplazar comas por puntos y forzar el cálculo
    lbInput = lbInput.replace(',', '.');

    if (lbInput !== "") {
        const libras = parseFloat(lbInput);
        kgInput.value = (isNaN(libras) ? "" : (libras * 0.45359237).toFixed(5)); // Conversión más precisa de lb a kg
    } else {
        kgInput.value = ""; // Limpiar el campo si no hay valor en lb
    }
}

// Validar el formulario para evitar errores de entrada
function validateForm(event) {
    event.preventDefault(); // Evita el envío del formulario

    let kilos = document.getElementById("kilos").value;
    let libras = document.getElementById("libras").value;
    let ancho = document.getElementById("ancho").value;
    let largo = document.getElementById("largo").value;
    let alto = document.getElementById("alto").value;
    let cantidad = document.getElementById("cantidad").value;
    const envioTipo = document.querySelector('input[name="envio-tipo"]:checked').value;

    // Reemplazar comas por puntos en los campos de peso y medidas
    kilos = kilos.replace(',', '.');
    libras = libras.replace(',', '.');
    ancho = ancho.replace(',', '.');
    largo = largo.replace(',', '.');
    alto = alto.replace(',', '.');

    // Convertir los valores a números (si no son válidos, forzar 0)
    const kilosNum = parseFloat(kilos) || 0;
    const librasNum = parseFloat(libras) || 0;
    const anchoNum = parseFloat(ancho) || 0;
    const largoNum = parseFloat(largo) || 0;
    const altoNum = parseFloat(alto) || 0;
    const cantidadNum = parseInt(cantidad) || 0;

    // Verificar si todos los campos están en 0
    if (kilosNum === 0 && librasNum === 0 && anchoNum === 0 && largoNum === 0 && altoNum === 0 && cantidadNum === 0) {
        // Mostrar un mensaje de advertencia si todo está en 0
        alert("Por favor, ingresa valores diferentes de 0 para calcular el costo del envío.");
        return; // Salir de la función sin ejecutar cálculos
    }

    // Pasar los valores convertidos a la función de cálculo
    calculateWeightsAndVolumes(kilosNum, librasNum, anchoNum, largoNum, altoNum, cantidadNum, envioTipo);
}

// Calcular y mostrar los pesos, volúmenes, conversiones y costos de envío
function calculateWeightsAndVolumes(kilos, libras, ancho, largo, alto, cantidad, envioTipo) {
    // Convertir medidas de pulgadas a centímetros (1 pulgada = 2.54 cm)
    const anchoCm = ancho * 2.54;
    const largoCm = largo * 2.54;
    const altoCm = alto * 2.54;

    // Calcular volumen en cm^3 y convertir a pies cúbicos (1 ft^3 = 28316.8466 cm^3)
    const volumenCm3 = anchoCm * largoCm * altoCm;
    const volumenFT3 = volumenCm3 / 28316.8466;

    // Calcular peso por pie cúbico
    const pesoFT3 = libras / volumenFT3;

    // Calcular el costo de envío según el tipo de envío
    let costoEnvio = 0;
    if (envioTipo === "maritimo") {
        costoEnvio = volumenFT3 * 38; // $38 por pie cúbico para marítimo
    } else if (envioTipo === "aereo") {
        costoEnvio = libras * 7; // $7 por libra para aéreo
    }

    // Calcular el costo del seguro si está seleccionado
    let seguroCosto = 0;
    const seguroChecked = document.getElementById("seguro-envio").checked;
    const valorDeclarado = parseFloat(document.getElementById("valor-declarado").value) || 0;
    
    if (seguroChecked && valorDeclarado > 0) {
        const porcentajeSeguro = 0.02; // Supongamos un 2% del valor declarado
        seguroCosto = valorDeclarado * porcentajeSeguro;
        costoEnvio += seguroCosto; // Sumamos el costo del seguro al costo total de envío
    }

    // Multiplicar el costo total por la cantidad de paquetes
    const costoTotal = (costoEnvio * cantidad).toFixed(2);

    // Mostrar los resultados en los campos correspondientes
    document.getElementById("peso-lb").innerText = libras.toFixed(2) + " Lb";
    document.getElementById("peso-kg").innerText = kilos.toFixed(2) + " Kg";
    document.getElementById("volumen-lb").innerText = (libras * volumenFT3).toFixed(5) + " Lb";
    document.getElementById("volumen-kg").innerText = (kilos * volumenFT3).toFixed(5) + " Kg";
    document.getElementById("peso-ft3").innerText = pesoFT3.toFixed(5) + " FT3";
    document.getElementById("vol-ft3").innerText = volumenFT3.toFixed(5) + " FT3";

    // Mostrar la conversión de pulgadas a centímetros
    document.getElementById("ancho-cm").innerText = anchoCm.toFixed(2) + " cm";
    document.getElementById("largo-cm").innerText = largoCm.toFixed(2) + " cm";
    document.getElementById("alto-cm").innerText = altoCm.toFixed(2) + " cm";

    // Mostrar el costo de envío
    document.getElementById("costo-envio").innerText = "$" + costoTotal;

    // Mostrar el costo del seguro si aplica
    if (seguroCosto > 0) {
        document.getElementById("costo-envio").innerText += " (incluye $" + seguroCosto.toFixed(2) + " de seguro)";
    }

    // Mostrar la nota de que los montos son estimados
    document.getElementById("nota").style.display = "block";

    // Mostrar el título de resultados, la sección de resultados y la nota
    document.getElementById("resultados-titulo").style.display = "block";
    document.getElementById("results").style.display = "block";
    document.getElementById("nota").style.display = "block";

    // Mostrar el botón pequeño después de los cálculos
    document.getElementById("small-button").style.display = "inline-block";
}

// Función para reiniciar la calculadora
function resetCalculator() {
    document.getElementById("calculator-form").reset();
    document.getElementById("results").style.display = "none";
    document.getElementById("nota").style.display = "none";
    document.getElementById("resultados-titulo").style.display = "none";
    document.getElementById("small-button").style.display = "none";
}

// Función para alternar la visualización del valor declarado
function toggleValorDeclarado() {
    var seguroEnvio = document.getElementById('seguro-envio');
    var valorDeclaradoInput = document.getElementById('valor-declarado-input');
    if (seguroEnvio.checked) {
        valorDeclaradoInput.style.display = 'block';
    } else {
        valorDeclaradoInput.style.display = 'none';
    }
}

// Función para validar y formatear el valor declarado
function formatValorDeclarado() {
    let valorInput = document.getElementById("valor-declarado").value;

    // Reemplazar comas por puntos para que funcione como decimal
    valorInput = valorInput.replace(',', '.');

    // Solo permitir números y un punto decimal
    valorInput = valorInput.replace(/[^0-9.]/g, '');

    // Evitar múltiples puntos decimales
    if ((valorInput.match(/\./g) || []).length > 1) {
        valorInput = valorInput.substring(0, valorInput.length - 1);
    }

    // Asignar el valor formateado de vuelta al input
    document.getElementById("valor-declarado").value = valorInput;
}

// Agregar el evento al campo de valor declarado para que valide cuando el usuario deje el campo (blur)
document.getElementById("valor-declarado").addEventListener("blur", formatValorDeclarado);


// --- Cubo 3D --- //

// Configurar la escena, cámara y renderizador de Three.js
let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
let renderer = new THREE.WebGLRenderer();
renderer.setSize(400, 400);  // Tamaño del canvas para el cubo
document.body.appendChild(renderer.domElement); // Agregar el renderizador al DOM

// Crear el cubo con dimensiones iniciales
let geometry = new THREE.BoxGeometry(1, 1, 1);
let material = new THREE.MeshBasicMaterial({color: 0x00ff00, wireframe: true});  // Wireframe para visualizar mejor
let cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.z = 5;  // Alejar un poco la cámara para ver el cubo

// Función de renderizado (loop)
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}
animate();

// Actualizar el tamaño del cubo en tiempo real según los inputs
document.getElementById("ancho").addEventListener("input", () => updateCubeSize());
document.getElementById("largo").addEventListener("input", () => updateCubeSize());
document.getElementById("alto").addEventListener("input", () => updateCubeSize());

function updateCubeSize() {
    const ancho = parseFloat(document.getElementById("ancho").value) || 1;
    const largo = parseFloat(document.getElementById("largo").value) || 1;
    const alto = parseFloat(document.getElementById("alto").value) || 1;

    // Actualizar la geometría del cubo
    cube.scale.set(ancho, alto, largo);  // El cambio se refleja en tiempo real
}
