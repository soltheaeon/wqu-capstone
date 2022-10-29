FROM continuumio/miniconda3

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN while read requirement; do conda install --yes $requirement; done < requirements.txt