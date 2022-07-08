FROM python:3.8.10

# RUN adduser python
# USER python
# WORKDIR /habits
COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "runner.py" ]