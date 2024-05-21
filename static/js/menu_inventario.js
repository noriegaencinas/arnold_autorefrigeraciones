document.addEventListener('DOMContentLoaded', function () {
    const rows = document.querySelectorAll('#tabla_inventario tbody tr');
  
    rows.forEach(row => {
      row.addEventListener('click', function () {
        // Extract information from the clicked row
        const nombre = row.cells[1].textContent;        
        const tipo = row.cells[2].textContent;
        const descripcion = row.cells[3].textContent;
        const cantidad = row.cells[3].textContent;
        const precio_compra = row.cells[4].textContent;
        const precio_venta = row.cells[5].textContent;        
  
        // Update the content of the details card
        document.getElementById('details_card').innerHTML = `
        <img src="/static/icons/box-seam-fill.svg" class="card-img-top my-3 mx-auto" style="max-width: 80%;" alt="...">
        <div class="card-body">
          <div class="row">
            <div class="col">
              <h5 class="card-title">Nombre</h5>
              <p class="card-text">${nombre}</p>
              <h5 class="card-title">Tipo</h5>
              <p class="card-text">${tipo}</p>
              <h5 class="card-title">Descripción</h5>
              <p class="card-text">${descripcion}</p>
              <h5 class="card-title">Cantidad</h5>
              <p class="card-text">${cantidad}</p>
              <h5 class="card-title">Precio compra</h5>
              <p class="card-text">${precio_compra}</p>
              <h5 class="card-title">Precio venta</h5>
              <p class="card-text">${precio_venta}</p>
            </div>
          </div>
        </div>
        `;
      });
    });
  });