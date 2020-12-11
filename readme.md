 
# Description of the project "Inventory"
#### Project developed in Django
 
This is the design of a website created with Django, which allows you to manage the inventory of products in a store, where you can manage customer information, also information about purchase orders and quotation orders.
 
In the first instance the website asks for the user's login, you can also create a new one. By logging in with the respective credentials, the user can now access the website interface.
 
 #### Login interface
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/login.png)
 
#### Create new user interface
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/register.png)



The website has a nav-bar that has three sections:
- #### Inventory
- #### Make order
- #### Reports

At the top right is the user's name and the option to log out.
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/index.png)

From the section **Inventory** you can see the information of the products and the quantity that exists. You can also modify and create a new product through the buttons in the view, "Modify" button and "Add New Product" respectively. These two buttons enable the options to be able to carry out the respective action.

![](https://github.com/scarlos723/finalproject/blob/master/images-readme/modifyProduct.png)![](https://github.com/scarlos723/finalproject/blob/master/images-readme/newProduct.png)
 
##### NOTE: **The tables have a search entry which allows filtering the information found in them. This is thanks to the following JavaScript function found in the function.js file (path * static / inventory *):**

```javascript
function search_item(){
   ....
}
```

The **Make Order** section allows you to take the different products that exist in the inventory and add them to the order list at the bottom. It also allows taking the customer's data (name, surname, identification and telephone number) which are associated with the order. If the user is new, a new entry is created in the database, if the user already exists, only the order is related to the existing user. From this section you can access three lists; purchase order list, quote order list, customer list, by means of the buttons; "Show Sales", "Show Quotes" and "Show Clients".

![](https://github.com/scarlos723/finalproject/blob/master/images-readme/makeOrder.png)

The **order list** has a field called "No. Order", from here you can access the detailed information of the order and later you can modify the description, the value and type of this.
 
#### Order list interface
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/orderList.png)

#### View order interface
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/orderView.png)    

The **client list** has a field called "Identification", by clicking on this you can access detailed information about the client and related orders. Customer information can also be modified.

#### Customer list interface
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/clientList.png)

#### View client interface
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/clientView.png)

The "Modify" button enables the fields to enter the new information, it also shows the "Apply" button which applies the changes.

![](https://github.com/scarlos723/finalproject/blob/master/images-readme/modifyclient.png)


The **Reports** section shows a detailed report in two card-type blocks, the first card shows total sales, customers and quotes, the second card shows total products sold and total products in inventory.
 
 #### Reports interface

![](https://github.com/scarlos723/finalproject/blob/master/images-readme/reports.png)
 
All the **CSS** code (style.css file) of the web page was created in the *static / inventory* path of the application. No need to use Bootstrap or other related tools. In the same way, the **JavaScript** functions implemented (function.js file) allow to send requests and modify the document's DOM to hide or show the different elements that compose it.
 
The models created in the file "**models.py**" of the application "**Inventory**" were 4: 
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
The application has a responsive design for mobiles, which has been defined to load when the browser has a view with a maximum width of 512 pixels:
 
```css
/* Mobile Styles */
@media only screen and (max-width: 512px) {
 
  .....
 
   }
```
By changing the width of the page, you can see the change in the font size of the text and the size of the buttons. The most significant change is that of the tables that must be adjusted to be able to visualize the information well. Below you can see some of the interfaces mobile responsive.

#### Mobile responsive

###### Login
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/mobileLogin.png)
###### Client list
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/mobileClientList.png)
###### Make order 1
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/mobileMakeOrder.png)
###### Make order 2
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/mobileMakeOrder1.png)
###### Order list
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/mobileOrderList.png)
###### Reports
![](https://github.com/scarlos723/finalproject/blob/master/images-readme/mobilereports.png)