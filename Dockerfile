   FROM python:3.12-slim
   WORKDIR /app
   COPY pwordstrengthtester.py .
   CMD ["python", "pwordstrengthtester.py"]