
# specifiy base image
FROM ubuntu:16.04

# Update the sources list
RUN apt-get update && \
    apt-get -y upgrade

# install useful system tools and libraries
RUN apt-get install -y libfreetype6-dev && \
    apt-get install -y libglib2.0-0 \
                       libxext6 \
                       libsm6 \
                       libxrender1 \
                       libblas-dev \
                       liblapack-dev \
                       gfortran \
                       libfontconfig1 --fix-missing

RUN apt-get install -y tar \
                    git \
                    curl \
                    nano \
                    wget \
                    dialog \
                    net-tools \
                    build-essential \
                    sqlite3 \
                    libsqlite3-dev

# install Python and pip package manager
RUN apt-get install -y python3-dev \
                       python-distribute \
                       python3-pip

# intall useful and/or required Python libraries to run your script
RUN pip3 install matplotlib \
                seaborn \
                pandas \
                numpy \
                scipy \
                sklearn \
                python-dateutil \
                gensim

COPY bin/ /climate/bin/
COPY data/ /climate/data/
