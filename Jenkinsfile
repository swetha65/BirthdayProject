pipeline{
    agent any
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
