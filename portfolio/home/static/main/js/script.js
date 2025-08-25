// simple smooth scrolling
document.querySelectorAll('a.nav-link').forEach(anchor =>{
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = anchor.getAttribute('href');
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
