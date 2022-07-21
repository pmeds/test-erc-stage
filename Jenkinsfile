pipeline {
  agent any
  stages {
    stage('get excel and python file') {
      steps {
        sh 'wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/rules.xlsx'
        sh 'wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/CSV_formatter.py'
      }
    }

  }
}