FROM python:3

COPY /personal_website/requirements.txt /personal_website/requirements.txt

WORKDIR /personal_website

RUN pip3 install -r requirements.txt

COPY /personal_website /personal_website

CMD ["python", "app.py", "-h", "0.0.0.0", "-p", "8080" ]