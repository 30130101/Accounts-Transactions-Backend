FROM python:3.11-slim-buster
RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE ${PORT}
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]