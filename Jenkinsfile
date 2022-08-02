pipeline {
  agent any
  stages {
    stage('get excel and python file') {
      steps {
        sh '''npm version
wget https://raw.githubusercontent.com/akamai/edgeworkers-examples/master/edgekv/utils/edgekv-importer/index.js 
wget https://raw.githubusercontent.com/akamai/edgeworkers-examples/master/edgekv/utils/edgekv-importer/package-lock.json 
wget https://raw.githubusercontent.com/akamai/edgeworkers-examples/master/edgekv/utils/edgekv-importer/package.json 
npm install -g


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

        sh 'cp games-upload.csv /resources/jenkins-ekvdata/games-upload-`date +%Y-%m-%d-%H-%M`.csv'
        script {
          sshagent (credentials: ['git-log']) {
            sh '''cd /resources/jenkins-ekvdata
pwd
git pull
git add .
git commit -m "upload `date +%Y-%m-%d-%H-%M`"
git branch -M main
git remote -v
git push origin main'''
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