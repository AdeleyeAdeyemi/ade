pipeline {
    agent any

    environment {
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AdeleyeAdeyemi/ade'
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
                    def buildResult = sh(script: 'docker build -t world_of_games2:latest .', returnStatus: true)
                    if (buildResult != 0) {
                        sh 'docker logs $(docker ps -q --filter "name=world_of_games2") || true'
                        error "Docker build failed"
                    }
                }
            }
        }

        stage('Verify Image') {
            steps {
                sh '''
                    docker run --rm world_of_games2:latest python3 --version
                    docker run --rm world_of_games2:latest pip list
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', 
                                                 usernameVariable: 'DOCKER_USER', 
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker tag world_of_games2:latest $DOCKER_USER/world_of_games2:$IMAGE_TAG
                        docker push $DOCKER_USER/world_of_games2:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Debug Docker Status') {
            steps {
                sh '''
                    echo "Docker containers running:"
                    docker ps
                    echo "Docker logs for app container:"
                    docker logs world_of_games2 || true
                '''
            }
        }

        stage('Verify Flask Installation') {
            steps {
                sh 'docker exec world_of_games2 pip list || true'
            }
        }

        stage('Wait for App') {
            steps {
                script {
                    def maxRetries = 20
                    def waitTime = 6
                    def success = false
                    for (int i = 0; i < maxRetries; i++) {
                        def result = sh(script: 'curl -sf http://localhost:8888 || echo "fail"', returnStdout: true).trim()
                        if (result != 'fail') {
                            success = true
                            break
                        }
                        echo "App not ready yet, retrying in ${waitTime}s..."
                        sleep(waitTime)
                    }
                    if (!success) {
                        sh 'docker logs world_of_games2 || true'
                        error "App did not become ready in time"
                    }
                }
            }
        }

        stage('Test Container Environment') {
            steps {
                sh 'docker run --rm world_of_games2:latest python3 -m pip install --upgrade pip selenium'
            }
        }

        stage('Test on Jenkins Agent') {
            steps {
                sh '''
                    python3 -m venv myenv &&
                    . myenv/bin/activate &&
                    pip install --upgrade pip selenium
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up containers..."
            sh 'cd "$WORKSPACE" && docker compose down -v || true'
        }
    }
}

