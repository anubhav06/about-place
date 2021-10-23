document.addEventListener('DOMContentLoaded', function(){

    console.log('Loaded!')

    

    //var countries = document.querySelectorAll('.countryName');
    //if( countries.length > 1 ){   
    //    for(var i=0 ; i<countries.length; i++){

    //        var name = countries[i].innerHTML
    //        callFetch(name,countries,i)
    //    }
    //}
    //else{
    //    console.log('No countries! ')
    //}

})


function callFetch(name, countries, i){
    console.log('Fetch ran')
    fetch('https://restcountries.com/v3.1/name/' + name)
    .then(response => response.json())
    .then(response => {
        var url = response[0].flags.png
        countries[i].innerHTML = "<img src='" + url + "' alt='" + name + "'s flag' height='250' width='auto'>"
    })
}

function loaded(){
    console.log('Template Loaded')
    var countries = document.querySelectorAll('.countryName');
    if( countries.length > 0 ){   
        for(var i=0 ; i<countries.length; i++){

            var name = countries[i].innerHTML
            callFetch(name,countries,i)
        }
    }
    else{
        console.log('No countries! ')
    }
}