document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.toggle-services').forEach(button => {
        const carBlock = button.closest('.car-block');
        const priceElement = carBlock.querySelector('.dynamic-price');

        // Удаляем пробелы и преобразуем в число
        const basePrice = parseFloat(carBlock.dataset.basePrice.replace(/\s/g, '')) || 0;
        const totalWithServices = parseFloat(carBlock.dataset.totalWithServices.replace(/\s/g, '')) || 0;
        console.log('Parsed Base:', basePrice);
        console.log('Parsed Total:', totalWithServices);
        // Инициализация
        priceElement.textContent = totalWithServices.toLocaleString('ru-RU') + ' ₽';

        button.addEventListener('click', () => {
            const servicesList = carBlock.querySelector('.services-list');
            const isExpanded = servicesList.classList.toggle('expanded');

            priceElement.textContent = isExpanded
                ? basePrice.toLocaleString('ru-RU') + ' ₽'
                : totalWithServices.toLocaleString('ru-RU') + ' ₽';
        });
    });
});