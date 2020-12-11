document.addEventListener('DOMContentLoaded', function () {


    document.querySelectorAll('#btn-add').forEach(button => {
        button.onclick = function () {
            //this.style.display = "none";
            add_to_cart(this.dataset.page);
        }
    });

});

function show_form(){
    document.querySelector(".form-created-product").style.display="block";
}

function update_product(id){
    let data = new FormData();
    let token = document.getElementsByName("csrfmiddlewaretoken");
    //token is type Nodelist

    data.append('csrfmiddlewaretoken', token[0].value );
    data.append('name',document.getElementById('inp-name-'+id).value);
    data.append('model',document.getElementById('inp-model-'+id).value);
    data.append('price',document.getElementById('inp-price-'+id).value);
    data.append('stock',document.getElementById('inp-stock-'+id).value);

    fetch('product/'+id,{
        method:'POST',
        body:data,
        
        
    })
    .then(response => response) //se quita la funcion .json() para que no arroje error
    .then(result => {
         // Print result
         console.log(result); //imprime un objetohtml con el resultado
         console.log("Aqui debe ir el set")
         setTimeout( console.log("Loading..."), 1000); //retardo para que recargue la pagina
         window.location.href="/inventory";  
         //load_mailbox('inbox');
       });

    


}


function modify_product(id){

    document.querySelectorAll('.inp-product-'+id).forEach(item=>{
        item.style.display='block';
    });
    document.querySelectorAll('.row-product-'+id).forEach(item=>{
        item.style.display='none';
    });
    document.querySelector('.button_blue').style.display='none';
    document.querySelector('.button_green').style.display='block';
}


function modify_view(id){
    document.querySelectorAll('#inp-client-'+id).forEach(item=>{
        item.style.display ="block";
    });
    
    document.querySelectorAll('#item-client-'+id).forEach(item=>{
        item.style.display ="none";
    });

    document.querySelector('.button_red').style.display ="none";
    document.querySelector('.button_blue').style.display ="none";
    document.querySelector('.button_green').style.display ="block";
    
    
}

function modify_client(id){

    //crear peticion
    var data = new FormData();
    
    var inps =  document.querySelectorAll('#inp-client-'+id);  //inps is type Nodelist
    var token=  document.getElementsByName("csrfmiddlewaretoken"); //token is type Nodelist

    data.append('csrfmiddlewaretoken',token[0].value);
    data.append('identification', inps[0].value);
    data.append('name', inps[1].value);
    data.append('lastname', inps[2].value);
    data.append('telephone', inps[3].value);


        fetch('client/'+id,{
            method:'POST',
            body:data,
            
            
        })
        .then(response => response.json())
        .then(result => {
             // Print result
             console.log(result);
             //load_mailbox('inbox');
             
           });

    setTimeout( console.log("Loading..."), 1000); //retardo para que recargue la pagina
    window.location.href="client-list";        
    
}

function create_order(order){

    let order_form = document.getElementById('order-form').elements; //retorna una lista de los nputs

    
    let description="";
    let items = document.getElementById('tbody_cart').rows;
    
    for (var i=0; i< items.length; i++ ){
        description = description + items[i].innerText + "Amount: " + items[i].lastElementChild.value + "\n"   ;
    }
        
    
    console.log(description);


    let data = new FormData();

    data.append('csrfmiddlewaretoken',order_form.csrfmiddlewaretoken.value);
    data.append('name',order_form.name.value);
    data.append('lastname',order_form.lastname.value);
    data.append('identification', order_form.identification.value);
    data.append('telephone', order_form.telephone.value);
    data.append('user_id', order_form.user_id.value);
    data.append('total', document.getElementById("total-cart").innerText);
    data.append('description', description);

    //obtener tuplas de cantidades
    let inps = document.querySelectorAll('.cant-item');
    let cant_list ="[";
    for(let i=0; i < inps.length; i++){
        cant_list = cant_list + "(" + inps[i].getAttribute('id') + "," + inps[i].value + "),";
    }
    cant_list=cant_list+"]";

    data.append('cant_list', cant_list);

    console.log("Creando orden...");
    //console.log(order_form);
    //console.log(data);
    console.log(order)
  
   
    
    if(order =="quote"){
        
        data.append('type_order', "Quote");

        fetch('create-order',{
            method:'POST',
            body:data,
            
            
        })
        .then(response => response.json())
        .then(result => {
             // Print result
             console.log(result);
             //load_mailbox('inbox');
           });
        window.alert("The quote order has been created");
    }

    if (order=="sale"){
        data.append('type_order', "Sale");
        
        fetch('create-order',{
            method:'POST',
            body:data,
            
            
        })
        .then(response => response.json())
        .then(result => {
             // Print result
             console.log(result);
             //load_mailbox('inbox');
           });
        window.alert("The purchase order has been created");
    }
    
}


function add_to_cart(id){
    var name = document.getElementById('item-name-' + id).innerHTML;
    var model = document.getElementById('item-model-' + id).innerHTML;
    var price = document.getElementById('item-price-' + id).innerHTML;
    
    console.log(name + model + price);  

    var trow = document.createElement('tr');
    var tbl1 = document.createElement('td');
    var tbl2 = document.createElement('td');
    var tbl3 = document.createElement('td');
    
    trow.setAttribute('id','item-row'+id);
    tbl1.setAttribute('id','name-product'+id);
    tbl2.setAttribute('id','model-product'+id);
    tbl3.setAttribute('id','value'+id);


    var cant = document.createElement('input')
    
    cant.setAttribute('style','width:50px; text-align:center;');
    cant.setAttribute('class','cant-item');
    cant.setAttribute('id',id);
    cant.setAttribute('type','number');
    cant.setAttribute('value','1'); 
    cant.setAttribute('onkeyup','calc_total()');
    cant.setAttribute('onclick','calc_total()');
    cant.setAttribute('min','0');
    cant.setAttribute('max', document.getElementById('item-stock-'+id).innerText);

    tbl1.innerHTML = name;
    tbl2.innerHTML = model;
    tbl3.innerHTML = price;

    trow.appendChild(tbl1);
    trow.appendChild(tbl2);
    trow.appendChild(tbl3);
    trow.appendChild(cant);

    console.log(trow);

    var tbody = document.getElementById("tbody_cart");
    tbody.appendChild(trow);

    calc_total();
}

function calc_total(){ 
    let sum=0;
    document.querySelectorAll('.cant-item').forEach(item =>{
            id_aux= item.getAttribute('id');
            sum=sum+ ( parseInt(item.value)* parseInt((document.getElementById("value"+id_aux).innerText).substring(1)));
            
    });

    document.getElementById('total-cart').innerHTML = sum;
}

function search_item(){

    const tableReg = document.getElementById('date-table');

    const searchText = document.getElementById('searchTerm').value.toLowerCase();

    let total = 0;



    // Recorremos todas las filas con contenido de la tabla

    for (let i = 1; i < tableReg.rows.length; i++) {

        // Si el td tiene la clase "noSearch" no se busca en su cntenido

        if (tableReg.rows[i].classList.contains("noSearch")) {

            continue;

        }



        let found = false;

        const cellsOfRow = tableReg.rows[i].getElementsByTagName('td');

        // Recorremos todas las celdas

        for (let j = 0; j < cellsOfRow.length && !found; j++) {

            const compareWith = cellsOfRow[j].innerHTML.toLowerCase();

            // Buscamos el texto en el contenido de la celda

            if (searchText.length == 0 || compareWith.indexOf(searchText) > -1) {

                found = true;

                total++;

            }

        }

        if (found) {

            tableReg.rows[i].style.display = '';

        } else {

            // si no ha encontrado ninguna coincidencia, esconde la

            // fila de la tabla

            tableReg.rows[i].style.display = 'none';

        }

    }



    // mostramos las coincidencias

    const lastTR=tableReg.rows[tableReg.rows.length-1];

    const td=lastTR.querySelector("td");

    lastTR.classList.remove("hide", "red");

    if (searchText == "") {

        lastTR.classList.add("hide");

    } else if (total) {

        //td.innerHTML="Se ha encontrado "+total+" coincidencia"+((total>1)?"s":"");

    } else {

        lastTR.classList.add("red");

        //td.innerHTML="No se han encontrado coincidencias";

    }

}

