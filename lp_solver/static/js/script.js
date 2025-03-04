// lp_solver/static/js/script.js
document.addEventListener("DOMContentLoaded", function() {
    const toggleSwitch = document.getElementById("dark-mode-toggle");
    const form = document.querySelector("form");
    const inputs = document.querySelectorAll("input");
    const loadingScreen = document.querySelector(".loading");

    // 🌙 Dark Mode Toggle
    toggleSwitch.addEventListener("change", () => {
        document.body.classList.toggle("light-mode");
    });

    // 🚀 Live Input Validation
    inputs.forEach(input => {
        input.addEventListener("input", function() {
            if (isNaN(this.value) || this.value === "") {
                this.style.border = "2px solid red";
            } else {
                this.style.border = "2px solid green";
            }
        });
    });

    // ⏳ Loading Animation on Form Submission
    if (form) {
        form.addEventListener("submit", function(event) {
            event.preventDefault();
            loadingScreen.style.display = "block";
            setTimeout(() => form.submit(), 2000);  // Simulating delay
        });
    }
});
