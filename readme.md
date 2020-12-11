# Descripción del proyecto "Inventario"
###Projecto desarrollado en Django

Este es el proyecto un diseño de un sitio web, que permite manejar el inventario de productos de una tienda, se puede tambien administrar la informacion de los clientes, tambien la informacion de  las ordenes de compra y las ordenes de cotizacion.

El sitio web cuenta con una nav-bar que tienen tres secciones:
- ####Inventario
- ####Crear orden
- ####Reportes

Desde la seccion **Inventario** se puede observar la informacion de los productos y la cantidad que existe. Tambien se puede modificar y crear un producto nuevo a travez de los botones que tiene la vista, boton "Modify" y "Add New Product" respectivamente.

#####NOTA:  **Las tablas tienen una entrada de busqueda la cual permite filtrar la informacion que se encuentre estas. Esto es gracias a la siguiente funcion JavaScript que se encuentra en el archivo function.js (ruta *static/inventory*) :**
```javascript
function search_item(){
	....
}
```
La seccion **Crear Orden** permite tomar los distintos productos que existen en el inventario y agregarlos a la lista de la orden en la parte inferior. Tambien permite tomar los datos del cliente (nombre, apellido, identificacion y telefono) los cuales van asociados a la orden. Si el usuario es nuevo se crea una nueva entrada en la base de datos, si el usuario ya existe solo se relaciona la orden al usuario existente. Desde esta seccion se puede acceder tres listas; lista de ordenes de compra, lista de ordesde de cotizaciones, lista de clientes, por medio de los botones; "Show Sales", "Show Quotes" y "Show Clients". 

La seccion **Reportes** Muestra un informe detallado en dos bloques tipo tarjeta, la primera tarjeta muestra el total de ventas, los clientes y  las cotizaciones, la segunda tarjeta muestra el total de productos vendidos y el total de productos en inventario.

La **lista de ordenes **  tiene un campo llamado "No. orden" , desde aqui se puede acceder a la informacion detallada de la orden y posteriormente se puede modificar la descripcion, el valor y tipo de esta.

La** lista de clientes** tiene un campo llamado "Identificacion", haciendo click se puede acceder a la informacion detallada del cliente y las ordenes relacionadas. Tambien se puede modificar la informacion del cliente.

Todo el codigo **CSS** (archivo style.css) de la pagina web fue creado en la ruta *static/inventory* de la aplicacion. No fue necesario utilizar bootstrapp u otras herramientas relacionadas. De igual forma las funciones **JavaScrip**  implementadas (archivo function.js) permiten enviar peticiones y modificar el DOM del documento para ocultar o mostrar los distintos elementos que lo componen.

Los modelos creados en el archivo "**models.py**" de la aplicacion "**Invenrario**" fueron 4:
```python
class User(AbstractUser):
    pass

class Product(models.Model):
    ..
    

class Client(models.Model):
   ...


class Order(models.Model):
    ...

```
La aplicacion tiene un diseño responsivo para moviles, el cual se definio que se cargarian cuando el navegador tenga una vista con un ancho maximo de 512 pixeles:

```css
/* Mobile Styles */
@media only screen and (max-width: 512px) {
   
   .....
   
    }

```