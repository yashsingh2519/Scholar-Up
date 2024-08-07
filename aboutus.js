document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for navigation links
    const navLinks = document.querySelectorAll('header nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Adding some dynamic interactivity
    const aboutUsSection = document.querySelector('.about-us');
    aboutUsSection.addEventListener('mouseover', function() {
        this.style.boxShadow = '0 0 15px rgba(0, 0, 0, 0.3)';
    });
    aboutUsSection.addEventListener('mouseout', function() {
        this.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.1)';
    });

    // Dark mode toggle
    const toggleDarkMode = document.createElement('button');
    toggleDarkMode.textContent = 'Toggle Dark Mode';
    toggleDarkMode.style.position = 'fixed';
    toggleDarkMode.style.bottom = '10px';
    toggleDarkMode.style.right = '10px';
    toggleDarkMode.style.padding = '10px';
    toggleDarkMode.style.backgroundColor = '#35424a';
    toggleDarkMode.style.color = '#ffffff';
    toggleDarkMode.style.border = 'none';
    toggleDarkMode.style.cursor = 'pointer';
    document.body.appendChild(toggleDarkMode);

    toggleDarkMode.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
    });
});

// CSS for dark mode
const style = document.createElement('style');
style.innerHTML = `
    .dark-mode {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .dark-mode header {
        background-color: #1a1a1a;
    }
    .dark-mode footer {
        background-color: #1a1a1a;
    }
    .dark-mode .about-us {
        background-color: #2c2c2c;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
    }
    .dark-mode header nav ul li a {
        color: #ffffff;
    }
    .dark-mode header nav ul li a.active {
        border-bottom: 2px solid #e8491d;
    }
`;
document.head.appendChild(style);
