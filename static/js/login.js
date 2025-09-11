// LENTERAMU Login Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Login page loaded');
    
    // Initialize login functionality
    initLoginForm();
    initPasswordToggle();
    initDemoAccounts();
    initFormValidation();
    initAnimations();
    
    // Debug: Test if elements are clickable
    testClickability();
});

function testClickability() {
    const inputs = document.querySelectorAll('input, select, button');
    inputs.forEach((element, index) => {
        element.addEventListener('click', function() {
            console.log(`Element ${index} clicked:`, element);
        });
        
        element.addEventListener('focus', function() {
            console.log(`Element ${index} focused:`, element);
        });
    });
}

// Login Form Functionality
function initLoginForm() {
    const loginForm = document.querySelector('.login-form');
    const loginBtn = document.querySelector('.login-btn');
    
    console.log('Login form:', loginForm);
    console.log('Login button:', loginBtn);
    
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            console.log('Form submitted');
            
            const formData = new FormData(this);
            const username = formData.get('username');
            const password = formData.get('password');
            const role = formData.get('role');
            
            console.log('Form data:', { username, password, role });
            
            // Validate form
            if (!validateForm(username, password, role)) {
                e.preventDefault();
                return false;
            }
            
            // Show loading state
            showLoading(loginBtn);
            
            // Let form submit normally for server processing
        });
    }
}

// Password Toggle Functionality
function initPasswordToggle() {
    const toggleBtn = document.querySelector('.toggle-password');
    const passwordInput = document.getElementById('password');
    
    if (toggleBtn && passwordInput) {
        toggleBtn.addEventListener('click', function() {
            const type = passwordInput.type === 'password' ? 'text' : 'password';
            passwordInput.type = type;
            
            const icon = this.querySelector('i');
            icon.classList.toggle('fa-eye');
            icon.classList.toggle('fa-eye-slash');
        });
    }
}

// Demo Accounts Functionality
function initDemoAccounts() {
    const demoAccounts = document.querySelectorAll('.demo-account');
    
    demoAccounts.forEach(account => {
        account.addEventListener('click', function() {
            const username = this.dataset.username;
            const password = this.dataset.password;
            const role = this.dataset.role;
            
            // Fill form with demo data
            document.getElementById('username').value = username;
            document.getElementById('password').value = password;
            document.getElementById('role').value = role;
            
            // Add visual feedback
            this.style.background = 'rgba(102, 126, 234, 0.3)';
            setTimeout(() => {
                this.style.background = '';
            }, 200);
            
            // Show notification
            showNotification('Demo akun telah diisi. Klik "Masuk" untuk melanjutkan.', 'info');
        });
    });
}

// Form Validation
function initFormValidation() {
    const inputs = document.querySelectorAll('input, select');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            clearFieldError(this);
        });
    });
}

function validateForm(username, password, role) {
    let isValid = true;
    
    // Validate username
    if (!username || username.trim().length < 3) {
        showFieldError('username', 'Username minimal 3 karakter');
        isValid = false;
    }
    
    // Validate password
    if (!password || password.length < 6) {
        showFieldError('password', 'Password minimal 6 karakter');
        isValid = false;
    }
    
    // Validate role
    if (!role) {
        showFieldError('role', 'Pilih role terlebih dahulu');
        isValid = false;
    }
    
    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    
    switch (fieldName) {
        case 'username':
            if (value.length < 3) {
                showFieldError(fieldName, 'Username minimal 3 karakter');
                return false;
            }
            break;
        case 'password':
            if (value.length < 6) {
                showFieldError(fieldName, 'Password minimal 6 karakter');
                return false;
            }
            break;
        case 'role':
            if (!value) {
                showFieldError(fieldName, 'Pilih role terlebih dahulu');
                return false;
            }
            break;
    }
    
    showFieldSuccess(fieldName);
    return true;
}

function showFieldError(fieldName, message) {
    const field = document.getElementById(fieldName) || document.querySelector(`[name="${fieldName}"]`);
    const inputGroup = field.closest('.input-group');
    
    inputGroup.classList.add('error');
    inputGroup.classList.remove('success');
    
    // Remove existing error message
    const existingError = inputGroup.parentNode.querySelector('.error-message');
    if (existingError) {
        existingError.remove();
    }
    
    // Add error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
    inputGroup.parentNode.appendChild(errorDiv);
}

function showFieldSuccess(fieldName) {
    const field = document.getElementById(fieldName) || document.querySelector(`[name="${fieldName}"]`);
    const inputGroup = field.closest('.input-group');
    
    inputGroup.classList.remove('error');
    inputGroup.classList.add('success');
    
    // Remove error message
    const existingError = inputGroup.parentNode.querySelector('.error-message');
    if (existingError) {
        existingError.remove();
    }
}

function clearFieldError(field) {
    const inputGroup = field.closest('.input-group');
    inputGroup.classList.remove('error');
    
    const errorMessage = inputGroup.parentNode.querySelector('.error-message');
    if (errorMessage) {
        errorMessage.remove();
    }
}

// Loading State
function showLoading(button) {
    button.classList.add('loading');
    button.disabled = true;
}

function hideLoading(button) {
    button.classList.remove('loading');
    button.disabled = false;
}

// Login Process
function processLogin(username, password, role) {
    const loginBtn = document.querySelector('.login-btn');
    
    // Simulate API call
    // In real implementation, this would be an actual API call
    const isValidLogin = validateCredentials(username, password, role);
    
    if (isValidLogin) {
        showNotification('Login berhasil! Mengalihkan...', 'success');
        
        setTimeout(() => {
            // Redirect based on role
            redirectToRoleDashboard(role);
        }, 1000);
    } else {
        hideLoading(loginBtn);
        showNotification('Username atau password salah!', 'error');
    }
}

function validateCredentials(username, password, role) {
    // Demo credentials validation
    const demoCredentials = {
        'demo_student': { password: 'demo123', role: 'student' },
        'demo_teacher': { password: 'demo123', role: 'teacher' },
        'demo_admin': { password: 'demo123', role: 'admin' }
    };
    
    const user = demoCredentials[username];
    return user && user.password === password && user.role === role;
}

function redirectToRoleDashboard(role) {
    const redirectUrls = {
        'student': '/dashboard/siswa',
        'teacher': '/teacher/workflow',
        'admin': '/dashboard/admin'
    };
    
    const url = redirectUrls[role] || '/dashboard';
    window.location.href = url;
}

// Notification System
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => {
        notification.remove();
    });
    
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    
    const iconMap = {
        'success': 'fa-check-circle',
        'error': 'fa-exclamation-circle',
        'info': 'fa-info-circle',
        'warning': 'fa-exclamation-triangle'
    };
    
    const colorMap = {
        'success': '#27ae60',
        'error': '#e74c3c',
        'info': '#3498db',
        'warning': '#f39c12'
    };
    
    notification.innerHTML = `
        <i class="fas ${iconMap[type]}"></i>
        <span>${message}</span>
        <button class="notification-close">&times;</button>
    `;
    
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${colorMap[type]};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        z-index: 10000;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 350px;
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove
    const autoRemoveTimeout = setTimeout(() => {
        removeNotification(notification);
    }, 5000);
    
    // Close button
    notification.querySelector('.notification-close').addEventListener('click', function() {
        clearTimeout(autoRemoveTimeout);
        removeNotification(notification);
    });
}

function removeNotification(notification) {
    notification.style.transform = 'translateX(100%)';
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 300);
}

// Animation Initialization
function initAnimations() {
    // Stagger form field animations
    const formGroups = document.querySelectorAll('.form-group');
    formGroups.forEach((group, index) => {
        group.style.animationDelay = `${index * 0.1}s`;
        group.classList.add('fade-in-up');
    });
    
    // Demo accounts animation
    const demoAccounts = document.querySelectorAll('.demo-account');
    demoAccounts.forEach((account, index) => {
        account.style.animationDelay = `${0.5 + (index * 0.1)}s`;
        account.classList.add('fade-in-up');
    });
    
    // Feature items animation
    const featureItems = document.querySelectorAll('.feature-item');
    featureItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.2}s`;
        item.classList.add('fade-in-right');
    });
}

// Keyboard Shortcuts
document.addEventListener('keydown', function(e) {
    // Enter to submit form
    if (e.key === 'Enter' && e.target.tagName !== 'BUTTON') {
        const loginForm = document.querySelector('.login-form');
        if (loginForm) {
            loginForm.requestSubmit();
        }
    }
    
    // Escape to clear form
    if (e.key === 'Escape') {
        clearForm();
    }
});

function clearForm() {
    const form = document.querySelector('.login-form');
    if (form) {
        form.reset();
        
        // Clear validation states
        const inputGroups = document.querySelectorAll('.input-group');
        inputGroups.forEach(group => {
            group.classList.remove('error', 'success');
        });
        
        // Clear error messages
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(message => message.remove());
        
        showNotification('Form telah dibersihkan', 'info');
    }
}

// Auto-fill detection
function detectAutoFill() {
    const inputs = document.querySelectorAll('input');
    
    inputs.forEach(input => {
        input.addEventListener('animationstart', function(e) {
            if (e.animationName === 'autofill') {
                this.classList.add('autofilled');
            }
        });
    });
}

// Form persistence (remember form state)
function initFormPersistence() {
    const form = document.querySelector('.login-form');
    const rememberCheckbox = document.querySelector('input[name="remember_me"]');
    
    // Load saved form data
    if (localStorage.getItem('lenteramu_remember_form') === 'true') {
        const savedUsername = localStorage.getItem('lenteramu_username');
        const savedRole = localStorage.getItem('lenteramu_role');
        
        if (savedUsername) {
            document.getElementById('username').value = savedUsername;
        }
        if (savedRole) {
            document.getElementById('role').value = savedRole;
        }
        
        rememberCheckbox.checked = true;
    }
    
    // Save form data on change
    form.addEventListener('change', function() {
        if (rememberCheckbox.checked) {
            localStorage.setItem('lenteramu_remember_form', 'true');
            localStorage.setItem('lenteramu_username', document.getElementById('username').value);
            localStorage.setItem('lenteramu_role', document.getElementById('role').value);
        } else {
            localStorage.removeItem('lenteramu_remember_form');
            localStorage.removeItem('lenteramu_username');
            localStorage.removeItem('lenteramu_role');
        }
    });
}

// Initialize additional features
document.addEventListener('DOMContentLoaded', function() {
    detectAutoFill();
    initFormPersistence();
    
    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        .fade-in-up {
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 0.6s ease-out forwards;
        }
        
        .fade-in-right {
            opacity: 0;
            transform: translateX(20px);
            animation: fadeInRight 0.6s ease-out forwards;
        }
        
        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInRight {
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes autofill {
            to {
                color: transparent;
            }
        }
        
        input:-webkit-autofill {
            animation-delay: 1s;
            animation-name: autofill;
            animation-fill-mode: both;
        }
    `;
    document.head.appendChild(style);
});

// Performance monitoring
function initPerformanceMonitoring() {
    if ('performance' in window) {
        window.addEventListener('load', function() {
            setTimeout(() => {
                const perfData = performance.getEntriesByType('navigation')[0];
                const loadTime = perfData.loadEventEnd - perfData.loadEventStart;
                
                if (loadTime > 2000) {
                    console.warn('Login page load time is slow:', loadTime + 'ms');
                }
            }, 0);
        });
    }
}

// Initialize performance monitoring
initPerformanceMonitoring();
