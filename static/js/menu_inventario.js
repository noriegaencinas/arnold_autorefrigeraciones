document.addEventListener('DOMContentLoaded', function () {
    const rows = document.querySelectorAll('#tabla_empleados tbody tr');
  
    rows.forEach(row => {
      row.addEventListener('click', function () {
        // Extract information from the clicked row
        const nombre = row.cells[1].textContent;
        const cargo = row.cells[2].textContent;
        const numero = row.cells[3].textContent;
        const correo = row.cells[4].textContent;
        const fecha_contratacion = row.cells[5].textContent;
        const horario_trabajo = row.cells[6].textContent;
        const salario = row.cells[7].textContent;
        const automoviles_asignados = row.cells[8].textContent;
  
        // Update the content of the details card
        document.getElementById('details_card').innerHTML = `
        <img src="/static/icons/person-square.svg" class="card-img-top my-3 mx-auto" style="max-width: 80%;" alt="...">
        <div class="card-body">
          <div class="row">
            <div class="col">
              <h5 class="card-title">Nombre</h5>
              <p class="card-text">${nombre}</p>
              <h5 class="card-title">Cargo</h5>
              <p class="card-text">${cargo}</p>
              <h5 class="card-title">Fecha de contratación</h5>
              <p class="card-text">${fecha_contratacion}</p>
              <h5 class="card-title">Horario de trabajo</h5>
              <p class="card-text">${horario_trabajo}</p>
              <h5 class="card-title">Numero</h5>
              <p class="card-text">${numero}</p>
              <h5 class="card-title">Correo electrónico</h5>
              <p class="card-text">${correo}</p>
              <h5 class="card-title">Salario</h5>
              <p class="card-text">${salario}</p>
              <h5 class="card-title">Reparaciones asignadas</h5>
              <p class="card-text">${automoviles_asignados}</p>
            </div>
          </div>
        </div>
        `;
      });
    });
  });