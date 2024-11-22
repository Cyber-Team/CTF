// Glitch effect on title
document.addEventListener("DOMContentLoaded", function () {
    const glitchElement = document.querySelector('.glitch');
    glitchElement.setAttribute("data-text", glitchElement.textContent);
});
