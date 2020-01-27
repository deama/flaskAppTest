pipeline 
{
	agent any 
	environment
	{
		install_dir = "/opt/flask-app"
		ssh_ip = "jenkins-docker"
		ssh_ip_self = "playground"
		number = "${env.BUILD_NUMBER}"
	}

	stages 
	{
		stage("setup_git_repo")
		{
			steps 
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip_self} << EOF
					cd ~/flaskMicroServer
					git pull
				'''
			}
		}
		stage("ssh_into_itself_and_build_project")
		{
			steps
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip_self} << EOF
					cd ~/flaskMicroServer
					git checkout updateBranch
					export BUILD_NUMBER="${number}"
					docker-compose build
					docker-compose push
				'''
			}
		}
		stage("update_service_files")
		{
			steps
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip} << EOF
					docker service update --replicas 1 --image 172.31.47.162:5000/flask-prize:build-${number} proj_flask-prize
					docker service update --replicas 1 --image 172.31.47.162:5000/flask-host:build-${number} proj_flask-host
					docker service update --replicas 1 --image 172.31.47.162:5000/flask-number:build-${number} proj_flask-number
					docker service update --replicas 1 --image 172.31.47.162:5000/flask-letter:build-${number} proj_flask-letter
					docker service update --replicas 1 --image 172.31.47.162:5000/flask-sequence:build-${number} proj_flask-sequence
				'''
			}
		}
	}
}
