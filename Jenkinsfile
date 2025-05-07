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
                sh 'pip3 install pytest'
                sh 'python main.py &'
                sh 'pytest test.py'
                sh 'git config --global --add safe.directory "/var/lib/jenkins/workspace/pipeline-1"'
                sh 'git push origin prod'
            }
        }
    }
}
