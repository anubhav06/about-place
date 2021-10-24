//document.addEventListener('DOMContentLoaded', function(){

//    console.log('Loaded!')

//})

function callFetch(name, countries, i) {
  fetch("https://restcountries.com/v3.1/name/" + name)
    .then((response) => response.json())
    .then((response) => {
      console.log(response);
      var url = response[0].flags.png;
      countries[i].innerHTML =
        "<img src='" +
        url +
        "' alt='" +
        name +
        "'s flag' height='213' width='320'>";
    });
}

function loaded() {
  console.log("Template Loaded");
  var countries = document.querySelectorAll(".countryName");
  if (countries.length > 0) {
    for (var i = 0; i < countries.length; i++) {
      var name = countries[i].innerHTML;
      callFetch(name, countries, i);
    }
  } else {
    console.log("No countries! ");
  }
}

function countryPageFetch(
  name,
  coatOfArms,
  continents,
  currenciesName,
  currenciesSymbol,
  flags,
  languages,
  population
) {
  fetch("https://restcountries.com/v3.1/name/" + name)
    .then((response) => response.json())
    .then((response) => {
      console.log(response);
      // R at end means response variable
    //  var coatOfArmsR = response[0].coatOfArms.png;
    //  var continentsR = response[0].continents[0];
    //  var currenciesNameR =
    //    response[0].currencies[Object.keys(response[0].currencies)[0]].name;
    //  var currenciesSymbolR =
    //    response[0].currencies[Object.keys(response[0].currencies)[0]].symbol;
    //  var flagsR = response[0].flags.png;
    //  var languagesR = response[0].languages;
    //  var populationR = response[0].population;

      //Change the elements inner HTML to the fetched value
      coatOfArms.innerHTML =
        "<img src='" + coatOfArmsR + "' height='100' width='auto'>";
    //  continents.innerHTML = `${continentsR}`;
    //  currenciesName.innerHTML = `${currenciesNameR}`;
    //  currenciesSymbol.innerHTML = `${currenciesSymbolR}`;
    //  flags.innerHTML = "<img src='" + flagsR + "' height='100' width='auto'>";
    //  population.innerHTML = `${populationR}`;
    });
}

function countryPageLoad() {
  console.log("Country Page LOADED!");

  // Get the country name
  var name = document.querySelector(".country").value;
  console.log(name);

  var coatOfArms = document.body.querySelector(".coatOfArms");
  var continents = document.body.querySelector(".continents");
  var currenciesName = document.body.querySelector(".currencies-name");
  var currenciesSymbol = document.body.querySelector(".currencies-symbol");
  var flags = document.body.querySelector(".flags");
  var languages = document.body.querySelector(".languages");
  var population = document.body.querySelector(".population");

  countryPageFetch(
    name,
    coatOfArms,
    continents,
    currenciesName,
    currenciesSymbol,
    flags,
    languages,
    population
  );
}
