
document.getElementById("addbutton").onclick = add_string;

function add_string() {
  var str = document.createElement("tr");

  var name = document.createElement("td");
  var val1 = eel.handler();
  name.innerHTML = val1;
  alert(val1)

  var autor = document.createElement("td");
  var val2 = document.getElementById("book_autor").value;
  autor.innerHTML = val2;

  var year = document.createElement("td");
  var val3 = document.getElementById("book_year").value;
  year.innerHTML = val3;

  var genre = document.createElement("td");
  var val4 = document.getElementById("book_genre").value;
  genre.innerHTML = val4;

  str.appendChild(name);
  str.appendChild(autor);
  str.appendChild(year);
  str.appendChild(genre);
  var new_str = document.getElementById("addtable");
  new_str.appendChild(str);

}