document.addEventListener('DOMContentLoaded', function(){

    console.log('Loaded!')

    var countries = document.querySelectorAll('.countryName');
    for(var i=0 ; i<countries.length; i++){

        var name = countries[i].innerHTML
        callFetch(name,countries,i)
    }

})


function callFetch(name, countries, i){
    
    fetch('https://www.googleapis.com/customsearch/v1?key=AIzaSyA-iusVy-dJ3y56kSEA3GNE-uZRL0lmbyA&cx=9a0610b867724db27&q=' + name)
    .then(response => response.json())
    .then(response => {
        var url = response.items[0].pagemap.cse_image[0].src
        countries[i].innerHTML = "<img src='" + url + "' alt='" + name + "'s flag' height='250' width='auto'>"
    })
}
