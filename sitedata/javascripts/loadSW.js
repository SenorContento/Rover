if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker
    .register('/sw.js', {
      scope: '/' //Be warned, the location of the sw.js script will override this in certain cases (The error code was also cryptic until I added this line of code).
    }).then(function(registration) {
      console.log("Hooray Señor! SW Registered! Registration: " + registration);
    })
    .catch(function(error) {
      console.log("Oh No Señor! You received error " + error + "!");
    });
  });
}
