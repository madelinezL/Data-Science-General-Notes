https://courses.datacumulus.com/downloads/certified-cloud-practitioner-zb2/
aws.amazon.com/faqs/


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
  - On premises (local)
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

### Compute in the Cloud - EC2
* VM/EC2 Instance
* Elastic Load Balancing: it does not add/remove instances, have different types from AWS
* Auto Scaling group: will add/remove more instances, inform ELB when instances added/removed to distribute better, only 1 type <br/>
* SNS: Simple Notification Service - Microservices, the receiving component is not active, waiting for the push service
* SQS: Simple Queue Service - Monolithic application, the receiving component is active, poll service, hold the message
* Edge Location: piece of infrastructure Amazon uses to cache copies of content for faster delivery to users at any location
  - Four services based on the edge location: R53, CloudFront, AWS Shield, Web Application Firewall
* CDN: CloudFront, a global content delivery service, we have 400+ edge locations. We do not upload files in cloudfront, instead, we ask them where to fetch and deliver.
* Global infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/
* Three ways to intercat with AWS services:
  - CLI: command line interface
  - API: programmatic access to cloud services
  - Web UI: AWS management console
* VPC is a regional component, we can have VPC in region but not edge location.
* We have 31 regions globally, each region have 200+ services (S3, SQS, etc.)
* DDos: Distributor Denial of Service - AWS Shield

### Networking

### Practice Questions
1. CloudFront - edge locations - low latency


