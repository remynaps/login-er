FROM python:3.7-alpine
RUN apk add --update build-base libffi-dev
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENV FLASK_APP=server/api.py FLASK_ENV=development
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]