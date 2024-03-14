import json
from flask import Flask, request
from flask import jsonify
from flask_restful import Api,Resource
import requests
app = Flask(__name__)

#Channel access token 
Channel_Access_Token = 'F+O5RanwyCaJ1LK7I7zPtbRG373V6hHyRWDCsm/owEYpvKhR+nLTghMLlrNC1GtducIWqYMDUs9v0bxDGMi3onJr5BNM+hjjP3x6Bs9K41E0XY0/clvhKZ9lU8dKXuUt4too2HLKq/PBQ578pjbXxwdB04t89/1O/w1cDnyilFU='
#Bot basic ID
basic_id = '@604xmsex'
#Channel secret
Channel_secret = 'db330bc6356ab19f3c3bef7b115bbc3a'

@app.route('/webhook',methods=['GET','POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        Reply_Token = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        print('reply = ',Reply_Token)
        print('json = ',request.json)
        
        if('hi' in message):
          resMessage = 'ว่ายังไง'
          ReplyMessage(Reply_Token,resMessage,Channel_Access_Token)
        elif('ข้อความ' in message):
          resMessage = 'นี้คือข้อความ'
          ReplyMessage(Reply_Token,resMessage,Channel_Access_Token)
        elif('qr' in message):
          quickReply(Reply_Token,Channel_Access_Token)
        elif('ปุ่ม' in message):
          buttonShow(Reply_Token,Channel_Access_Token)
        elif('หน้า' in message):
          CarouselReply(Reply_Token,Channel_Access_Token);
        else :
          resMessage = 'พิมพ์ qr เพื่อดูคำสั่งทั้งหมด'
          ReplyMessage(Reply_Token,resMessage,Channel_Access_Token)
        return request.json,200
    elif request.method == 'GET':
        return 'This get'
  
#Fucntion ตอบกลับแบบ Text
def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200
  
#Fucntion ตอบกลับแบบ Quick Reply
def quickReply(Reply_token, Line_Acees_Token):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Line_Acees_Token)
  print(Authorization)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization':Authorization
  }

  data = {
      "replyToken":Reply_token,
       "messages":[{
        "type": "text", 
        "text": "คำสั่งทั้งหมดที่มี",
        "quickReply": { 
          "items": [
            {
              "type": "action", 
              "action": {
                "type": "message",
                "label": "ปุ่ม",
                "text": "ปุ่ม"
              }
            },
            {
              "type": "action",
              "action": {
                "type": "message",
                "label": "หน้า",
                "text": "หน้า"
              }
            },
            {
              "type": "action",
              "action": {
                "type": "message",
                "label": "ข้อความ",
                "text": "ข้อความ"
              }
            },
            
            {
              "type": "action",
              "action": {
                "type": "location",
                "label": "Send location"
              }
            }
          ]
        }
      }]
  }
  
  print('sent quick reply')
  data = json.dumps(data) ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data) 
  return 200

#Fucntion ตอบกลับแบบ Button
def buttonShow(Reply_token, Line_Acees_Token):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Line_Acees_Token)
  print(Authorization)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization':Authorization
  }

  data = {
      "replyToken":Reply_token,
      "messages":[{
      "type": "template",
      "altText": "This is a buttons template",
      "template": {
        "type": "buttons",
        "imageAspectRatio": "rectangle",
        "imageSize": "cover",
        "imageBackgroundColor": "#FFFFFF",
        "title": "Menu",
        "text": "Please select",
        "defaultAction": {
          "type": "uri",
          "label": "View detail",
          "uri": "https://www.google.co.th/"
        },
        "actions": [
          {
            "type": "postback",
            "label": "Buy",
            "data": "action=buy&itemid=123"
          },
          {
            "type": "postback",
            "label": "Add to cart",
            "data": "action=add&itemid=123"
          },
          {
            "type": "uri",
            "label": "View detail",
            "uri": "https://www.google.co.th/"
         } 
        ]
      }
    }
  ]}
  data = json.dumps(data) ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data) 
  return 200

#Fucntion ตอบกลับแบบCarousel
def CarouselReply(Reply_token, Line_Acees_Token): 
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Line_Acees_Token)
  print(Authorization)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization':Authorization
  }

  data = {
      "replyToken":Reply_token,
      "messages":[{
        "type": "template",
        "altText": "this is a carousel template",
        "template": {
          "type": "carousel",
          "columns": [
            {
              "thumbnailImageUrl": "https://example.com/bot/images/item1.jpg",
              "imageBackgroundColor": "#FFFFFF",
              "title": "this is menu",
              "text": "description",
              "defaultAction": {
                "type": "uri",
                "label": "View detail",
                "uri": "https://www.google.co.th/"
              },
              "actions": [
                {
                  "type": "postback",
                  "label": "Buy",
                  "data": "action=buy&itemid=111"
                },
                {
                  "type": "postback",
                  "label": "Add to cart",
                  "data": "action=add&itemid=111"
                },
                {
                  "type": "uri",
                  "label": "View detail",
                  "uri": "https://www.google.co.th/"
                }
              ]
            },
            {
              "thumbnailImageUrl": "https://example.com/bot/images/item2.jpg",
              "imageBackgroundColor": "#000000",
              "title": "this is menu",
              "text": "description",
              "defaultAction": {
                "type": "uri",
                "label": "View detail",
                "uri": "https://www.google.co.th/"
              },
              "actions": [
                {
                  "type": "postback",
                  "label": "Buy",
                  "data": "action=buy&itemid=222"
                },
                {
                  "type": "postback",
                  "label": "Add to cart",
                  "data": "action=add&itemid=222"
                },
                {
                  "type": "uri",
                  "label": "View detail",
                  "uri": "https://www.google.co.th/"
                }
              ]
            }
          ],
          "imageAspectRatio": "rectangle",
          "imageSize": "cover"
        }
      }
      
    ]
  }
  data = json.dumps(data) ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data) 
  return 200



if  __name__ == "__main__":
    app.run(debug=True)