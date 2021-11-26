FROM jenkins/jenkins:latest
LABEL maintainer="tvquocchi@gmail.com"

ARG USER=jenkins
ARG GROUP=jenkins

USER root
RUN apt update
RUN apt install -y sudo
RUN echo "%$USER ALL=NOPASSWD:ALL" >> /etc/sudoers

USER ${USER}
RUN echo "$USER"
RUN sudo mkdir /var/log/${USER}
RUN sudo chown -R ${USER}:${GROUP} /var/log/${USER}

# https://support.cloudbees.com/hc/en-us/articles/209715698-How-to-add-Java-arguments-to-Jenkins?mobile_site=true
ENV JAVA_OPTS="-Xmx8192m"
# http://winstone.sourceforge.net/#commandLine
ENV JENKINS_OPTS="--logfile=/var/log/$USER/$USER.log"
