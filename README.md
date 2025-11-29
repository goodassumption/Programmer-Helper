# Programmer-Helper

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Набор Python-утилит для автоматизации рутинных задач программиста с помощью API [fifty.su](https://chat.fifty.su).

## О проекте

Многие программисты тратят значительное время на повторяющиеся задачи: написание шаблонного кода, создание документации, рефакторинг, генерацию коммит-сообщений и многое другое. Этот проект призван решить эту проблему, предоставляя набор простых и мощных утилит, которые используют нейросетевые модели через API `fifty.su` для автоматизации этих процессов.

Основная цель — повысить вашу продуктивность и позволить вам сосредоточиться на решении более сложных и интересных задач.

## Основные возможности

* **Форматирование коммитов**: Бот может переписывать ваши коммиты в формате Conventional Commits

## Установка

Для начала работы с проектом, следуйте этим шагам:

1. Склонируйте репозиторий

    ```bash
    git clone https://github.com/goodassumption/Programmer-Helper.git
    ```

2. Установите виртуальное окружение и активируйте его

    ```bash
    python3 -m venv .venv
    .venv/bin/activate # Для Linux
    .venv/Scripts/activate # Для Windows
    ```

3. Установите зависимости

    ```bash
    pip install -r requirements.txt
    ```

4. Можно пользоваться!

## Структура проекта

```text
PROGRAMMER-HELPER/
├── src/
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── commit_maker.py
│   ├── API.py
│   ├── choose_module.py
│   ├── errors.py
│   ├── requests.py
│   └── utils.py
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Настройка

Для работы с API `fifty.su` вам потребуется API-ключ.

1. Получите ваш API-ключ на сайте [chat.fifty.su](https://chat.fifty.su/api).
2. Создайте в директории src файл с именем `API.py`.
3. Добавьте в него ваш ключ в следующем формате:

    ```text
    api_key="ваш_api_ключ_здесь"
    ```

Проект автоматически подгрузит этот ключ для аутентификации запросов.

## Использование

Выполните ``python3 main.py`` в корневой директории проекта для начала работы

## Как внести вклад

1. Склонируйте репозиторий

    ```bash
    git clone https://github.com/goodassumption/Programmer-Helper.git
    ```

2. Установите виртуальное окружение и активируйте его

    ```bash
    python3 -m venv .venv
    .venv/bin/activate # Для Linux
    .venv/Scripts/activate # Для Windows
    ```

3. Установите зависимости

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте ветку под ваши изменения

    ```bash
    git checkout -b dev/amazing-feature
    ```

5. Закоммитьте изменения с использованием Conventional Commits

    ```bash
    git commit -m 'feat: add amazing feature'
    ```

6. Запушьте в ветку

    ```bash
    git push origin feature/amazing-feature
    ```

7. Откройте Pull Request

## Лицензия

Этот проект распространяется под лицензией GNU General Public License v3.0. Подробности смотрите в файле [LICENSE](LICENSE)

## Контакты

Связаться с разработчиком: [@goodassumption](https://t.me/goodassumption) в tg

## Благодарности

Спасибо [@Payziii](https://fifty.su) за такой прекрасный сайт!
