FROM jenkins/jenkins:2.317-jdk11
LABEL maintainer="tvquocchi@gmail.com"

USER root
RUN mkdir /var/log/jenkins
RUN chown -R jenkins:jenkins /var/log/jenkins

USER jenkins

ENV JAVA_OPTS="-Xmx8192m"
ENV JENKINS_OPTS=" --handlerCountMax=300"
ENV JENKINS_OPTS="--handlerCountMax=300 --logfile=/var/log/jenkins/jenkins.log"