document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let gender = document.getElementById("gender").value;
    let country = document.getElementById("country").value;
    let programming = [];

    if (document.getElementById("cpp").checked) {
        programming.push("C++");
    }
    if (document.getElementById("python").checked) {
        programming.push("Python");
    }

    if (!name || !email || !gender || !country || programming.length === 0) {
        document.getElementById("message").innerHTML = "All fields are required!";
        return;
    }

    fetch("/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, gender, country, programming })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerHTML = data.message;
    })
    .catch(error => console.error("Error:", error));
});
