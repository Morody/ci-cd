pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'ls -a'
                sh 'pip install -r requirements.txt'
                sh 'python main.py'
            }
        }
    }
}
