// static/js/banner-switcher.js

document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('banner-carousel');
    if (!carousel) return;

    const banners = carousel.querySelectorAll('.banner-item');
    if (banners.length <= 1) return;

    let currentBannerIndex = 0;
    const intervalTime = 5000; // 5 секунд, вы можете изменить на 30000

    const switchBanner = () => {
        // Убираем класс 'active' у текущего баннера
        banners[currentBannerIndex].classList.remove('active');

        // Переходим к следующему баннеру по кругу
        currentBannerIndex = (currentBannerIndex + 1) % banners.length;

        // Добавляем класс 'active' новому баннеру
        banners[currentBannerIndex].classList.add('active');
    };

    // Убедимся, что первый баннер изначально активен
    if (banners[currentBannerIndex] && !banners[currentBannerIndex].classList.contains('active')) {
        banners[currentBannerIndex].classList.add('active');
    }

    // Запускаем автоматическое переключение баннеров с заданным интервалом
    setInterval(switchBanner, intervalTime);
});