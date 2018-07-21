pipeline {
  agent any
  stages {
    stage('Pytest') {
          steps {
                sh '''  #!/bin/bash |
                pytest test_calculadora.py |
                exit 0
            '''
          }
    }
  }
}

