FROM python:3.9-slim

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m nltk.downloader stopwords

COPY ./app /code/app
COPY ./data/processed /code/data/processed
COPY ./models /code/models

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]