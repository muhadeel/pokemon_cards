# this is an official Python runtime, used as the parent image
FROM python:3.8.8-buster

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

#Install SQl server to enable mysqlcient
RUN apt-get update \
&& apt-get install -y build-essential \
&& apt-get install -y python3-all-dev \
&& apt-get install -y default-libmysqlclient-dev

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Flask app to run on
ENV LISTEN_PORT=5000
EXPOSE 5000

# execute the Flask app
RUN export FLASK_APP=pokemon_cards
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
