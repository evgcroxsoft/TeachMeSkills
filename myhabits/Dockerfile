FROM python:3.10.6

WORKDIR /habits
COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install python-dotenv
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]