FROM python:3.12-alpine

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirement.txt

ENTRYPOINT ["dbt"]