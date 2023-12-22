document.addEventListener("DOMContentLoaded", function() {
      const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target); // Optionnel: arrêtez d'observer l'élément après l'animation
          }
        });
      }, { threshold: 0.1 }); // Le seuil peut être ajusté selon les besoins

      // Ciblez chaque élément avec la classe 'fade-up' pour l'animation
      document.querySelectorAll('.fade-up').forEach((el) => observer.observe(el));
    });

document.addEventListener("DOMContentLoaded", function() {
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible"); // Assurez-vous que cette classe correspond à celle définie dans votre CSS
        observer.unobserve(entry.target); // Optionnel : arrêtez d'observer l'élément après l'animation
      }
    });
  }, { threshold: 0.1 }); // Le seuil peut être ajusté selon les besoins

  // Ciblez chaque élément avec la classe 'fade-left' pour l'animation
  document.querySelectorAll('.fade-left').forEach((el) => observer.observe(el));
});
