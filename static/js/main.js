let menuIcon = document.getElementById('menu-icon')
let sideBar = document.getElementById('side-bar')
let performance = true

menuIcon.addEventListener('click', ()=>{
   if(performance == true){
    sideBar.style.left = '20px'
    sideBar.style.transition  = '0.5s'
    menuIcon.innerHTML = '<i class="fa-solid fa-close fa-2x"></i>'
    performance = false
   }else{
    sideBar.style.left = '-350px'
    menuIcon.innerHTML = '<i class="fa-solid fa-bars fa-2x"></i>'
    performance = true
   }
})

