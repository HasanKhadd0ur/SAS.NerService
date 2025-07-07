pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = 1
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/hasanKhadd0ur/sas.nerservice.git'
            }
        }

        stage('Set up Python venv') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest tests/
                '''
            }
        }

        stage('Run Flask App') {
            when {
                expression { return params.RUN_SERVER == true }
            }
            steps {
                bat '''
                call venv\\Scripts\\activate
                python run.py
                '''
            }
        }
    }

    parameters {
        booleanParam(name: 'RUN_SERVER', defaultValue: false, description: 'Run the Flask NER server')
    }
}
