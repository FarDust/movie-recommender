FROM python3.10-slim-bullseye

RUN apt-get update
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8080

CMD ["gunicorn", "--bind=0.0.0.0:8080", "--worker-class=uvicorn.workers.UvicornWorker", "movie_recommender/movie_recommender:app"]
