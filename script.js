document.addEventListener('DOMContentLoaded', () => {

    // --- Mobile Menu Toggle ---
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
    }

    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            if (hamburger.classList.contains('active')) {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
            }
        });
    });

    // --- Navbar Scroll Effect ---
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // --- Scroll Reveal Animations ---
    const revealElements = document.querySelectorAll('.card, .feature-text, .feature-image, .team-card, .resources-content, .download-card');
    
    // Add initial reveal class
    revealElements.forEach(el => {
        el.classList.add('reveal');
    });

    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Trigger only once
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });
});

// --- Interactive Gameplay Gallery Switcher ---
window.switchGallery = function(imageSrc, captionText) {
    const mainImg = document.getElementById('gallery-main-img');
    const captionEl = document.getElementById('gallery-caption-text');
    
    if (mainImg && captionEl) {
        // Fade out
        mainImg.style.opacity = '0';
        
        setTimeout(() => {
            mainImg.src = imageSrc;
            captionEl.textContent = captionText;
            // Fade in
            mainImg.style.opacity = '1';
        }, 200);
    }
    
    // Update active thumb styling
    const thumbs = document.querySelectorAll('.gallery-thumbs .thumb');
    thumbs.forEach(thumb => {
        // Normalize URLs to accurately compare them
        const thumbSrcNormalized = thumb.getAttribute('src').replace(/\\/g, '/');
        const targetSrcNormalized = imageSrc.replace(/\\/g, '/');
        
        if (thumbSrcNormalized === targetSrcNormalized) {
            thumb.classList.add('active');
        } else {
            thumb.classList.remove('active');
        }
    });
};
