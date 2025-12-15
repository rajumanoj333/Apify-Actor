FROM apify/actor-python:3.9

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src ./src

CMD ["python", "-m", "src.main"]