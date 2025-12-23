pipeline {
    agent any

    environment {
        PYTHON = "python"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Jodlucifer/selenium-bdd-framework.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                pytest
                '''
            }
        }
    }

    post {
        always {
            echo "Test execution completed"
        }
        success {
            echo "BUILD SUCCESS"
        }
        failure {
            echo "BUILD FAILED"
        }
    }
}
