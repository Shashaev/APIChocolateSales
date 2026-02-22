# APIChocolateSales

Проект представляет собой сервис для предсказывания стоимости партии шоколада. Данные для обучения модели брались из [Kaggle](https://www.kaggle.com/datasets/saidaminsaidaxmadov/chocolate-sales). Доступ к функциональности идёт через WebAPI (FastAPI).

## Запуск проекта

Запуск проекта через Docker:
```bash
sudo docker run -p 9876:9876 shashaevkirill/apichocolatesales
```

Далее идёт инструкция по мануальному запуску.

### Что нужно для запуска?

- [Git](https://git-scm.com/downloads)
- [Python3.11+](https://www.python.org/downloads/)

### Запуск:
1. Клонирование репозитория и переход в директорию проекта:
   ```bash
   git clone https://github.com/Shashaev/APIChocolateSales.git
   cd APIChocolateSales
   ```
2. Создание и активация виртуального окружения:
  - **Windows**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
  - **Linux/macOS**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Установка зависимостей:
    ```bash
    pip install -r requirements/prod.txt
    ```
4. Запуск проекта:
  - **Windows**
    ```bash
    python src/main.py
    ```
  - **Linux/macOS**
    ```bash
    python3 src/main.py
    ```

После запуска вы можете отправлять запросы напрямую или использовать [свагер](http://127.0.0.1:9876/docs) от FastAPI.
