// JavaScript to enhance the buttons in the Projects section

// Selecting the buttons
const projectButtons = document.querySelectorAll('#projects a');

// Adding click event listeners to each button
projectButtons.forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        
        // Change background color of main content area
        const mainContent = document.querySelector('main');
        mainContent.style.backgroundColor = getRandomColor();
    });
});

// Function to generate a random color
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
