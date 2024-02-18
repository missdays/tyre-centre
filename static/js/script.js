document.addEventListener('DOMContentLoaded', function() {
    var notifications = document.querySelectorAll('.notification');
    notifications.forEach(function(notification) {
        notification.addEventListener('animationend', function() {
            notification.remove();
        });
        setTimeout(function() {
            notification.classList.add('fadeOut');
        }, 3000);
    });
});