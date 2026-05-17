FROM python:3.9-slim
WORKDIR /app
COPY setup.py setup.cfg ./
COPY app/ ./app/
RUN pip install -e .
EXPOSE 8080
ENV FLASK_APP=app:app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]