document.addEventListener('DOMContentLoaded', function() {
    const popupAd = document.getElementById('popup-ad');
    const closePopupBtn = document.getElementById('close-popup-btn');
    const countdownSpan = document.getElementById('countdown');
    let countdown = 5;

    // Функция для скрытия баннера
    function hidePopup() {
        popupAd.style.display = 'none';
    }

    // Обработчик для кнопки закрытия
    closePopupBtn.addEventListener('click', hidePopup);

    // Таймер обратного отсчёта
    const timerInterval = setInterval(() => {
        countdown--;
        countdownSpan.textContent = countdown;

        if (countdown <= 0) {
            clearInterval(timerInterval);
            hidePopup();
        }
    }, 1000);
});