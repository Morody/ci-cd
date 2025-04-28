pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'ls -a'
                sh 'python --version'
            }
        }
    }
}
