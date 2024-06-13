## Description
This implementation deploys a Lambda Function, SNS Topic and EventBridge Rule to notify via SLACK when a protected action has been carried out.(see parameters.json)

## Prerequisites

1. Upload the Lambda function code (index.zip) to S3 bucket. 
2. Ensure a Cloudtrail > Trails is created with **log Events=Management, Status=logging** 
3. Create Slack Webhook URL for your channel

## Steps

### 1. Create the CloudFormation stack

Example parameters.json:
```JSON
[
  {
    "ParameterKey": "pEvents",
    "ParameterValue": "CreateUser, CreateAccessKey, CreateRoute, AuthorizeSecurityGroupEgress, AuthorizeSecurityGroupIngress, CreateNetworkAclEntry, DeleteNetworkAcl, AttachRolePolicy, CreateVirtualMFADevice, DeactivateMFADevice, DeleteBucketPolicy, PutBucketPolicy, StopLogging"
  },
  {
    "ParameterKey": "pSlackWebhookUrl",
    "ParameterValue": "paste-link-from-slack-webhookURL"
  }
]
```

Usage
```bash
aws cloudformation create-stack --stack-name <my-stack-name> \
--template-body file://cf-alert-on-protected-actions.yaml \
--parameters file://parameters.json --capabilities CAPABILITY_NAMED_IAM
```

### 2. Ne need to confirm subscription because the message is sent by lambda over HTTP

### 3. Execute one of the protected actions Eg CreateUser

### 4. Confirm a Slack message is received identifying the protected action and the user who executed it
