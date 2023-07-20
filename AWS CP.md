https://courses.datacumulus.com/downloads/certified-cloud-practitioner-zb2/

* Important Slides
  - Shared responsibility model diagram

* IAM: Identitiy and Access Management
  - Global service, root acount
  - note: pw v2
  - MFA: Multi Factor Authentication --> password you know + security device you own
    - MFA devices options

* AWS CLI: AWS Command Line Interface
  - Enables you to interact with AWS services using commands in your command-line shell
  - Downloaded the AWS CLI v2

* AWS SDK: AWS Software Development Kit
  - Enables you to access and manage AWS services programmatically

* AWS CouldShell

* EC2 - Elastic Compute Cloud
  - SSH: Secure Shell - SSH provides a secure way to access and manage instances (virtual servers) within the AWS infrastructure.
  - EC2 Spot Instances 90% cheaper
    - can get a discount of up to 90% compared to On-demand
    - most cost-efficient instances in AWS
    - useful for workloads that are resilient to failure
    - not suitable for critical jobs or databases
  - EC2 Dedicated Hosts
    - most expensive option
  - EC2 Dedicated Instances

* EC2 Instance Storage

 
request exam recommendations - 30 mins extra 

*7/20/2023* 
## Bootcamp
### Introduction
* Three cloud computing deployment models
  - Cloud
  - On premises
  - Hybrid
* Six Benefits of cloud computing
  - Variable expenses
  - Cost optimization
  - Capacity
  - Economies of scale
  - Speed and agility
  - Global in minutes
* No upfront expenses (similar as CapExs), have variable expenses (similar as OpExs)
* On-premises deployment (Private cloud deployment), on-premise --> local
* High Latency --> longer response time (download, wait longer)
* High available: 1 region
* Disastor Recovery: need several regions

### EC2
* VM/EC2 Instance
* Elastic Load Balancing: it does not add/remove instances, have different types from AWS
* Auto Scaling group: will add/remove more instances, inform ELB when instances added/removed to distribute better, only 1 type
