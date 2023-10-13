### Этот проект является ответом на тестовое задание на позицию junior-разработчика в компанию bewise

### Инструкция по разворачиванию проекта:
- Скачайте проект, перейдите в основную папку проекта и добавьте .env и .env-docker
    >Для примера:\
    >.env:\
    >DB_HOST=localhost\
    >DB_NAME=tz_bewise\
    >DB_USER=gg\
    >DB_PASSWORD=123\
    >DB_PORT=5432\
    >Для .env-docker все то же самое.
- После для сборки проекта пропишите команду **"docker-compose up --build"**
- После этого если у вас windows перейдите на адрес (ваш ipV4 + : + 8000), для примера -> 192.168.0.12:8000. Если linux то 0.0.0.0:8000
- Если вы хотите использовать проект без Dockera, тогда -> **"pip install -r requirements.txt"** а после "**"uvicorn src.main:app"**