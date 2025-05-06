pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'ls -a'
                sh 'apt update'
                sh 'pip3 install -r requirements.txt --user'
                sh 'python main.py'
            }
        }
    }
}
