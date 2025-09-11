// LENTERAMU Dynamic Dashboard JavaScript
class LenteramuDashboard {
    constructor() {
        this.refreshInterval = 30000; // 30 seconds
        this.notificationInterval = 60000; // 1 minute
        this.userRole = this.getUserRole();
        this.init();
    }

    init() {
        this.startAutoRefresh();
        this.setupEventListeners();
        this.initializeAnimations();
        this.setupNotifications();
    }

    getUserRole() {
        // Get user role from session or DOM
        const roleElement = document.querySelector('[data-user-role]');
        return roleElement ? roleElement.dataset.userRole : 'student';
    }

    // Auto-refresh functionality
    startAutoRefresh() {
        setInterval(() => {
            this.refreshDashboardData();
        }, this.refreshInterval);

        setInterval(() => {
            this.refreshNotifications();
        }, this.notificationInterval);
    }

    async refreshDashboardData() {
        try {
            const response = await fetch(`/api/dashboard/refresh/${this.userRole}`);
            const data = await response.json();
            
            if (data.status === 'success') {
                this.updateDashboardStats(data.data);
                this.showRefreshIndicator();
            }
        } catch (error) {
            console.error('Error refreshing dashboard:', error);
        }
    }

    async refreshNotifications() {
        try {
            const response = await fetch(`/api/notifications/${this.userRole}`);
            const data = await response.json();
            
            if (data.status === 'success') {
                this.updateNotifications(data.notifications);
                this.updateNotificationCount(data.count);
            }
        } catch (error) {
            console.error('Error refreshing notifications:', error);
        }
    }

    updateDashboardStats(data) {
        // Update stats based on role
        if (this.userRole === 'student') {
            this.updateStudentStats(data);
        } else if (this.userRole === 'teacher') {
            this.updateTeacherStats(data);
        } else if (this.userRole === 'admin') {
            this.updateAdminStats(data);
        }
    }

    updateStudentStats(data) {
        // Update progress
        const progressElement = document.querySelector('.progress-stat .stat-number');
        if (progressElement) {
            this.animateNumber(progressElement, data.progress, '%');
        }

        // Update completed courses
        const completedElement = document.querySelector('.completed-stat .stat-number');
        if (completedElement) {
            this.animateNumber(completedElement, data.completed_courses);
        }

        // Update pending tasks
        const pendingElement = document.querySelector('.pending-stat .stat-number');
        if (pendingElement) {
            this.animateNumber(pendingElement, data.pending_tasks);
        }

        // Update learning streak
        const streakElement = document.querySelector('.streak-stat .stat-number');
        if (streakElement) {
            this.animateNumber(streakElement, data.learning_streak);
        }

        // Update subject progress
        this.updateSubjectProgress(data.subjects);
    }

    updateTeacherStats(data) {
        // Update total students
        const studentsElement = document.querySelector('.students-stat .stat-number');
        if (studentsElement) {
            this.animateNumber(studentsElement, data.total_students);
        }

        // Update pending grading
        const gradingElement = document.querySelector('.grading-stat .stat-number');
        if (gradingElement) {
            this.animateNumber(gradingElement, data.pending_grading);
        }

        // Update class performance
        const performanceElement = document.querySelector('.performance-stat .stat-number');
        if (performanceElement) {
            this.animateNumber(performanceElement, data.average_class_performance, '%');
        }
    }

    updateAdminStats(data) {
        // Update total users
        const usersElement = document.querySelector('.users-stat .stat-number');
        if (usersElement) {
            this.animateNumber(usersElement, data.total_users);
        }

        // Update active users
        const activeElement = document.querySelector('.active-stat .stat-number');
        if (activeElement) {
            this.animateNumber(activeElement, data.daily_active_users);
        }

        // Update system metrics if available
        if (data.system_metrics) {
            this.updateSystemMetrics(data.system_metrics);
        }
    }

    updateSubjectProgress(subjects) {
        subjects.forEach(subject => {
            const subjectElement = document.querySelector(`[data-subject="${subject.name}"]`);
            if (subjectElement) {
                const progressBar = subjectElement.querySelector('.progress-fill');
                const progressText = subjectElement.querySelector('.progress-text');
                
                if (progressBar) {
                    progressBar.style.width = subject.progress + '%';
                }
                if (progressText) {
                    progressText.textContent = subject.progress + '%';
                }
            }
        });
    }

    updateSystemMetrics(metrics) {
        // Update CPU usage
        const cpuBar = document.querySelector('.metric-fill.cpu');
        const cpuValue = document.querySelector('.cpu-usage .metric-value');
        if (cpuBar && cpuValue) {
            cpuBar.style.width = metrics.cpu_usage + '%';
            cpuValue.textContent = metrics.cpu_usage + '%';
        }

        // Update Memory usage
        const memoryBar = document.querySelector('.metric-fill.memory');
        const memoryValue = document.querySelector('.memory-usage .metric-value');
        if (memoryBar && memoryValue) {
            memoryBar.style.width = metrics.memory_usage + '%';
            memoryValue.textContent = metrics.memory_usage + '%';
        }

        // Update Disk usage
        const diskBar = document.querySelector('.metric-fill.disk');
        const diskValue = document.querySelector('.disk-usage .metric-value');
        if (diskBar && diskValue) {
            diskBar.style.width = metrics.disk_usage + '%';
            diskValue.textContent = metrics.disk_usage + '%';
        }
    }

    updateNotifications(notifications) {
        const notificationsList = document.querySelector('.notifications-list');
        if (!notificationsList) return;

        // Clear existing notifications
        notificationsList.innerHTML = '';

        // Add new notifications
        notifications.forEach(notification => {
            const notificationElement = this.createNotificationElement(notification);
            notificationsList.appendChild(notificationElement);
        });
    }

    createNotificationElement(notification) {
        const div = document.createElement('div');
        div.className = `notification-item ${notification.type}`;
        
        const iconMap = {
            'assignment': 'fa-file-alt',
            'grade': 'fa-star',
            'announcement': 'fa-bullhorn',
            'meeting': 'fa-users',
            'system': 'fa-cog',
            'alert': 'fa-exclamation-circle'
        };

        div.innerHTML = `
            <div class="notification-icon">
                <i class="fas ${iconMap[notification.type] || 'fa-info-circle'}"></i>
            </div>
            <div class="notification-content">
                <p>${notification.message}</p>
                <span class="notification-time">${notification.time}</span>
            </div>
        `;

        return div;
    }

    updateNotificationCount(count) {
        const countElements = document.querySelectorAll('.notification-count');
        countElements.forEach(element => {
            element.textContent = count;
            if (count > 0) {
                element.classList.add('has-notifications');
            } else {
                element.classList.remove('has-notifications');
            }
        });
    }

    animateNumber(element, newValue, suffix = '') {
        const currentValue = parseInt(element.textContent) || 0;
        const increment = (newValue - currentValue) / 20;
        let current = currentValue;

        const animation = setInterval(() => {
            current += increment;
            if ((increment > 0 && current >= newValue) || (increment < 0 && current <= newValue)) {
                current = newValue;
                clearInterval(animation);
            }
            element.textContent = Math.round(current) + suffix;
        }, 50);
    }

    showRefreshIndicator() {
        // Show a subtle refresh indicator
        const indicator = document.createElement('div');
        indicator.className = 'refresh-indicator';
        indicator.innerHTML = '<i class="fas fa-sync-alt"></i> Data diperbarui';
        indicator.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(39, 174, 96, 0.9);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.8rem;
            z-index: 10000;
            opacity: 0;
            transition: opacity 0.3s ease;
        `;

        document.body.appendChild(indicator);

        // Animate in
        setTimeout(() => {
            indicator.style.opacity = '1';
        }, 100);

        // Remove after 3 seconds
        setTimeout(() => {
            indicator.style.opacity = '0';
            setTimeout(() => {
                if (indicator.parentNode) {
                    indicator.parentNode.removeChild(indicator);
                }
            }, 300);
        }, 3000);
    }

    setupEventListeners() {
        // Search functionality
        const searchInput = document.querySelector('.dashboard-search');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                this.performSearch(e.target.value);
            });
        }

        // Filter buttons
        const filterButtons = document.querySelectorAll('.filter-btn');
        filterButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                this.applyFilter(e.target.dataset.filter);
            });
        });

        // Quick action buttons
        document.addEventListener('click', (e) => {
            if (e.target.matches('.quick-action-btn')) {
                this.handleQuickAction(e.target.dataset.action);
            }
        });
    }

    performSearch(query) {
        // Implement search functionality
        console.log('Searching for:', query);
        // This would filter dashboard content based on the query
    }

    applyFilter(filterType) {
        // Implement filtering functionality
        console.log('Applying filter:', filterType);
        // This would filter dashboard content based on the filter type
    }

    handleQuickAction(action) {
        // Handle quick actions
        switch (action) {
            case 'new-assignment':
                window.location.href = '/assignments/create';
                break;
            case 'view-grades':
                window.location.href = '/grades';
                break;
            case 'start-quiz':
                window.location.href = '/quiz/start';
                break;
            default:
                console.log('Unknown action:', action);
        }
    }

    initializeAnimations() {
        // Intersection Observer for animations
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        });

        // Observe all stat cards
        const statCards = document.querySelectorAll('.stat-card, .dashboard-card, .admin-card, .teacher-card');
        statCards.forEach(card => {
            card.classList.add('animate-ready');
            observer.observe(card);
        });
    }

    setupNotifications() {
        // Setup real-time notifications
        if ('Notification' in window && Notification.permission === 'default') {
            Notification.requestPermission();
        }
    }

    showBrowserNotification(title, message) {
        if ('Notification' in window && Notification.permission === 'granted') {
            new Notification(title, {
                body: message,
                icon: '/static/favicon.ico',
                badge: '/static/favicon.ico'
            });
        }
    }

    // Utility methods
    formatNumber(num) {
        if (num >= 1000000) {
            return (num / 1000000).toFixed(1) + 'M';
        } else if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    }

    formatTime(timestamp) {
        const now = new Date();
        const time = new Date(timestamp);
        const diffInSeconds = Math.floor((now - time) / 1000);

        if (diffInSeconds < 60) {
            return 'Baru saja';
        } else if (diffInSeconds < 3600) {
            const minutes = Math.floor(diffInSeconds / 60);
            return `${minutes} menit lalu`;
        } else if (diffInSeconds < 86400) {
            const hours = Math.floor(diffInSeconds / 3600);
            return `${hours} jam lalu`;
        } else {
            const days = Math.floor(diffInSeconds / 86400);
            return `${days} hari lalu`;
        }
    }
}

// Global functions for dashboard interactions
function refreshDashboard() {
    if (window.lenteramuDashboard) {
        window.lenteramuDashboard.refreshDashboardData();
    }
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

function exportDashboardData() {
    // Export dashboard data functionality
    console.log('Exporting dashboard data...');
}

// Initialize dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the dashboard
    window.lenteramuDashboard = new LenteramuDashboard();

    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        .animate-ready {
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.6s ease-out;
        }
        
        .animate-in {
            opacity: 1;
            transform: translateY(0);
        }
        
        .notification-count.has-notifications {
            background: #e74c3c;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .refresh-indicator {
            animation: slideInRight 0.3s ease-out;
        }
        
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
            }
            to {
                transform: translateX(0);
            }
        }
    `;
    document.head.appendChild(style);

    // Load dark mode preference
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
    }
});

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LenteramuDashboard;
}
