// Modern Dashboard Interactions
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS
    AOS.init({
        duration: 800,
        once: true,
        offset: 100
    });

    // Add hover effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
            this.style.boxShadow = '0 15px 30px rgba(0,0,0,0.1)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });

    // Smooth progress bar animations
    const progressBars = document.querySelectorAll('.progress-fill');
    progressBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        setTimeout(() => {
            bar.style.width = width;
        }, 300);
    });

    // Stat number counter animation
    const stats = document.querySelectorAll('.stat-number');
    stats.forEach(stat => {
        const finalValue = parseInt(stat.textContent);
        let currentValue = 0;
        const duration = 1500;
        const stepTime = 20;
        const steps = duration / stepTime;
        const increment = finalValue / steps;

        const counter = setInterval(() => {
            currentValue += increment;
            if (currentValue >= finalValue) {
                stat.textContent = finalValue;
                clearInterval(counter);
            } else {
                stat.textContent = Math.floor(currentValue);
            }
        }, stepTime);
    });

    // Avatar image loading optimization
    const avatars = document.querySelectorAll('.avatar-img');
    avatars.forEach(avatar => {
        avatar.addEventListener('load', function() {
            this.classList.add('loaded');
        });
        
        avatar.addEventListener('error', function() {
            this.classList.add('error');
            // Default avatar already set in HTML onerror
        });
    });

    // Notification badge animations
    const badges = document.querySelectorAll('.badge');
    badges.forEach(badge => {
        badge.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
        });

        badge.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Quick action button effects
    const actionButtons = document.querySelectorAll('.action-btn');
    actionButtons.forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'scale(1.2) translateY(-2px)';
            }
        });

        btn.addEventListener('mouseleave', function() {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = '';
            }
        });

        btn.addEventListener('click', function() {
            this.classList.add('pressed');
            setTimeout(() => {
                this.classList.remove('pressed');
            }, 200);
        });
    });

    // Subject progress hover effects
    const subjectItems = document.querySelectorAll('.subject-item');
    subjectItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            const progressBar = this.querySelector('.progress-fill');
            if (progressBar) {
                progressBar.style.filter = 'brightness(1.1)';
            }
        });

        item.addEventListener('mouseleave', function() {
            const progressBar = this.querySelector('.progress-fill');
            if (progressBar) {
                progressBar.style.filter = '';
            }
        });
    });

    // Timeline animations
    const timelineItems = document.querySelectorAll('.timeline-item');
    let delay = 0;
    timelineItems.forEach(item => {
        item.style.animationDelay = `${delay}ms`;
        item.classList.add('fade-in');
        delay += 200;
    });
});

// Scroll position memory
window.addEventListener('beforeunload', () => {
    localStorage.setItem('scrollPos', window.scrollY);
});

window.addEventListener('load', () => {
    const scrollPos = localStorage.getItem('scrollPos');
    if (scrollPos) {
        window.scrollTo(0, parseInt(scrollPos));
        localStorage.removeItem('scrollPos');
    }
});

// Performance optimizations
document.addEventListener('scroll', () => {
    requestAnimationFrame(() => {
        const scrolled = window.scrollY > 100;
        document.body.classList.toggle('scrolled', scrolled);
    });
}, { passive: true });