

const btn = document.querySelector(".btn");
const btn2 = document.querySelector(".btn-cadastro");

const back = document.querySelector(".back");
const content= document.querySelector(".content");
const content2= document.querySelector(".content2");

function trocar(id, texto){
 document.getElementById(id).innerHTML = texto
}


btn.addEventListener("click", (e) => {
    e.preventDefault();
  back.classList.add("ativo");
  content.classList.add("sumir"); 
  content2.classList.add("mostrar"); 

});

btn2.addEventListener("click", (e) => {
  e.preventDefault();

  back.classList.remove("ativo");
  content.classList.remove("sumir"); 
  content2.classList.remove("mostrar"); 
});
