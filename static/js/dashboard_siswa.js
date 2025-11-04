// Modern Dashboard App Module
const dashboardApp = {
    init() {
        this.initializeAOS();
        this.setupAnimations();
        this.initializeProgressBars();
        this.initializeProgressCircles();
        this.setupAutoRefresh();
        this.setupInteractiveCards();
    },

    initializeAOS() {
        // Initialize AOS (Animate On Scroll)
        AOS.init({
            duration: 800,
            easing: 'ease-out-cubic',
            once: true
        });
    },

    setupInteractiveCards() {
        // Add hover effect to stat cards
        document.querySelectorAll('.stat-card').forEach(card => {
            card.addEventListener('mouseenter', this.handleCardHover);
            card.addEventListener('mouseleave', this.handleCardLeave);
        });
    },

    handleCardHover(e) {
        const card = e.currentTarget;
        const icon = card.querySelector('.stat-icon i');
        icon.style.transform = 'scale(1.2) rotate(5deg)';
    },

    handleCardLeave(e) {
        const card = e.currentTarget;
        const icon = card.querySelector('.stat-icon i');
        icon.style.transform = 'scale(1) rotate(0)';
    },

    initializeProgressCircles() {
        document.querySelectorAll('.progress-circle').forEach(circle => {
            const value = parseInt(circle.dataset.value) || 0;
            const circumference = 2 * Math.PI * 15.9155; // Radius from SVG
            const offset = circumference - (value / 100 * circumference);
            const path = circle.querySelector('path');
            
            path.style.strokeDasharray = `${circumference} ${circumference}`;
            path.style.strokeDashoffset = offset;
        });
    },

    setupAnimations() {
        // Add staggered animations for notifications
        document.querySelectorAll('.notification').forEach((el, index) => {
            el.style.animationDelay = `${index * 150}ms`;
        });
        
        // Add staggered animations for feature cards
        document.querySelectorAll('.feature-card').forEach((el, index) => {
            el.style.animationDelay = `${(index * 100) + 200}ms`;
        });

        // Add fade-in animations with delay
        document.querySelectorAll('.fade-in').forEach((el, index) => {
            el.style.animationDelay = `${index * 100}ms`;
        });

        // Add hover effects
        this.setupHoverEffects();
    },

    setupHoverEffects() {
        // Subject item hover effects
        document.querySelectorAll('.subject-item').forEach(item => {
            item.addEventListener('mouseenter', () => item.classList.add('hover'));
            item.addEventListener('mouseleave', () => item.classList.remove('hover'));
        });

        // Action button press effect
        document.querySelectorAll('.action-btn').forEach(btn => {
            btn.addEventListener('mousedown', () => btn.classList.add('pressed'));
            btn.addEventListener('mouseup', () => btn.classList.remove('pressed'));
            btn.addEventListener('mouseleave', () => btn.classList.remove('pressed'));
        });
    },

    initializeProgressBars() {
        document.querySelectorAll('.progress-fill').forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0';
            requestAnimationFrame(() => {
                bar.style.width = width;
            });
        });
    },

    setupAutoRefresh() {
        // Auto refresh data every 5 minutes
        setInterval(() => {
            const now = new Date().getMinutes();
            if (now % 5 === 0) this.refreshData();
        }, 60000);
    },

    async refreshData() {
        const refreshBtn = document.querySelector('.dashboard-actions .btn i');
        refreshBtn.classList.add('animate-spin');

        try {
            const response = await fetch('/siswa/api/refresh-data');
            const data = await response.json();
            
            if (data.success) {
                this.updateDashboardData(data);
                this.showNotification('Data berhasil diperbarui!', 'success');
            } else {
                throw new Error(data.message || 'Gagal memperbarui data');
            }
        } catch (error) {
            this.showNotification(error.message, 'error');
        } finally {
            refreshBtn.classList.remove('animate-spin');
        }
    },

    updateDashboardData(data) {
        // Update stats
        if (data.stats) {
            Object.entries(data.stats).forEach(([key, value]) => {
                const el = document.querySelector(`.${key}-stat .stat-number`);
                if (el) this.animateNumber(el, value);
            });
        }

        // Update other sections if needed
        if (data.activities) this.updateActivities(data.activities);
        if (data.notifications) this.updateNotifications(data.notifications);
    },

    animateNumber(element, targetValue, duration = 1000) {
        const start = parseInt(element.textContent) || 0;
        const range = targetValue - start;
        const increment = range / (duration / 16); // 60fps
        let current = start;
        
        const animate = () => {
            current += increment;
            
            if ((increment > 0 && current >= targetValue) || 
                (increment < 0 && current <= targetValue)) {
                element.textContent = targetValue;
                return;
            }
            
            element.textContent = Math.round(current);
            requestAnimationFrame(animate);
        };
        
        requestAnimationFrame(animate);
    },

    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification ${type} slide-in`;
        notification.innerHTML = `
            <i class="fas ${this.getNotificationIcon(type)}"></i>
            <span>${message}</span>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.classList.add('fade-out');
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    },

    getNotificationIcon(type) {
        const icons = {
            success: 'fa-check-circle',
            error: 'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        };
        return icons[type] || icons.info;
    },

    // Action handlers
    async startLearning() {
        this.showNotification('Memulai sesi pembelajaran...', 'info');
        await this.delay(500);
        window.location.href = '/learning/start';
    },

    async viewAssignments() {
        this.showNotification('Membuka daftar tugas...', 'info');
        await this.delay(500);
        window.location.href = '/assignments';
    },

    async takeQuiz() {
        this.showNotification('Mempersiapkan kuis...', 'info');
        await this.delay(500);
        window.location.href = '/quiz/daily';
    },

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
};

// Initialize dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', () => dashboardApp.init());