document.getElementById("login-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    console.log("Login submitted with email: " + email);
});

document.getElementById("signup-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const newEmail = document.getElementById("new-email").value;
    const newPassword = document.getElementById("new-password").value;
    console.log("Signup submitted with email: " + newEmail);
});
