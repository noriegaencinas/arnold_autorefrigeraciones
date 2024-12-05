document.getElementById("form-validate").addEventListener("submit", async function (event) {
  event.preventDefault(); // Evita el envío tradicional del formulario.

  // Obtén los valores de los campos.
  const folio = document.getElementById("folio_numero").value.trim();
  const importe = document.getElementById("importe_total").value.trim();
  const fecha = document.getElementById("fecha_transaccion").value.trim();

  try {
    // Realiza la petición al servidor.
    const response = await fetch("/menu/facturas/validar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ folio, importe, fecha }),
    });

    const result = await response.json();

    if (result.status === "success") {
      // Datos válidos: Aplica estilos de éxito.
      document.querySelectorAll(".form-control").forEach((input) => {
        input.classList.remove("is-invalid");
        input.classList.add("is-valid");
        input.disabled = true; // Deshabilitar los inputs
      });

      // Cambiar el texto y color del botón
      const validateButton = document.getElementById("validate-button");
      validateButton.innerHTML = `
        <img src="/static/icons/check2.svg" alt="check icon" height="20px"> Siguiente
      `;
      validateButton.classList.remove("btn-warning");
      validateButton.classList.add("btn-success");

      // Redirigir solo si el usuario hace clic nuevamente después de la validación.
      validateButton.addEventListener("click", function () {
        window.location.href = "/menu/facturas/datos";
      });
    } else {
      // Datos inválidos: Aplica estilos de error.
      document.querySelectorAll(".form-control").forEach((input) => {
        input.classList.remove("is-valid");
        input.classList.add("is-invalid");
      });

    }
  } catch (error) {
    console.error("Error al validar:", error);
    alert("Ocurrió un error inesperado. Por favor, intenta nuevamente.");
  }
});
