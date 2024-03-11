import json
import boto3
import logging
import datetime

dynamodb_translate_history = boto3.resource('dynamodb').Table('translate_history')

logger = logging.getLogger()
logger.setLevel("INFO")
    
translate = boto3.client('translate')

def lambda_handler(event, context):
    input_text = event['queryStringParameters']['input_text']
    logger.info(f'## EVENT  {input_text}')

    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode='ja',
        TargetLanguageCode='en',
    )
    output_text = response.get('TranslatedText')
    dynamodb_translate_history.put_item(
        Item = {
            "timestamp": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "input_text": input_text,
            "output_text": output_text
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text':output_text
        }),
        'isBase64Encoded': False,
        'headers': {}
    }
    