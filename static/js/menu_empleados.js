{% extends 'base.html' %} 

{% block styling %}
  {{ super() }}
{% endblock %}

{% block nombre_menu %}Gestion de empleados{% endblock%} 
{% block content %}
<!-- Agregar dentro de este bloque el codigo del menu empleados-->
<div class="container parent">
  <div class="row">    
    <div class="col-lg-8 col-sm-12 col-10 child">                  
      <nav class="navbar">
        <div class="container-fluid">
          <form class="d-flex" role="search", action="{{url_for('select_empleado_by_filter')}}", method="POST">
            <input class="form-control me-2 col-lg-3" type="search" placeholder="Empleado" aria-label="Search" name="filtro">
            <button class="btn btn-outline-success col-lg-3" type="submit">Buscar</button>
          </form>
          <button type="button" class="btn btn-primary col-lg-3" data-bs-toggle="modal" data-bs-target="#ModalCreateEmpleado">      
            Agregar empleado
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
              <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"/>
            </svg>
          </button>  
        </div>
      </nav>    
    <div class="table-responsive">
      <table class="table table-hover" id="tabla_empleados">
        <thead class="thead-dark">
          <tr>            
            <th scope="col">#</th>
            <th scope="col">Nombre</th>
            <th scope="col">Cargo</th>            
            <th scope="col">Numero</th>
            <th scope="col">Correo</th>
            <th scope="col">Acciones</th>            
          </tr>
        </thead>
        <tbody>
          {% for empleado in empleados[0] %}
            <tr>
              <th scope="row">{{ empleado[0] }}</th>
              <td>{{ empleado[1] }}</td>
              <td>{{ empleado[2] }}</td>            
              <td>{{ empleado[6] }}</td>            
              <td>{{ empleado[7] }}</td>        
              <td>       
                <button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#modal_update{{empleado[0]}}">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                    <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                    <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
                  </svg>
                </button>         
                <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#modal_delete{{empleado[0]}}">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                    <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
                  </svg>
                </button>                
              </td>            
            </tr>
            <!-- Modal of update empleado-->
            <div class="modal fade" id="modal_update{{empleado[0]}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" >
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Actualizar la información del empleado</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    Modifica los campos necesarios
                    <form action="{{url_for('actualizar_empleado', id_empleado=empleado[0])}}", method="POST">
                      <div class="mb-1">
                        <label for="recipient-name" class="col-form-label">Nombre completo</label>
                        <input name="nombre_completo" type="text" class="form-control" id="recipient-name" value="{{ empleado[1] }}">
                      </div>
                      <div class="mb-1">
                        <label for="message-text" class="col-form-label">Cargo</label>
                        <input name="cargo" type="text" class="form-control" id="recipient-name" value="{{ empleado[2] }}">
                      </div>
                      <div class="mb-1">
                        <label for="recipient-name" class="col-form-label">Fecha de contratación</label>
                        <input name="fecha_contratacion" type="text" class="form-control" id="recipient-name" value="{{ empleado[3] }}">
                      </div>
                      <div class="mb-1">
                        <label for="recipient-name" class="col-form-label">Horario de trabajo</label>
                        <input name="horario_trabajo" type="text" class="form-control" id="recipient-name" value="{{ empleado[5] }}">
                      </div>
                      <div class="mb-1">
                        <label for="recipient-name" class="col-form-label">Número</label>
                        <input name="numero_contacto" type="text" class="form-control" id="recipient-name" value="{{ empleado[6] }}">
                      </div>
                      <div class="mb-1">
                        <label for="recipient-name" class="col-form-label">Correo electrónico</label>
                        <input name="correo_electronico" type="text" class="form-control" id="recipient-name" value="{{ empleado[7] }}">
                      </div>
                      <div class="mb-1">
                        <label for="recipient-name" class="col-form-label">Salario:</label>
                        <input name="salario" type="text" class="form-control" id="recipient-name" value="{{ empleado[8] }}">
                      </div>      
                      <div class="modal-footer">        
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" class="btn btn-primary">Guardar</button>
                      </div>  
                    </form>
                  </div>      
                </div>
              </div>
            </div>
            <!-- Modal of delete empleado-->
            <div class="modal fade" id="modal_delete{{empleado[0]}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <form action="{{url_for('eliminar_empleado', id_empleado=empleado[0])}}" method="POST">
                    <div class="modal-header">
                      <h1 class="modal-title fs-5" id="exampleModalLabel">Confirmar eliminación</h1>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                      ¿Estás seguro de que deseas eliminar este empleado?
                      <label for="recipient-name" class="col-form-label">Nombre:</label>
                      <input name="salario" type="text" class="form-control" id="recipient-name" value="{{ empleado[1] }}" disabled>                    
                      <label for="recipient-name" class="col-form-label">Cargo:</label>
                      <input name="salario" type="text" class="form-control" id="recipient-name" value="{{ empleado[2] }}" disabled>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                      <button type="submit" class="btn btn-danger" id="confirmDeleteButton">Confirmar</a>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          {% endfor %}
          </tbody>
        </table>
      </div>
      <!-- this is the navbar for the employees -->
      <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
          <li class="page-item disabled">
            <a class="page-link">Anterior</a>
          </li>          
          {% for i in range(empleados[1]) %}
            <li class="page-item"><a class="page-link" href="{{url_for('menu_empleados', page=i+1)}}">{{i+1}}</a></li>          
          {% endfor %}
          <li class="page-item">
            <a class="page-link" href="#">Siguiente</a>
          </li>
        </ul>
      </nav>
    </div>

    <div class="col-lg-4 col-sm-6 col-10 child">
      <div class="card" style="width: 18rem;" id="details_card">
        <img src="/static/icons/person-square.svg" class="card-img-top" alt="...">
        <div class="card-body">
          <div class="row">
            <div class="col">
              <h5 class="card-title">Nombre</h5>
              <p class="card-text">...</p>
              <h5 class="card-title">Cargo</h5>
              <p class="card-text">...</p>
              <h5 class="card-title">Fecha de contratación</h5>
              <p class="card-text">...</p>
              <h5 class="card-title">Horario de trabajo</h5>
              <p class="card-text">...</p>
            </div>
              <div class="col">
              <h5 class="card-title">Número</h5>
              <p class="card-text">...</p>
              <h5 class="card-title">Correo electrónico</h5>
              <p class="card-text">...</p>
              <h5 class="card-title">Salario</h5>
              <p class="card-text">...</p>    
            </div>
          </div>
        </div>
      </div>
    </div>    
  </div>
</div>

<!-- Modal of create empleado-->
<div class="modal fade" id="ModalCreateEmpleado" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" >
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Agregar nuevo empleado</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        Introduce la siguiente información para dar de alta al nuevo empleado
        <form action="{{ url_for('crear_empleado') }}", method="POST">
          <div class="mb-1">
            <label for="recipient-name" class="col-form-label">Nombre completo</label>
            <input name="nombre_completo" type="text" class="form-control" id="recipient-name">
          </div>
          <div class="mb-1">
            <label for="message-text" class="col-form-label">Cargo</label>
            <input name="cargo" type="text" class="form-control" id="recipient-name">
          </div>
          <div class="mb-1">
            <label for="recipient-name" class="col-form-label">Fecha de contratación</label>
            <input name="fecha_contratacion" type="text" class="form-control" id="recipient-name">
          </div>
          <div class="mb-1">
            <label for="recipient-name" class="col-form-label">Horario de trabajo</label>
            <input name="horario_trabajo" type="text" class="form-control" id="recipient-name">
          </div>
          <div class="mb-1">
            <label for="recipient-name" class="col-form-label">Número</label>
            <input name="numero_contacto" type="text" class="form-control" id="recipient-name">
          </div>
          <div class="mb-1">
            <label for="recipient-name" class="col-form-label">Correo electrónico</label>
            <input name="correo_electronico" type="text" class="form-control" id="recipient-name">
          </div>
          <div class="mb-1">
            <label for="recipient-name" class="col-form-label">Salario:</label>
            <input name="salario" type="text" class="form-control" id="recipient-name">
          </div>      
          <div class="modal-footer">        
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="submit" class="btn btn-primary">Confirmar</button>
          </div>  
        </form>
      </div>      
    </div>
  </div>
</div>

<div class="toast-container position-fixed bottom-0 end-0 p-3">
  <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <img src="..." class="rounded me-2" alt="...">
      <strong class="me-auto">Bootstrap</strong>      
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      El empleado ha sido eliminado correctamente
    </div>
  </div>
</div>

<script src="/static/js/menu_empleados.js"></script>
{% endblock %}