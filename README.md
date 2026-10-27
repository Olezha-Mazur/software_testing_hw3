# Docker и CI CD для API автотеста

Проект проверяет публичный API [JSONPlaceholder](https://jsonplaceholder.typicode.com/). Автотест выполняет `GET /todos/1`, проверяет HTTP-статус `200`, тип ответа и ключевые поля JSON-объекта.

## Требования

- Docker 24+ с доступом в интернет;
- Git — если проект запускается из клона репозитория.

## Локальный запуск

Из корня репозитория соберите образ:

```bash
docker build -t api-test .
```

Запустите контейнер:

```bash
docker run --rm api-test
```

При успехе `unittest` выводит результат проверки, а команда завершается с кодом `0`. Если API недоступен или проверка не проходит, `unittest` возвращает ненулевой код; Docker передаёт его вызывающей среде.

## Состав проекта

- `test_api.py` — API-автотест на стандартной библиотеке Python;
- `Dockerfile` — воспроизводимый образ на `python:3.13-slim`; тест запускается автоматически через `CMD`;
- `.dockerignore` — исключает Git-метаданные, виртуальные окружения, кэши и документацию из контекста сборки;
- `.github/workflows/ci.yml` — GitHub Actions workflow.

## CI

Workflow расположен в `.github/workflows/ci.yml` и запускается при каждом `push` и `pull_request`. Он выполняет полную цепочку:

```text
checkout → docker build → docker run → API test → result job
```

Запуски workflow доступны на [странице GitHub Actions](https://github.com/Olezha-Mazur/software_testing_hw3/actions).