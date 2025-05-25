document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.car-camping-more-information-categories-titles');
    const titleEl = document.querySelector('.category-title');
    const infoEl = document.querySelector('.category-info');
    const dataEl = document.getElementById('product-data');
    const addServiceUrl = dataEl.dataset.addServiceUrl;
    let servicesData = [];
    try {
            servicesData = JSON.parse(dataEl.dataset.services);
        } catch (e) {
            console.error('Ошибка при загрузке услуг:', e);
        }
    function getLabel(field) {
        const labels = {
            steering: 'Гидроусилитель',
            cruiseControl: 'Круиз-контроль',
            multimedia: 'Магнитола',
            conditioner: 'Кондиционер',
            computer: 'Компьютер',
            kitchenEquipment: 'Газ. плита',
            windows: 'Окна с сетками'
        };
        return labels[field] || field;
    }
    // Данные для вкладок с корректными переменными
    const content = {
        'desc': {
            title: "Описание",
            text: dataEl.dataset.description
        },
        'spec': {
            title: "Характеристики",
            text: `
            <div class="d-flex flex-column">
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Д/Ш/В:</span>
                  <span class="value">${dataEl.dataset.length} / ${dataEl.dataset.width} / ${dataEl.dataset.height} мм</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Коробка:</span>
                  <span class="value">${dataEl.dataset.transmission}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Двигатель:</span>
                  <span class="value">${dataEl.dataset.engine}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Категория:</span>
                  <span class="value">${dataEl.dataset.category}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Шасси:</span>
                  <span class="value">${dataEl.dataset.chassis}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Топливный бак:</span>
                  <span class="value">${dataEl.dataset.fuelTank}л дизель</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">ABS/EBD/ASR:</span>
                    <span class="value">${
                        ['abs', 'ebd', 'asr'].some(f => dataEl.dataset[f] === 'true') ? '+' : '-'
                    }</span>
                </div>
                <!-- Булевы характеристики с преобразованием -->
            ${['steering', 'cruiseControl', 'multimedia', 'conditioner', 'computer', 'kitchenEquipment', 'windows']
                .map(field => `
                    <div class="category-box d-flex flex-row justify-content-between mb-4">
                        <span class="category-name-label">${getLabel(field)}:</span>
                        <span class="value">${dataEl.dataset[field] === 'true' ? '+' : '-'}</span>
                    </div>
                `).join('')}
                
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Ремни безопасности:</span>
                  <span class="value">${dataEl.dataset.seatbelts}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Спальные места:</span>
                  <span class="value">${dataEl.dataset.seats}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Кровать в алькове:</span>
                  <span class="value">${dataEl.dataset.alcovSleeperLength}×${dataEl.dataset.alcovSleeperWidth} мм</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Доп. спальное место:</span>
                  <span class="value">${dataEl.dataset.additionalSleeperLength}×${dataEl.dataset.additionalSleeperWidth} мм</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Холодильник:</span>
                  <span class="value">${dataEl.dataset.fridge}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Столовая группа:</span>
                  <span class="value">${dataEl.dataset.diningGroup} чел.</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Водоснабжение:</span>
                  <span class="value">${dataEl.dataset.waterSystem} л</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Маркиза:</span>
                  <span class="value">${dataEl.dataset.awning} м</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Велобагажник:</span>
                  <span class="value">${dataEl.dataset.bikeRack}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                  <span class="category-name-label">Внутр. высота:</span>
                  <span class="value">${dataEl.dataset.internalHeight} мм</span>
                </div>
            </div>
        `
        },
        'services': {
        title: "Доп. услуги",
        text: `
            <div class="d-flex flex-column">
                ${servicesData.map(service => `
                    <div class="category-box d-flex flex-row justify-content-between mb-4">
                        <span class="additional-label">${service.name}:</span>
                        <span class="value">${service.price} ₽</span>
                        <a href="${addServiceUrl.replace('0', service.id).replace(/0$/, dataEl.dataset.carId)}">
                            <img src="/media/pages_components/additional_service_add.png" class="add-btn">
                        </a>
                    </div>
                `).join('')}
            </div>
        `
        }
    };

    // Остальной код без изменений
    function switchTab(tab) {
        tabs.forEach(t => t.classList.remove('active'));
        const tabId = tab.id;

        if (!content[tabId]) {
            console.error('Контент не найден:', tabId);
            return;
        }

        titleEl.textContent = content[tabId].title;
        infoEl.innerHTML = content[tabId].text;
        tab.classList.add('active');
    }

    switchTab(document.getElementById('desc'));
    tabs.forEach(tab => tab.addEventListener('click', () => switchTab(tab)));
});