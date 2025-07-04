pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Undefinedboss/ade'
            }
        }

        stage('Build') {
            steps {
                sh 'chmod +x build.sh && ./build.sh'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def buildResult = sh(script: 'docker compose build --no-cache', returnStatus: true)
                    if (buildResult != 0) {
                        sh 'docker compose logs'
                        error "Docker compose build failed"
                    }
                }
            }
        }

        stage('Run Containers') {
            steps {
                script {
                    def upResult = sh(script: 'docker compose up -d', returnStatus: true)
                    if (upResult != 0) {
                        sh 'docker compose logs'
                        error "Docker compose failed to start containers"
                    }
                }
            }
        }

        stage('Debug Docker Status') {
            steps {
                sh '''
                    echo "Docker containers running:"
                    docker ps
                    echo "Docker logs for app container:"
                    docker logs $(docker ps -q --filter "name=newnew-world_of_games2-1") || true
                '''
            }
        }

        stage('Verify Flask Installation') {
            steps {
                sh '''
                    echo "Installed Python packages inside the container:"
                    docker exec $(docker ps -q --filter "name=newnew-world_of_games2-1") pip list || true
                '''
            }
        }

        stage('Wait for app') {
            steps {
                script {
                    def maxRetries = 20
                    def waitTime = 6
                    def success = false
                    def containerId = sh(script: "docker ps -q --filter 'name=newnew-world_of_games2-1'", returnSt
