pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Клонирование репозитория'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Сборка Docker образа'
                script {
                    docker.build("my-app:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Запуск тестов'
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
                echo 'Деплой (только ветка master)'
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