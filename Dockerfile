FROM python:3.13-slim

WORKDIR /app

COPY test_api.py ./

CMD ["python", "-m", "unittest", "-v", "test_api.py"]
