pipeline {
    agent { 
        docker { 
            image 'python:latest'
            args '-u root'
        } 
    }
    stages {
        stage('build') {
            steps {
                sh 'ls -a'
                sh 'apt update'
                sh 'pip3 install -r requirements.txt --user'
                sh 'python -d main.py'
                sh 'pytest test.py'
            }
        }
    }
}
