 
# Descripción del proyecto "Inventario"
#### Proyecto desarrollado en Django
 
Este es el diseño de un sitio web creado con Django, que permite manejar el inventario de productos de una tienda, donde se puede  administrar la información de los clientes, también la información de  las órdenes de compra y las órdenes de cotización.
 
En primera instancia el sitio web pide el inicio de sesión del usuario, también se puede crear uno nuevo. Accediendo con las respectivas credenciales, el usuario ya puede acceder a la interfaz del sitio web.
 
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/login.png)
 
 
El sitio web cuenta con una nav-bar que tienen tres secciones:
- #### Inventario
- #### Crear orden
- #### Reportes
 
Desde la sección **Inventario** se puede observar la información de los productos y la cantidad que existe. También se puede modificar y crear un producto nuevo a través de los botones que tiene la vista, botón "Modify" y "Add New Product" respectivamente.
 
##### NOTA:  **Las tablas tienen una entrada de búsqueda la cual permite filtrar la información que se encuentra en estas. Esto es gracias a la siguiente función JavaScript que se encuentra en el archivo function.js (ruta *static/inventory*) :**
 
```javascript
function search_item(){
   ....
}
```
La sección **Crear Orden** permite tomar los distintos productos que existen en el inventario y agregarlos a la lista de la orden en la parte inferior. También permite tomar los datos del cliente (nombre, apellido, identificacion y teléfono) los cuales van asociados a la orden. Si el usuario es nuevo se crea una nueva entrada en la base de datos, si el usuario ya existe solo se relaciona la orden al usuario existente. Desde esta sección se puede acceder a tres listas; lista de órdenes de compra, lista de ordenes de cotización, lista de clientes, por medio de los botones; "Show Sales", "Show Quotes" y "Show Clients".
 
La sección **Reportes** Muestra un informe detallado en dos bloques tipo tarjeta, la primera tarjeta muestra el total de ventas, los clientes y  las cotizaciones, la segunda tarjeta muestra el total de productos vendidos y el total de productos en inventario.
 
La **lista de órdenes**  tiene un campo llamado "No. orden" , desde aquí se puede acceder a la información detallada de la orden y posteriormente se puede modificar la descripción, el valor y tipo de esta.
 
La **lista de clientes** tiene un campo llamado "Identificación", haciendo click en este se puede acceder a la información detallada del cliente y las órdenes relacionadas. También se puede modificar la información del cliente.
 
Todo el código **CSS** (archivo style.css) de la página web fue creado en la ruta *static/inventory* de la aplicación. No fue necesario utilizar Bootstrap u otras herramientas relacionadas. De igual forma las funciones **JavaScript**  implementadas (archivo function.js) permiten enviar peticiones y modificar el DOM del documento para ocultar o mostrar los distintos elementos que lo componen.
 
Los modelos creados en el archivo "**models.py**" de la aplicación "**Inventario**" fueron 4:
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
La aplicación tiene un diseño responsivo para móviles, el cual se definió que se cargarán cuando el navegador tenga una vista con un ancho máximo de 512 pixeles:
 
```css
/* Mobile Styles */
@media only screen and (max-width: 512px) {
 
  .....
 
   }
```