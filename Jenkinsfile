pipeline 
{
	agent any 
	environment
	{
		ssh_ip = "deama85@playground"
		ssh_ip_self = "jenkins-docker"
		number = "${env.BUILD_NUMBER}"
	}

	stages 
	{
		stage("setup_git_repo")
		{
			steps 
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip_self} << EOF
					cd ~/flaskAppTest
					git pull
				'''
			}
		}
		stage("ssh_into_itself_and_build_project")
		{
			steps
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip_self} << EOF
					cd ~/flaskAppTest
					git checkout master
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
					export BUILD_NUMBER="${number}"
					echo ${BUILD_NUMBER}
					/home/deama85/google-cloud-sdk/bin/kubectl apply -f /home/deama85/flaskAppTest/kube/app.yaml
				'''
			}
		}
	}
}
