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
					cd /home/deama85
					/home/deama85/google-cloud-sdk/bin/kubectl apply -f app.yaml
				'''
			}
		}
	}
}
