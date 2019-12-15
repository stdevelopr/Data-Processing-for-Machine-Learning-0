From python:3

ADD /data /data
WORKDIR /data
RUN pip install -r requirements.txt

CMD [ "python", "./data_processing.py" ]