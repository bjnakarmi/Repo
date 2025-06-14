pipeline{
	agent any

	stages{
		stage('Checkout Code'){
			steps{
				git 'https://github.com/bjnakarmi/Repo.git'
			}
		}
		stage('Run Tests'){
			steps{
				bat 'pytest tests/ --html=report.html --self-contained-html'
			}
		}
		stage('Publish Report'){
			steps{
				publishHTML([
					reportDir: '.',
					reportFiles: 'report.html',
					reportName: 'Test Report',
					keepAll: True
					])
			}
		}
	}
}
		