# airflow-scheduler for databases e-commerce benchmark

# Contents
* [installation](#install)
* [settings-GCE](#settings-GCE)
* [Run the app](#run)


Prerequisites
------------------

You just need ansible, terraform and terraform-inventory on your machine and an account gcp.

Or via brew on mac : 

```bash
brew updates 
brew install terraform
```

Install ansible :
```
pip install ansible
```
terraform inventory dynamique for ansible : 
```
brew install terraform-inventory
```
See more about [here](https://github.com/adammck/terraform-inventory)

# settings-GCE:

Create google project and connect it to terraform
------------------
1. Follow : [here](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
2. Download the json creds to connect your teraform to your gcp account, if you have problem see [this](https://github.com/caminale/benchmark-ecommerce-scala/blob/master/docs/gcp-configs.md)
3. Download the private ssh key and connect into your terraform to allow connection with the new instances,
   personnaly gcloud create me ssh keys when I used gcloud compute to connect to a machine.

# Pop up your schedule-machine:

run the app
------------------

Check **terraform.tfvars.example** file inside `terraform` folder to see what variables you need to define before you can use terraform to create the machine. If you have some problem go to see this : [here](https://github.com/caminale/benchmark-ecommerce-scala/blob/master/docs/gcp-configs.md)

You can run the following command in `terraform` to make your variables definitions available to terraform:
```bash
$ mv terraform.tfvars.example terraform.tfvars # variables defined in terraform.tfvars will be automatically picked up by terraform during the run
```
### Terraform reminders :
* To download the plugins : 
    ```bash
    cd terraform
    terraform init
    ```
* To run the code : 

    ```bash
    cd terraform
    terraform apply
    ```
* To show what we want to build (show tfstate)

    ```bash 
    cd terraform
    terraform plan
    ```







