pipeline {
    agent any

    environment {
        APP_CONTAINER_NAME = 'world_of_games_app'  // Set your actual container name here
    }

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
                        sh "docker compose logs ${env.APP_CONTAINER_NAME}"
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
                        sh "docker compose logs ${env.APP_CONTAINER_NAME}"
                        error "Docker compose failed to start containers"
                    }
                }
            }
        }

        stage('Debug Docker Status') {
            steps {
                sh """
                    echo "Docker containers running:"
                    docker ps
                    echo "Docker logs for app container:"
                    docker logs \$(docker ps -q --filter "name=${APP_CONTAINER_NAME}") || true
                """
            }
        }

        stage('Verify Flask Installation') {
            steps {
                sh """
                    echo "Installed Python packages inside the container:"
                    docker exec \$(docker ps -q --filter "name=${APP_CONTAINER_NAME}") pip list || true
                """
            }
        }

        stage('Wait for app') {
            steps {
                script {
                    def maxRetries = 20
                    def waitTime = 6
                    def success = false
                    def containerId = sh(script: "docker ps -q --filter 'name=${APP_CONTAINER_NAME}'", returnStdout: true).trim()

                    for (int i = 0; i < maxRetries; i++) {
                        def status = sh(script: "docker exec ${containerId} curl -sf http://localhost:8888 > /dev/null", returnStatus: true)
                        if (status == 0) {
                            success = true
                            break
                        }
                        echo "App not ready yet, retrying in ${waitTime}s..."
                        sleep(waitTime)
                    }
                    if (!success) {
                        sh "docker logs ${containerId} || true"
                        error "App did not become ready in time"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myenv && \
                    source myenv/bin/activate && \
                    pip install --upgrade pip selenium && \
                    python e2e.py
                '''
            }
        }
    }

    post {
        always {
            sh 'docker compose up -d'
        }
    }
}
