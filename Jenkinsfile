pipeline {
  agent any
  stages {
    stage('get excel and python file') {
      steps {
        sh '''wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/rules.xlsx
wget https://raw.githubusercontent.com/pmeds/test-erc-stage/main/CSV_formatter.py 
chmod 754 /var/lib/jenkins/workspace/test-erc-stage_main/CSV_formatter.py'''
      }
    }

    stage('run python file') {
      steps {
        sh '''python3 /var/lib/jenkins/workspace/test-erc-stage_main/CSV_formatter.py
'''
      }
    }

    stage('ekv upload games') {
      steps {
        script {
          if (fileExists('games-upload.csv')) {
            sh 'echo "uploading games rules"'
            sh 'edgekv-importer --edgerc $EDGERC --namespace poc_gpdc_redirects --group redirects --account-key 1-6JHGX --csv games-upload.csv --key hash'
          }
        }

      }
    }

    stage('ekv upload general') {
      steps {
        script {
          if (fileExists('general-upload.csv')) {
            sh 'echo "uploading games rules"'
            sh 'edgekv-importer --edgerc $EDGERC --namespace general --group redirects --account-key 1-6JHGX --csv games-upload.csv --key hash'
          }
        }

      }
    }

    stage('ekv upload support') {
      steps {
        script {
          if (fileExists('support-upload.csv')) {
            sh 'echo "uploading games rules"'
            sh 'edgekv-importer --edgerc $EDGERC --namespace support --group redirects --account-key 1-6JHGX --csv games-upload.csv --key hash'
          }
        }

      }
    }

    stage('clean up on success') {
      steps {
        cleanWs(cleanWhenSuccess: true)
      }
    }

  }
  tools {
    nodejs 'njs'
  }
  environment {
    EDGERC = credentials('pauledgerc')
  }
}