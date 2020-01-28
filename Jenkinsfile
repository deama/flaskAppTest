pipeline 
{
	agent any 
	environment
	{
		ssh_ip = "deama85@playground"
		number = "${env.BUILD_NUMBER}"
	}

	stages 
	{
		stage("setup_git_repo")
		{
			steps 
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip} << EOF
					cd ~/flaskAppTest
					git pull
				'''
			}
		}
		stage("ssh_into_itself_and_build_project")
		{
			steps
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip} << EOF
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
					cd ~/
					export BUILD_NUMBER="${number}"
					sed "s/{{BUILD_NUMBER}}/$BUILD_NUMBER/g" ~/flaskAppTest/kube/app.yaml
					sed "s/{{BUILD_NUMBER}}/$BUILD_NUMBER/g" ~/flaskAppTest/kube/app.yaml | ~/google-cloud-sdk/bin/kubectl apply -f -
				'''
			}
		}
	}
}
