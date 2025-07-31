// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    const popupAd = document.getElementById('popup-ad');
    const closePopupBtn = document.getElementById('close-popup-btn');
    const countdownTimer = document.getElementById('countdown-timer'); // Получаем элемент таймера
    const countdownSpan = countdownTimer.querySelector('span'); // Получаем span внутри таймера

    let timeLeft = 5; // Начальное время в секундах
    const displayDuration = timeLeft * 1000; // 5 секунд в миллисекундах

    // Функция для обновления обратного отсчета
    function updateCountdown() {
        timeLeft--;
        countdownSpan.textContent = timeLeft; // Обновляем текст в span
        if (timeLeft <= 0) {
            clearInterval(countdownInterval); // Останавливаем интервал, когда время вышло
            countdownTimer.textContent = 'Теперь вы можете закрыть рекламу.'; // Сообщение, когда отсчет закончился
            showCloseButton(); // Показываем кнопку закрытия
        }
    }

    // Функция для показа кнопки закрытия (переместили сюда)
    function showCloseButton() {
        closePopupBtn.classList.remove('d-none'); // Удаляем d-none, чтобы показать кнопку
        closePopupBtn.focus(); // Можно дать фокус на кнопку для доступности
    }

    // Функция для скрытия всплывающего окна
    function hidePopup() {
        popupAd.classList.add('hidden'); // Добавляем класс hidden для плавного скрытия
    }

    // Запускаем интервал для обновления отсчета каждую секунду
    const countdownInterval = setInterval(updateCountdown, 1000);

    // Добавляем обработчик клика на кнопку закрытия
    closePopupBtn.addEventListener('click', hidePopup);
});