document.addEventListener('DOMContentLoaded', function () {
    const rows = document.querySelectorAll('#tabla_empleados tbody tr');
  
    rows.forEach(row => {
      row.addEventListener('click', function () {
        // Extract information from the clicked row
        const modelo = row.cells[1].textContent;
        const placa = row.cells[2].textContent;
        const nombre_propietario = row.cells[3].textContent;
        const motivo_ingreso = row.cells[4].textContent;
        const fecha_ingreso = row.cells[5].textContent;
        const notas = row.cells[6].textContent;
        const marca = row.cells[7].textContent;
        const telefono_propietario = row.cells[8].textContent;
        const correo_propietario = row.cells[8].textContent;
  
        // Update the content of the details card
        document.getElementById('details_card').innerHTML = `
        <img src="/static/icons/person-square.svg" class="card-img-top my-3 mx-auto" style="max-width: 80%;" alt="...">
        <div class="card-body">
          <div class="row">
            <div class="col">
              <h5 class="card-title">Marca</h5>
              <p class="card-text">${salario}</p>
              <h5 class="card-title">Modelo</h5>
              <p class="card-text">${nombre}</p>
              <h5 class="card-title">Placa</h5>
              <p class="card-text">${cargo}</p>
              <h5 class="card-title">Nombre del propietario</h5>
              <p class="card-text">${fecha_contratacion}</p>
              <h5 class="card-title">Motivo de ingreso</h5>
              <p class="card-text">${horario_trabajo}</p>
              <h5 class="card-title">Fecha de ingreso</h5>
              <p class="card-text">${numero}</p>
              <h5 class="card-title">Notas</h5>
              <p class="card-text">${correo}</p>              
              <h5 class="card-title">Celular de contacto</h5>
              <p class="card-text">${automoviles_asignados}</p>
              <h5 class="card-title">Correo de</h5>
              <p class="card-text">${automoviles_asignados}</p>
            </div>
          </div>
        </div>
        `;
      });
    });
  });