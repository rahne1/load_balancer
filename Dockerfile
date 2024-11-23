FROM python:3
RUN pip install flask
COPY ./cwd/app.py /app/app.py
CMD ["python", "/app/app.py"]