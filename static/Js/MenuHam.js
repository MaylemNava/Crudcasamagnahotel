const burger = document.querySelector("#burger-menu");
const ul = document.querySelector("nav ul");
const nav = document.querySelector("nav");



// Seleccionar enlaces de navegación
const navLink = document.querySelectorAll(".nav-link");

burger.addEventListener("click", () => {
    ul.classList.toggle("show");
  });


// Cerrar el menú de hambuguesa cuando se hace click en un enlace  

navLink.forEach((link) =>
  link.addEventListener("click", () => {
    ul.classList.remove("show");
  })
);
