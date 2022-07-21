pipeline {
  agent any
  stages {
    stage('get excel and python file') {
      steps {
        sh '''whoami
pwd
wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/rules.xlsx -P /home/paul/ekvdatafile'''
        sh 'wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/CSV_formatter.py -P /home/paul/ekvdatafile'
      }
    }

  }
}