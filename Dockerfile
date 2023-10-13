FROM python:3.12-alpine

WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install 


# CMD ["poetry", "run", "uvicorn", "bewise.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "bewise/main.py"]
