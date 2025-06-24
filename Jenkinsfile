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

        stage('Run') {
            steps {
                sh 'docker compose up -d'
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
                            sh 'curl -sf http://localhost:8777 > /dev/null'
                            success = true
                            break
                        } catch (Exception e) {
                            echo "App not ready yet, retrying in ${waitTime}s..."
                            sleep waitTime
                        }
                    }
                    if (!success) {
                        error "App did not become ready in time"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myenv &&
                    . myenv/bin/activate &&
                    pip install --upgrade pip selenium &&
                    python e2e.py
                '''
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }
    }
}

