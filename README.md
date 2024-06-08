# Backend de Restaurante con Django

Este proyecto es una aplicación backend para la gestión de un restaurante, desarrollada con Django y Django Rest Framework. La aplicación proporciona endpoints para la administración de productos, mesas, restaurantes, órdenes, facturas, meseros y usuarios.

## Requisitos del Proyecto

1. **Endpoints CRUD**:
    - Productos: `/products/products/`
    - Mesas: `/restaurants/tables/`
    - Restaurantes: `/restaurants/restaurants/`
    - Órdenes: `/restaurants/orders/`
    - Facturas: `/restaurants/bills/`
    - Meseros: `/users/waiters/`
    - Usuarios: `/users/users/`

2. **Turnos de Meseros**:
    - Crear turno: `POST /users/waiters/<id>/add_shift/`
    - Datos requeridos:
        ```json
        {
            "start_date": "fecha de inicio del turno",
            "end_date": "fecha de finalización del turno",
            "restaurant": "id del restaurante"
        }
        ```

3. **Filtrar Mesas por Turno Activo**:
    - Mostrar solo mesas relacionadas al turno activo del mesero.

4. **Órdenes de Meseros**:
    - Acceder a las órdenes del mesero: `GET /users/waiters/<id>/orders/`
    - Filtro por órdenes activas: `GET /users/waiters/<id>/orders?active=1`

5. **Permisos de Eliminación**:
    - Solo los managers pueden eliminar facturas: `DELETE /restaurants/bills/<id>/`
    - Managers o `ADMINTABLES` pueden eliminar órdenes: `DELETE /restaurants/orders/<id>/`
    - 
6. **Documentación del Proyecto**:
    - La documentación fue generada con `drf-yasg`

## Uso

Puedes acceder a la documentación automática del API (si usas `drf-yasg`) en:

http://localhost:8000/swagger/ o http://localhost:8000/redoc/
