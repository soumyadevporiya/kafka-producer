FROM python:3.9
WORKDIR ./
COPY ./requirement.txt ./requirement.txt
RUN pip install -r requirement.txt
COPY ./kafka_producer.py ./kafka_producer.py
CMD ["python3","./kafka_producer.py"]
