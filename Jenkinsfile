pipeline {
  agent any
  stages {
    stage('get excel and python file') {
      steps {
        sh '''wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/rules.xlsx
wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/CSV_formatter.py 
chmod 755 /var/lib/jenkins/workspace/test-erc-stage_main/CSV_formatter.py'''
        sh 'chmod 754 CSV_formatter.py'
      }
    }

    stage('run python file') {
      steps {
        sh '''python3 /var/lib/jenkins/workspace/test-erc-stage_main/CSV_formatter.py
'''
      }
    }

  }
}