pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "Build Stage Start"

#ENV
export IMAGE_NAME=krx_fast_api
export IMAGE_TAG=latest

#DOCKER BUILD
docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'''
      }
    }

    stage('Deploy') {
      steps {
        sh '''echo "Deploy Stage Start"

#ENV
export CONTAINER_NAME=krx_fast_api
export PORT=3100
export IMAGE_TAG=latest

#RUN CONATAINER
docker rm -f ${CONTAINER_NAME} || true\'
docker run -d --name ${CONTAINER_NAME} -p ${PORT}:${PORT} ${CONTAINER_NAME}:${IMAGE_TAG}

echo "Deploy Stage End"'''
      }
    }

    stage('Process After Deploy') {
      steps {
        sh '''echo "Process After Deploy start"


'''
      }
    }

  }
}