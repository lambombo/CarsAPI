FROM python:3.6-alpine


COPY flask_manage.py config.py boot.sh requirements.txt ./

RUN pip install -r ./requirements.txt
