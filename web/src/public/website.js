function myFunction() {
  alert("Thank you for visiting");
}

document.addEventListener("DOMContentLoaded", (event) => {
    document.querySelector('#personal').addEventListener("submit", function(e){
      var firstName 
      var lastName 
      var Emailaddress 
      var comments 
      // Get user input
      firstName = document.getElementById("firstN").value;
      lastName = document.getElementById("lastN").value;
      Emailaddress = document.getElementById("email").value;
      comments = document.getElementById("comment").value;
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
