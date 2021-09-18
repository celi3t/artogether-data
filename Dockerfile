FROM python:3.8-slim 

RUN pip install -U python-dotenv
RUN pip install requests
RUN pip install arrow

# Create app directory
WORKDIR /app

# Bundle app source
COPY src /app

CMD [ "python3", "webserver.py" ]





