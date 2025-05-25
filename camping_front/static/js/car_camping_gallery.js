document.addEventListener('DOMContentLoaded', () => {
    let currentIndex = 0;
    const images = document.querySelectorAll('.other-img');
    const mainImage = document.getElementById('mainImage');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const thumbnailContainer = document.getElementById('thumbnailContainer');

    function setActiveImage(element) {
        currentIndex = parseInt(element.dataset.index);
        updateMainImage();
        updateThumbnails();
        scrollToThumbnail();
    }

    function updateMainImage() {
        mainImage.src = images[currentIndex].src;
    }

    function updateThumbnails() {
        images.forEach((img, index) => {
            img.classList.toggle('active', index === currentIndex);
        });
    }

    function scrollToThumbnail() {
        const activeThumbnail = images[currentIndex];
        activeThumbnail.scrollIntoView({
            behavior: 'smooth',
            block: 'nearest',
            inline: 'center'
        });
    }

    function switchImage(direction) {
        currentIndex += direction;
        if (currentIndex < 0) currentIndex = images.length - 1;
        if (currentIndex >= images.length) currentIndex = 0;
        updateMainImage();
        updateThumbnails();
        scrollToThumbnail();
    }

    prevBtn.addEventListener('click', () => switchImage(-1));
    nextBtn.addEventListener('click', () => switchImage(1));

    images.forEach(img => {
        img.addEventListener('click', () => setActiveImage(img));
    });

    if (images.length > 0) {
        mainImage.src = images[0].src;
        images[0].classList.add('active');
    }
});