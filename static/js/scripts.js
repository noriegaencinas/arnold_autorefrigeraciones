document.addEventListener('DOMContentLoaded', (event) => {
    // Selecciona todos los elementos con la clase "only-numbers"
    const inputs = document.querySelectorAll('.only-numbers');

    // Función para permitir solo teclas numéricas y ciertas teclas de control
    function allowOnlyNumbers(event) {
        const keyCode = event.which ? event.which : event.keyCode;

        // Permitir teclas de control (backspace, tab, enter, escape, delete y flechas)
        if (
            keyCode === 8 || // backspace
            keyCode === 9 || // tab
            keyCode === 13 || // enter
            keyCode === 27 || // escape
            keyCode === 46 || // delete
            (keyCode >= 35 && keyCode <= 39) // home, end, left, right
        ) {
            return;
        }

        // Permitir números (0-9)
        if (keyCode < 48 || keyCode > 57) {
            event.preventDefault();
        }
    }

    // Función para eliminar caracteres no numéricos en el evento input
    function sanitizeInput(event) {
        const value = event.target.value;
        event.target.value = value.replace(/[^0-9]/g, '');
    }

    // Función para validar que el campo no esté vacío
    function validateNotEmpty(event) {
        const value = event.target.value.trim(); // Elimina espacios en blanco al principio y al final
        if (value === '') {
            event.preventDefault(); // Detiene el envío del formulario si el campo está vacío
            alert('El campo no puede estar vacío');
        }
    }

    // Aplica los eventos a todos los inputs seleccionados
    inputs.forEach(input => {
        input.addEventListener('keypress', allowOnlyNumbers);
        input.addEventListener('input', sanitizeInput);
        input.form.addEventListener('submit', validateNotEmpty); // Agrega la validación al evento submit del formulario asociado
    });
});