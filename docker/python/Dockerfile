#base image
FROM python:3.11-slim
#working dir
WORKDIR /app
#copy code 
COPY flask-app/ .
#required libarirs
RUN pip install flask
#run
EXPOSE 5000
CMD ["python","app.py"]
