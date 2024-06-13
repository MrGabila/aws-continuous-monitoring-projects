import boto3
import json
import os
import urllib3

def lambda_handler(event, context):
    print('Event:', json.dumps(event))
    
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']
    
    user_name = ''
    try:
        # IAM user
        user_name = event['detail']['userIdentity']['userName']
    except:
        # assumed IAM role
        user_name = event['detail']['userIdentity']['arn']
        # parse the user name from the arn
        user_name = user_name.rsplit('/', 1)[-1]
    
    event_name = event['detail']['eventName']
    event_time = event['detail']['eventTime']
    source_ip = event['detail']['sourceIPAddress']
    aws_region = event['detail']['awsRegion']
    
    sns_client = boto3.client('sns')
    
    message = f'Alert: User {user_name}[{source_ip}] made API call "{event_name}" at {event_time} in the {aws_region} region'
    print(message)
    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message
    )
    
    # Send message to Slack
    slack_message = {'text': message}
    http = urllib3.PoolManager()
    response = http.request(
        'POST',
        slack_webhook_url,
        body=json.dumps(slack_message),
        headers={'Content-Type': 'application/json'},
        retries=False
    )
    print('Slack response status:', response.status)
    
    return {
        'statusCode': 200,
        'body': message
    }
