document.addEventListener("DOMContentLoaded", (event) => {
    document.querySelector('#personal').addEventListener("submit", function(e){
      var firstName = document.getElementById("firstN").value;
      var lastName = document.getElementById("lastN").value;
      var Emailaddress = document.getElementById("email").value;
      var comments = document.getElementById("comment").value;

      const d = {first:firstName,last:lastName,em:Emailaddress,com:comments};
      fetch('/add_user',
      {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(d),
      }).then(response => response.json())
      e.preventDefault;
    })
  });
