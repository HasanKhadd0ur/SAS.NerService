pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = 1
    }

    parameters {
        booleanParam(name: 'RUN_SERVER', defaultValue: false, description: 'Run the Flask NER server')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hasanKhadd0ur/sas.nerservice.git'
            }
        }

        stage('Set up Python venv') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                if exist requirements.txt (
                    python -m pip install -r requirements.txt
                ) else (
                    echo No requirements.txt found!
                )
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                if exist src\\tests (
                    pytest src\\tests
                ) else (
                    echo No test directory found at src\\tests
                    exit /b 1
                )
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
                python src\\app\\run.py
                '''
            }
        }
    }
}
