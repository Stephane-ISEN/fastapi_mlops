FROM continuumio/miniconda3 
WORKDIR /home/app
RUN apt-get update
COPY requirements.txt /home/app/
RUN pip install -r requirement.txt
COPY . /home/app
CMD streamlit run --server.port $PORT Home.py