document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.product-more-information-categories-titles');
    const titleEl = document.querySelector('.category-title');
    const infoEl = document.querySelector('.category-info');
    const dataEl = document.getElementById('product-data');
    function getLabel(field) {
        const labels = {
            innerTent: 'Внутренняя палатка',
            quickAssembly: 'Быстрая сборка',
            snowskirt: 'Ветрозащитная юбка',
            windows: 'Окна',
            stormGuys: 'Штормовые оттяжки',
            innerPockets: 'Внутренние карманы',
            mosquitoNet: 'Противомоскитная сетка',
            fireproof: 'Огнеупорная пропитка'
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
                <!-- Основные характеристики -->
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Назначение:</span>
                    <span class="value">${dataEl.dataset.purpose}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Количество мест:</span>
                    <span class="value">${dataEl.dataset.capacity}</span>
                </div>
        
                <!-- Конструкция -->
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Тип каркаса:</span>
                    <span class="value">${dataEl.dataset.frameType}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Геометрия:</span>
                    <span class="value">${dataEl.dataset.geometry}</span>
                </div>
                ${['innerTent', 'quickAssembly'].map(field => `
                    <div class="category-box d-flex flex-row justify-content-between mb-4">
                        <span class="category-name-label">${getLabel(field)}:</span>
                        <span class="value">${dataEl.dataset[field] === 'true' ? '+' : '-'}</span>
                    </div>
                `).join('')}
        
                <!-- Элементы конструкции -->
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Входы/Тамбуры/Комнаты:</span>
                    <span class="value">${dataEl.dataset.entries} / ${dataEl.dataset.vestibules} / ${dataEl.dataset.rooms}</span>
                </div>
                ${['snowskirt', 'windows'].map(field => `
                    <div class="category-box d-flex flex-row justify-content-between mb-4">
                        <span class="category-name-label">${getLabel(field)}:</span>
                        <span class="value">${dataEl.dataset[field] === 'true' ? '+' : '-'}</span>
                    </div>
                `).join('')}
        
                <!-- Дополнительные особенности -->
                ${['stormGuys', 'innerPockets', 'mosquitoNet', 'fireproof'].map(field => `
                    <div class="category-box d-flex flex-row justify-content-between mb-4">
                        <span class="category-name-label">${getLabel(field)}:</span>
                        <span class="value">${dataEl.dataset[field] === 'true' ? '+' : '-'}</span>
                    </div>
                `).join('')}
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Герметизация швов:</span>
                    <span class="value">${dataEl.dataset.seamSealing}</span>
                </div>
        
                <!-- Материалы -->
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Материал тента:</span>
                    <span class="value">${dataEl.dataset.tentMaterial || "Не указано"} (${dataEl.dataset.tentWaterproof || "0"} мм в.ст.)</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Материал дна:</span>
                    <span class="value">${dataEl.dataset.floorMaterial} (${dataEl.dataset.floorWaterproof} мм в.ст.)</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Материал дуг:</span>
                    <span class="value">${dataEl.dataset.poleMaterial}</span>
                </div>
        
                <!-- Размеры -->
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Внешние размеры:</span>
                    <span class="value">${dataEl.dataset.externalDimensions}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Внутренние размеры:</span>
                    <span class="value">${dataEl.dataset.internalDimensions}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Размеры в упаковке:</span>
                    <span class="value">${dataEl.dataset.packedDimensions}</span>
                </div>
                <div class="category-box d-flex flex-row justify-content-between mb-4">
                    <span class="category-name-label">Вес:</span>
                    <span class="value">${dataEl.dataset.weight} кг</span>
                </div>
            </div>
            `
        },

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