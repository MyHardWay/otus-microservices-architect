# our base image
FROM python:3.9-alpine


# install Python modules needed by the Python app

RUN apk add build-base
RUN pip install -U Flask
RUN pip install -U psycopg2-binary
RUN pip install -U Flask-SQLAlchemy

# copy files required for the app to run
COPY app.py /usr/src/app/

# tell the port number the container should expose
EXPOSE 8000

# run the application
CMD ["python", "/usr/src/app/app.py"]
