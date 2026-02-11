# Chicken-Disease-Classification

# End to end ML Project Template

# How to Create CICD for ML Project

1. Create workflow main.yaml file
2. create AWS IAM user with AmazonEC2FullAccess access and AmazonEC2ContainerRegistryFullAccess full access
3. create AWS ECR repository
4. Create EC2 instance and configure it

## Configure EC2 Instance for CICD

* sudo apt-get update -y
* sudo apt-get upgrade -y

### Install Docker
* curl -fsSL https://get.docker.com -o get-docker.sh
* sudo sh get-docker.sh
* sudo usermod -aG docker ubuntu
* newgrp docker
* researt the ec2 instance

### Add runner
github repo--> settings --> Actions--> Runners --> Create new one for Linux
run the codes inside the EC2
Enter the name of runner:  self-hosted
go others with defalut values

5. Add Scerets to Github
github repo--> settings --> Secrets and variables --> Actions
