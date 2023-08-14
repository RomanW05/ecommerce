FROM python:3

COPY /ecommerce/backend_api/requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip3 install -r requirements.txt

COPY /ecommerce/backend_api /api

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/api/entrypoint.sh" ]

CMD ["python", "manage.py", "runserver" ]
