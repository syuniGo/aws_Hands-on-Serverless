import json
import os
import logging
logger = logging.getLogger()
logger.setLevel("INFO")
    
def lambda_handler(event, context):
    print('test1')
    logger.info('## EVENT')
    logger.info(event)
    print('test2')
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
