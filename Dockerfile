FROM python:3.6.4-slim-jessie
COPY . /textcompare
WORKDIR /textcompare
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
