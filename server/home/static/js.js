var modal = document.getElementById('first-modal');

var diveka = document.getElementById('frame1');

var span = document.getElementsByClassName("close")[0];

diveka.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event){
    if (event.target == modal){
        modal.style.display = "none";
    }
}
