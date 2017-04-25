FROM python:2.7
MAINTAINER Glen Baker <iepathos@gmail.com>

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN cd PyML-0.7.14 && python setup.py build && python setup.py install

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader brown
RUN python -m nltk.downloader conll2000
RUN python -m nltk.downloader conll2002
RUN python -m nltk.downloader treebank


ENTRYPOINT ["python"]
CMD ["server.py"]