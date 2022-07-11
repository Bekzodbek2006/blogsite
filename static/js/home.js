let msg = document.getElementById('msg')

if (msg.innerHTML != ""){
    msg.style.transition = '1s all'
    msg.style.top = "100px"
    setTimeout(()=>{
        msg.style.display = "none"
    }, 4000)
}

