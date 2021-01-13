FROM python:3.8
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
# copy requirements and install (so that changes to files do not mean rebuild cannot be cached)
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy all files into the container
COPY . /usr/src/app



