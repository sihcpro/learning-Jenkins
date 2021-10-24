pipeline {
  agent any

  stages {
    stage('Preparation') { // for display purposes
      steps {
        //# Pre-install
        sh "sudo apt update"
        sh "sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev"
        //# Get the Python.
        sh "curl -O https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tar.xz"
        sh "tar -xf Python-3.8.12.tar.xz"
        sh "cd Python-3.8.12 && ./configure --enable-optimizations && make -j 4 && sudo make altinstall || sudo make install"
        sh "python3.8 --version"
        //# Get the Python required libraries.
        sh "sudo apt install -y python3 python3-dev python3-pip"
        sh "sudo apt install -y libxml2-dev libxslt-dev musl-dev"
        //# Get project
        sh "rm -rf lrn_jenkin"
        sh "git clone https://github.com/sihcpro/learning-Jenkins.git lrn_jenkin"
        sh "cd lrn_jenkin && pip install -r requirements.txt"
      }
    }
    stage('Build') {
      parallel {
        stage('Build 1') {
          steps {
            //# Run project
            sh "cd lrn_jenkin && CRAW_EVERY_SECONDS=0 SOF_PAGE_SIZE=19 python3 -m src "
          }

          post {
            success {
              archiveArtifacts 'lrn_jenkin/output/*.csv'
            }
          }
        }
        stage('Build 2') {
          steps {
            //# Run project
            sh "cd lrn_jenkin && CRAW_EVERY_SECONDS=0 SOF_PAGE_SIZE=19 python3 -m src "
          }

          post {
            success {
              archiveArtifacts 'lrn_jenkin/output/*.csv'
            }
          }
        }
      }
    }
  }
}
