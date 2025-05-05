import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ccaas-customerMessage')


def lambda_handler(event, context):

   print("Received event:", event)

   attrs = event['Details']['ContactData']['Attributes']
   language = attrs.get('language', 'en').lower()
   message_id = attrs.get('messageID', '1')


   resp = table.get_item(key = {'messageID': message_id})
   item = resp.get('Item', {})

   if language == 'en':
      message_text = item.get('EnglishText', 'no English message found')
   else:
      message_text = item.get('FrenchText', 'no french message found')   

      

   return {
      'message_test': message_text
   }

