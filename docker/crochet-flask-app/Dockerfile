#code from
FROM python:3.12-slim
#working directory
WORKDIR /app
#copy
COPY requirements.txt .
#requirments
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]
