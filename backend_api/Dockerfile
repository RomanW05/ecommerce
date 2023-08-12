FROM python:3

COPY /django_project/requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip3 install -r requirements.txt

COPY /django_project /api

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/api/entrypoint.sh" ]

CMD ["python", "manage.py", "runserver" ]
