    const catId = "{{ cat.id }}";

    document.addEventListener('DOMContentLoaded', function() {
        const boyBtn = document.getElementById('boy-btn');
        const girlBtn = document.getElementById('girl-btn');
        const result = document.getElementById('result');

        boyBtn.addEventListener('click', function() {
            checkAnswer('men');
        });

        girlBtn.addEventListener('click', function() {
            checkAnswer('girl');
        });

        function checkAnswer(answer) {
            const url = '/check_answer/' + catId + '/' + answer + '/';  // Используем значение catId из JavaScript-переменной
            const xhr = new XMLHttpRequest();

            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    result.textContent = response.message;
                    loadNextCat();
                }
            };

            xhr.open('GET', url, true);
            xhr.send();
        }

        function loadNextCat() {
            const url = '/next_cat/';
            const xhr = new XMLHttpRequest();

            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    if (response.cat) {
                        updateCat(response.cat);
                    } else {
                        result.textContent = 'Игра окончена';
                        boyBtn.disabled = true;
                        girlBtn.disabled = true;
                    }
                }
            };

            xhr.open('GET', url, true);
            xhr.send();
        }

        function updateCat(cat) {
            const img = document.querySelector('img');
            img.src = cat.photo;
            result.textContent = '';
        }

        // Загрузка первого кота при открытии страницы
        loadNextCat();
    });

