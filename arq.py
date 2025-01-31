import boto3

# Create SQS client
sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/668768958219/danniel'
for _ in range(200): 
    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=0,
        
        MessageBody=(
            'Oi, tudo bem? '
        )
    )
 