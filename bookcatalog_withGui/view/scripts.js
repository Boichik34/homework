//
//document.getElementById("addbutton").onclick = add_string;
//
//async function add_string() {
//  var str = document.createElement("tr");
//
//  let name = document.createElement("td");
//  let ret_elem = document.getElementById('book_name').value;
//  let val1 = await eel.handler(ret_elem)();
//  name.innerHTML = val1;
//  alert(val1)
//
//  let autor = document.createElement("td");
//  let val2 = document.getElementById("book_autor").value;
//  autor.innerHTML = val2;
//
//  let year = document.createElement("td");
//  let val3 = document.getElementById("book_year").value;
//  year.innerHTML = val3;
//
//  let genre = document.createElement("td");
//  let val4 = document.getElementById("book_genre").value;
//  genre.innerHTML = val4;
//
//  str.appendChild(name);
//  str.appendChild(autor);
//  str.appendChild(year);
//  str.appendChild(genre);
//  let new_str = document.getElementById("addtable");
//  new_str.appendChild(str);
//
//


// document.getElementById('addbutton') = add_new_element;

async function add_new_element() {
    let name = document.getElementById('book_name').value;
    let autor = document.getElementById('book_autor').value;
    let genre = document.getElementById('book_genre').value;
    let year = document.getElementById('book_year').value;
    let status = document.getElementById('book_status').value;

    let id = await eel.handler(name, autor, genre, year)();
    addNewElementInTable(name, autor, genre, year, status, id)
}

async function makeApp() {
    let dictionary = await eel.get_list()();
    if (dictionary) {
        for (let key in dictionary) {
            let new_line = document.createElement('tr');

            let name = document.createElement('td');
            let autor = document.createElement('td');
            let genre = document.createElement('td');
            let year = document.createElement('td');
            let status = document.createElement('td');

            name.innerHTML = dictionary[key]['name'];
            autor.innerHTML = dictionary[key]['autor'];
            genre.innerHTML = dictionary[key]['genre'];
            year.innerHTML = dictionary[key]['year'];
            status.innerHTML = dictionary[key]['is_done'];

            new_line.appendChild(name);
            new_line.appendChild(autor);
            new_line.appendChild(year);
            new_line.appendChild(genre);
            new_line.appendChild(status);
            new_line.setAttribute('id', key)

            let new_str = document.getElementById("addtable");
            new_str.appendChild(new_line);
        }
    }

    for (let key in dictionary) {
        let btn = document.getElementById(key);
        btn.onclick = function (){
            alert(key)
        }
    }
}


function addNewElementInTable(new_name, new_autor, new_genre, new_year, new_status, id) {
    let new_line = document.createElement('tr');
    new_line.setAttribute('id', id);
    let name = document.createElement('td');
    let autor = document.createElement('td');
    let genre = document.createElement('td');
    let year = document.createElement('td');
    let status = document.createElement('td');

    name.innerHTML = new_name;
    autor.innerHTML = new_autor;
    genre.innerHTML = new_genre;
    year.innerHTML = new_year;
    status.innerHTML = new_status;

    new_line.appendChild(name);
    new_line.appendChild(autor);
    new_line.appendChild(year);
    new_line.appendChild(genre);
    new_line.appendChild(status);

    let new_str = document.getElementById("addtable");
    new_str.appendChild(new_line);

    document.getElementById(id).onclick = alertBingo;
}

makeApp();


function alertBingo(r) {
    alert(r)
}



