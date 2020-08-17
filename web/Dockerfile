FROM ubuntu:18.04
MAINTAINER gyumin "gmlee329@naver.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /web
WORKDIR /web
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["server.py"]
