FROM python:3.7-alpine

RUN apk add --update musl-dev gcc libffi-dev make --no-cache

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY ./app .

EXPOSE 2222
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2222"]
