// Initialize progress bars
function initializeProgressBars() {
    const progressBars = document.querySelectorAll('.progress-fill');
    progressBars.forEach(bar => {
        const progress = bar.getAttribute('data-progress');
        bar.style.width = progress + '%';
    });
}

// Handle avatar image fallback
function handleAvatarImages() {
    const avatars = document.querySelectorAll('.avatar-img');
    avatars.forEach(avatar => {
        if (!avatar.complete || avatar.naturalHeight === 0) {
            const defaultSrc = avatar.getAttribute('data-default-src');
            if (defaultSrc) {
                avatar.src = defaultSrc;
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Initialize progress bars
    initializeProgressBars();
    
    // Handle avatar images
    handleAvatarImages();
    
    // Smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});