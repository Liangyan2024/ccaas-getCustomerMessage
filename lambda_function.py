import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ccaas-customerMessage')


def lambda_handler(event, context):

   print("Received event:", event)

   attrs = event['Details']['ContactData']['Attributes']
   print ("attributes", attrs)
   language = attrs.get('language', 'en').lower()
   message_id = attrs.get('messageID', '1')

   
   resp = table.get_item(Key = {'MessageID': message_id})
   item = resp.get('Item', {})

   if language == 'en':
      message_text = item.get('EnglishText', 'no English message found')
   else:
      message_text = item.get('FrenchText', 'no french message found')   

   print (message_text)

   return {
      'message_text': message_text
   }