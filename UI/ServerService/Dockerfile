FROM python:3

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip && \
    pip3 install -e .[dev]

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
