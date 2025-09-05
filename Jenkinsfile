pipeline {
    agent any
    
     environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = "yourusername/world_of_games2"
        IMAGE_TAG = "latest"
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
                    def buildResult = sh(script: 'docker compose build -t world_of_games2:latest', returnStatus: true)
                    if (buildResult != 0) {
                        sh 'docker compose logs'
                        error "Docker compose build failed"
                    }
                }
            }
        }
        stage('Verify Image') {
            steps {
                script {
                    // Lightweight check: Python version and installed packages
                    sh '''
                        docker run --rm world_of_games2:latest python3 --version
                        docker run --rm world_of_games2:latest pip list
                    '''
                    
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker tag world_of_games2:latest $IMAGE_NAME:$IMAGE_TAG
                        docker push $IMAGE_NAME:$IMAGE_TAG
                    '''

        
                    }
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
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
                    for (int i = 0; i < maxRetries; i++) {
                        try {
                            sh 'curl -sf http://localhost:8888 > /dev/null'
                            success = true
                            break
                        } catch (Exception e) {
                            echo "App not ready yet, retrying in ${waitTime}s..."
                            sleep(waitTime)
                        }
                    }
                    if (!success) {
                        sh 'docker logs $(docker ps -q --filter "name=newnew-world_of_games2-1") || true'
                        error "App did not become ready in time"
                    }
                }
            }
        }
        stage('Test Container Environment') {
                steps {
                    sh '''
                        docker run --rm world_of_games2:latest python3 -m pip install --upgrade pip selenium
                    '''
            }
        }
    }

        stage('Test') {
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
            sh 'docker compose up -d'
        }
    }
}

