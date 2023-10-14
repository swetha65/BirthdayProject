pipeline{
    agent any
    stages {
        stage('Clean Up'){
            steps{
                deleteDir()
            }
        }
        stage("Run script"){
            steps{
                sh "./scripts/BirthdayChecker.py"
            }
        }
    }
}
