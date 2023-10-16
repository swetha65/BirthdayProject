pipeline{
    agent { docker { image 'python:3.12.0-alpine3.18' } }
    stages {
        stage('Clean Up'){
            steps{
                deleteDir()
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage("Run script"){
            steps{
                sh "python ./scripts/BirthdayChecker.py"
            }
        }
    }
}
