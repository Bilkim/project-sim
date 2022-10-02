let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx-search");
let homecontent = document.querySelector(".home_content")

btn.onclick = function(){
    sidebar.classList.toggle("active");
    homecontent.classList.toggle("active");
}


searchBtn.onclick = function(){
    sidebar.classList.toggle("active");
}