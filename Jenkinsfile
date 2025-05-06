pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'ls -a'
                sh 'virtualenv venv -p python3'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'python main.py'
                
            }
        }
    }
}
