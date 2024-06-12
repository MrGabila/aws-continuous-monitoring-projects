## Description
This implementation deploys a Lambda Function, SNS Topic and EventBridge Rule to automatically tags newly created resources (ec2,s3,rds) and notify you of the change.
Tags include Owner, Environment=Production, Region (Modify in the function code)

## Prerequisites

1. Upload the Lambda function code (auto-tag-resources.zip) to S3 bucket. 
2. Ensure a Cloudtrail > Trails is created and **log Events=Management, Status=logging** 

## Steps

### 1. Create the CloudFormation stack

#### a. Using the AWS Management Console:
- Go to the AWS Management Console. Navigate to the CloudFormation service.

- Click on "Create stack". Specify the Template:

- Choose "Upload a template file". Upload the CloudFormation template file.

- Configure Stack Details: Enter a stack name.
- Provide the required parameters:
    - pSupportingFilesBucket: bucket-name.
    - pSupportingFilesPrefix: prefix/auto-tag-resources.zip
    - NotificationEmail: email@email.com

- Review and Create:
 **Note: Goto your email and confirm the subcription**

#### b. Using the AWS CLI
```bash
aws cloudformation create-stack --stack-name <my-stack-name> \
    --template-body file://cf-auto-tag-resources.yaml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameters ParameterKey=pSupportingFilesBucket,ParameterValue=<my-bucket> ParameterKey=pSupportingFilesPrefix,ParameterValue=<prefix/file.zip> ParameterKey=NotificationEmail,ParameterValue=<my-email> \
    --proflie <user>
```
 **Note: Goto your email and confirm the subcription**

### 2. Test the Resources by creating a resource (ec2,rds,s3) without the appropriate tags
Console Example
- On the console, navigate to EC2 > Images > AMI Catalog, search for any AMI in your region
- Then navigate to EC2, create an instance without assigning any tags

AWS CLI Example
```bash
aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region <my-aws-region> --query Parameters[0].[Value]

aws ec2 run-instances --image-id <my-ami-id> --count 1 --instance-type <my-instance-type>
```

### 3. Confirm the Tags were automatically assigned (Owner, Evironment, Region)

```bash
aws ec2 describe-tags --filters "Name=resource-id,Values=<your-instance-id>"
```
