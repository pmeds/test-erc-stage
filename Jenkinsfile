pipeline {
  agent any
  stages {
    stage('get excel and python file') {
      steps {
        sh '''whoami
pwd
wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/rules.xlsx'''
        sh '''wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/CSV_formatter.py 
chmod u+x /var/lib/jenkins/workspace/test-erc-stage_main/CSV_formatter.py'''
      }
    }

  }
}