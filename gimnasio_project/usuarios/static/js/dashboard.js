document.addEventListener('DOMContentLoaded', function() {
    // Navegación entre secciones
    const navLinks = document.querySelectorAll('.sidebar-nav a');
    const sections = document.querySelectorAll('.content-section');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                
                // Ocultar todas las secciones
                sections.forEach(section => {
                    section.style.display = 'none';
                });
                
                // Mostrar la sección seleccionada
                const targetId = this.getAttribute('href');
                document.querySelector(targetId).style.display = 'block';
                
                // Actualizar el estado activo en el menú
                navLinks.forEach(navLink => {
                    navLink.parentElement.classList.remove('active');
                });
                this.parentElement.classList.add('active');
            }
        });
    });
    
    // Cerrar mensajes
    const closeButtons = document.querySelectorAll('.close-message');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.parentElement.style.display = 'none';
        });
    });
    
    // Mostrar la sección de inicio por defecto
    document.querySelector('#inicio').style.display = 'block';
});