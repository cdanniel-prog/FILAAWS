import boto3

# Create SQS client
sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/668768958219/danniel'
for i in range(200):
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    messages = response['Messages']
    for message in messages: 
        receipt_handle = message['ReceiptHandle']

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        
        print('Received and deleted message: %s' % message)
print(f'menssagens deletadas: {i}')