document.addEventListener('DOMContentLoaded', function () {


    document.querySelectorAll('#btn-add').forEach(button => {
        button.onclick = function () {
            //this.style.display = "none";
            add_to_cart(this.dataset.page);
        }
    });

});


function add_to_cart(id){
    var name = document.getElementById('item-name-' + id).innerHTML;
    var model = document.getElementById('item-model-' + id).innerHTML;
    var price = document.getElementById('item-price-' + id).innerHTML;
    
    console.log(name + model + price);  

    var trow = document.createElement('tr');
    var tbl1 = document.createElement('td');
    var tbl2 = document.createElement('td');
    var tbl3 = document.createElement('td');

    tbl3.setAttribute('id','value'+id);


    var cant = document.createElement('input')
    
    cant.setAttribute('style','width:50px; text-align:center;');
    cant.setAttribute('class','cant-item');
    cant.setAttribute('id',id);
    cant.setAttribute('type','number');
    cant.setAttribute('value','1'); 
    cant.setAttribute('onkeyup','calc_total()');
    cant.setAttribute('onclick','calc_total()');

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
