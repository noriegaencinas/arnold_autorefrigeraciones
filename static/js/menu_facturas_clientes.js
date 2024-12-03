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
        document.querySelectorAll(".form-control").forEach(input => {
          input.classList.remove("is-invalid");
          input.classList.add("is-valid");
        });        
      } else {
        // Datos inválidos: Aplica estilos de error.
        document.querySelectorAll(".form-control").forEach(input => {
          input.classList.remove("is-valid");
          input.classList.add("is-invalid");
        });        
      }
    } catch (error) {
      console.error("Error al validar:", error);
    }
  });
  