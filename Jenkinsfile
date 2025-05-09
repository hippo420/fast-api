pipeline {
  agent any
  stages {
    stage('check out') {
      steps {
        git(url: 'https://github.com/hippo420/fast-api.git', branch: 'master')
      }
    }

    stage('Deploy') {
      steps {
        sh 'echo "deploy"'
      }
    }

    stage('Process After Deploy') {
      steps {
        sh 'echo "Process After Deploy"'
      }
    }

  }
}