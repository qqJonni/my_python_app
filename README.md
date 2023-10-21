# Простое приложение на Python с использованием Flask и Docker Compose

Это простое приложение на Python, которое предоставляет REST API для управления значениями ключ=значение. Приложение использует Flask для обработки запросов и работает в контейнере Docker. Кроме того, для хранения данных используется NoSQL база данных MongoDB, также запущенная в контейнере Docker.

## Содержание
- [Запуск приложения](#запуск-приложения)
- [API Endpoints](#api-endpoints)
- [Примеры запросов](#примеры-запросов)
- [Остановка приложения](#остановка-приложения)

## Запуск приложения

Для запуска приложения вам потребуется Docker и Docker Compose.

1. Клонируйте репозиторий:

```properties
git clone https://github.com/qqJonni/my_python_app.git
```
1. Соберите и запустите контейнеры с помощью Docker Compose:
```properties
docker-compose up --build
```
Приложение будет доступно по адресу http://localhost:8080.

## API Endpoints

Приложение предоставляет следующие API endpoints:

* POST /create: Создать новое значение ключ=значение.
* PUT /update/<key>: Обновить значение для указанного ключа.
* GET /read/<key>: Получить значение по ключу.

## Примеры запросов

Вы можете использовать curl или любой другой HTTP-клиент для взаимодействия с API.
* Создать значение:
```properties
curl -X POST -H "Content-Type: application/json" -d '{"key": "example", "value": "some_value"}' http://localhost:8080/create
```
* Обновить значение:
```properties
curl -X PUT -H "Content-Type: application/json" -d '{"value": "new_value"}' http://localhost:8080/update/example
```
* Прочитать значение:
```properties
curl http://localhost:8080/read/example
```
## Остановка приложения
Чтобы остановить приложение и удалить контейнеры, выполните следующую команду:
```properties
docker-compose down
```
## Зависимости
* Python 3.11
* Flask
* Docker
* Docker Compose
* MongoDB (запускается в контейнере)

### Примечания

Код написан с целью выполнения тестового задания.
