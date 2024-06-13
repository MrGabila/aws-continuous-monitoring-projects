## Description
This implementation deploys a Lambda Function, SNS Topic and EventBridge Rule to notify via SLACK when a protected action has been carried out.(see parameters.json)

## Prerequisites

1. Upload the Lambda function code (index.zip) to S3 bucket.
2. Ensure a Cloudtrail > Trails is created with **log Events=Management, Status=logging** 
3. Modify values in the parameters.json

## Steps

### 1. Create SLACK WebHook URL
- Create a channel to receive alert within your workspace
- Go to the **App Directory** > Your Apps(top right) > 'Create App' > 'From Scratch'
- Give the app a Name and select workspace
- Next, select 'incoming webhooks', and Toggle ON
- Scrolldown, 'Add new webhook to workspace' > select your channel > 'Allow'
- Lastly, copy the webhool url to use as parameter value

### 2. Create the CloudFormation stack
Deploy on console OR use CLI

```bash
aws cloudformation create-stack --stack-name <my-stack-name> \
--template-body file://cf-alert-on-protected-actions.yaml \
--parameters file://parameters.json --capabilities CAPABILITY_NAMED_IAM
```

### 3. Ne need to confirm subscription because the message is sent by lambda over HTTP

### 4. Execute one of the protected actions Eg CreateUser

### 5. Confirm a Slack message is received identifying the protected action and the user who executed it
