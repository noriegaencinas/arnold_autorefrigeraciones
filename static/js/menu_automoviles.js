document.addEventListener('DOMContentLoaded', function () {
    const rows = document.querySelectorAll('#tabla_automoviles tbody tr');
  
    rows.forEach(row => {
      row.addEventListener('click', function () {

        // Extract information from the clicked row
        const id_automovil = row.cells[0].textContent;
        const modalId = `#modal_alta${id_automovil}`;
        const modelo = row.cells[1].textContent;
        const placa = row.cells[2].textContent;
        const nombre_propietario = row.cells[3].textContent;
        const motivo_ingreso = row.cells[4].textContent;
        const fecha_ingreso = row.cells[5].textContent;
        const notas = row.cells[6].textContent;
        const marca = row.cells[7].textContent;
        const telefono_propietario = row.cells[8].textContent;
        const correo_propietario = row.cells[9].textContent;
  
        // Update the content of the details card
        document.getElementById('details_card').innerHTML = `
        <img src="/static/icons/car-front-fill.svg" class="card-img-top my-3 mx-auto" style="max-width: 80%;" alt="...">
        <div class="card-body">
          <div class="row">
            <div class="col">
              <h5 class="card-title">Marca</h5>
              <p class="card-text">${marca}</p>
              <h5 class="card-title">Modelo</h5>
              <p class="card-text">${modelo}</p>
              <h5 class="card-title">Placa</h5>
              <p class="card-text">${placa}</p>
              <h5 class="card-title">Nombre del propietario</h5>
              <p class="card-text">${nombre_propietario}</p>
              <h5 class="card-title">Motivo de ingreso</h5>
              <p class="card-text">${motivo_ingreso}</p>
              <h5 class="card-title">Fecha de ingreso</h5>
              <p class="card-text">${fecha_ingreso}</p>
              <h5 class="card-title">Notas</h5>
              <p class="card-text">${notas}</p>              
              <h5 class="card-title">Celular de contacto</h5>
              <p class="card-text">${telefono_propietario}</p>
              <h5 class="card-title">Correo electrónico</h5>
              <p class="card-text">${correo_propietario}</p>         
              <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="${modalId}">Dar de alta</button> 
            </div>
          </div>
        </div>
        `;
      });
    });
  });