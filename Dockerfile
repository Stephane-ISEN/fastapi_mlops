FROM continuumio/miniconda3 
WORKDIR /home/app
RUN apt-get update
COPY requirements.txt /home/app/
RUN pip install -r requirements.txt
COPY . /home/app
CMD mlflow server --host 0.0.0.0 -p $PORT \
 --default-artifact-root $ARTIFACT_STORE_URI \
 --backend-store-uri $BACKEND_STORE_URI