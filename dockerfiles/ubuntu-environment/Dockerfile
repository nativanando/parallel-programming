#
# Necessary configuration to running MPI applications with the ubuntu distribuition
#

# Pull base image.
FROM ubuntu

# Installing dependencies.
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y curl git htop man unzip vim wget && \
  apt-get install -y python3-pip && \
  pip3 install --upgrade pip && \
  apt-get install -y openmpi-bin && \
  apt-get install -y openssh-server && \
  apt-get install -y openssh-client && \
  apt-get install -y libopenmpi-dev && \
  pip3 install mpi4py \
