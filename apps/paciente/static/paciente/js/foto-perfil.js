document.addEventListener('DOMContentLoaded', function () {
   
    const avatars = document.querySelectorAll('.circle-avatar');
    
    if(avatars.length > 0) {
        avatars.forEach((avatar, index) => {

            const firstLetter = avatar.textContent.charAt(0);
            const colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6'];

            const colorIndex = firstLetter.charCodeAt(0) % colors.length;
            avatar.style.backgroundColor = colors[colorIndex];
        });
    }
    
});
