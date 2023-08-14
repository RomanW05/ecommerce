FROM python:3

COPY /backend_api/django_proyect/requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip3 install -r requirements.txt

COPY /backend_api/django_proyect /api

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/api/entrypoint.sh" ]

CMD ["python", "manage.py", "runserver" ]
