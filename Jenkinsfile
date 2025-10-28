pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/F1Z3R/Lab2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecopslab_app .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest > result.log || true'
                archiveArtifacts artifacts: 'result.log'
            }
        }

        stage('Static Analysis (Bandit)') {
            steps {
                sh 'bandit -r . || true'
            }
        }

        stage('Dependency Scan (Safety)') {
            steps {
                sh 'safety check || true'
            }
        }

        stage('Image Scan (Trivy)') {
            steps {
                sh 'trivy image devsecopslab_app || true'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished ✅'
        }
    }
}
