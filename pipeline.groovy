pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                bat 'python -m venv venv'
                bat 'call venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Maths Test') {
            steps {
                bat 'call venv\\Scripts\\activate && pytest test/test_maths.py'
            }
        }

        // stage('Run Signup Test') {
        //     steps {
        //         bat 'call venv\\Scripts\\activate && pytest tests/test_signup.py'
        //     }
        // }

        // stage('Run Checkout Test') {
        //     steps {
        // //         bat 'call venv\\Scripts\\activate && pytest tests/test_checkout.py'
        //     }
        // }
    }
}
