FROM python:3.6.9
WORKDIR /app
COPY app.py .
COPY create.py .
COPY requirements.txt .
COPY application .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]