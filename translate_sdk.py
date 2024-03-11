import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel("INFO")
    
translate = boto3.client('translate')

def lambda_handler(event, context):
    input_text = 'おはよう'
    logger.info(f'## EVENT  {input_text}')

    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode='ja',
        TargetLanguageCode='en',
    )
    output_text = response.get('TranslatedText')
    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text':output_text
        })
    }