pipeline{
    agent any
    stages {
        stage('Clean Up'){
            steps{
                deleteDir()
            }
        stage("Clone Repo"){
            steps{
                sh "./scripts/BirthdayChecker.py"
            }
        }
        }
    }
}