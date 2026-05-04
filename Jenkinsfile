pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
            script {
                echo "Текущая ветка: ${env.BRANCH_NAME}"
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-app:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    docker.image("my-app:${env.BUILD_NUMBER}").inside {
                        sh 'python test_app.py'
                    }
                }
            }
        }
        
        stage('Deploy (CD)') {
            when {
                branch 'master'
            }
            steps {
                script {
                    sh 'docker stop my-app || true'
                    sh 'docker rm my-app || true'
                    sh "docker run -d --name my-app -p 5005:5000 my-app:${env.BUILD_NUMBER}"
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline успешно выполнен!'
        }
        failure {
            echo 'Pipeline упал!'
        }
    }
}