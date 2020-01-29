import base64
import errno
import json
import os
import sys
import tempfile
import requests
import urllib.request
from argparse import ArgumentParser
from requests import Request, Session
from PIL import Image
from io import BytesIO

from flask import Flask, request, abort
from py_translator import Translator

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.http_client import (
    HttpClient, RequestsHttpClient
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, JoinEvent, LeaveEvent, SourceUser, SourceGroup, SourceRoom,
    ConfirmTemplate, MessageAction, TemplateSendMessage,Action, PostbackEvent, MemberIds, Profile, ImageMessage,
    VideoMessage, AudioMessage, FileMessage, QuickReply, QuickReplyButton, PostbackAction, MemberJoinedEvent, MemberLeftEvent
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('x9I42/HXzVLQQ3HLWVmxCf7z5jLAtEf44gpdKmlnGCkzXw9+y+LuKjA8WIklR29p4cXtdgCmV1CCD3woIswyRrOkphjpeubSVLIgWlBtMnI4mcAWYjkHuV48A4C9q3JIhV8GauV4tRmfKDmmZwwSoQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3d7644d429a491ed618d3b2b2fec3b2d')

@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ Here's all the messages will be handled and processed by the program """
    msg = (event.message.text).lower()
    if msg == 'hello':
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text="Hello")])
# flag any messages starting with a period for known nukebot commands
    elif msg.startswith('.'):
       line_bot_api.multicast(FifthID, #5thElement
                              TextSendMessage(text='A PROHIBITED COMMAND WAS TYPED!'))
       line_bot_api.push_message(group_id1,TextSendMessage(text='A PROHIBITED COMMAND WAS TYPED!'))#R4 Room
       line_bot_api.reply_message(
           event.reply_token,
            [TextSendMessage(text="WARNING: PROHIBITED COMMAND!")])

# implement translation feature
    elif msg.endswith('> fr') or msg.endswith('>fr') or msg.endswith('>fr ') or msg.endswith('> fr '):
       s_fr_parsed = msg[:-4]
       print(s_fr_parsed)
       s_fr_parsed_trans = Translator().translate(text=s_fr_parsed, dest='fr').text
       print(s_fr_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_fr_parsed_trans)])
    elif msg.endswith('> en') or msg.endswith('>en') or msg.endswith('>en ') or msg.endswith('> en '):
       s_en_parsed = msg[:-4]
       print(s_en_parsed)
       s_en_parsed_trans = Translator().translate(text=s_en_parsed, dest='en').text
       print(s_en_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_en_parsed_trans)])
    elif msg.endswith('> sp') or msg.endswith('>sp') or msg.endswith('>sp ') or msg.endswith('> sp '):
       s_sp_parsed = msg[:-4]
       print(s_sp_parsed)
       s_sp_parsed_trans = Translator().translate(text=s_sp_parsed, dest='es').text
       print(s_sp_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_sp_parsed_trans)])
    elif msg.endswith('> vi') or msg.endswith('>vi') or msg.endswith('>vi ') or msg.endswith('> vi '):
       s_vi_parsed = msg[:-4]
       print(s_vi_parsed)
       s_vi_parsed_trans = Translator().translate(text=s_vi_parsed, dest='vi').text
       print(s_vi_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_vi_parsed_trans)])
    elif msg.endswith('> cn') or msg.endswith('>cn') or msg.endswith('>cn ') or msg.endswith('> cn '):
       s_cn_parsed = msg[:-4]
       print(s_cn_parsed)
       s_cn_parsed_trans = Translator().translate(text=s_cn_parsed, dest='zh-cn').text
       print(s_cn_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_cn_parsed_trans)])
    elif msg.endswith('> th') or msg.endswith('>th') or msg.endswith('>th ') or msg.endswith('> th '):
       s_th_parsed = msg[:-4]
       print(s_th_parsed)
       s_th_parsed_trans = Translator().translate(text=s_th_parsed, dest='th').text
       print(s_th_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_th_parsed_trans)])
    elif msg.endswith('> ru') or msg.endswith('>ru') or msg.endswith('>ru ') or msg.endswith('> ru '):
       s_ru_parsed = msg[:-4]
       print(s_ru_parsed)
       s_ru_parsed_trans = Translator().translate(text=s_ru_parsed, dest='ru').text
       print(s_ru_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_ru_parsed_trans)])
    elif msg.endswith('> it') or msg.endswith('>it') or msg.endswith('>it ') or msg.endswith('> it '):
       s_it_parsed = msg[:-4]
       print(s_it_parsed)
       s_it_parsed_trans = Translator().translate(text=s_it_parsed, dest='it').text
       print(s_it_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_it_parsed_trans)])
    elif msg.endswith('> nl') or msg.endswith('>nl') or msg.endswith('>nl ') or msg.endswith('> nl '):
       s_nl_parsed = msg[:-4]
       print(s_nl_parsed)
       s_nl_parsed_trans = Translator().translate(text=s_nl_parsed, dest='nl').text
       print(s_nl_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_nl_parsed_trans)])

# profile API from LINE
    elif msg == 'profile' or msg == 'profile ':
        if isinstance(event.source, SourceGroup):
          profile = line_bot_api.get_group_member_profile(event.source.group_id, event.source.user_id)
          line_bot_api.reply_message(
            event.reply_token,
             [TextSendMessage(text=profile.display_name),
              TextSendMessage(text='User id: ' + profile.user_id),
              TextSendMessage(text='Group id: ' + event.source.group_id),
             ])
        else:
          profile = line_bot_api.get_profile(event.source.user_id)
          line_bot_api.reply_message(
            event.reply_token,
             [TextSendMessage(text=profile.display_name),
              TextSendMessage(text='User id: ' + profile.user_id),
             ])

# implement time zone feature
    elif msg == 'time':
       time_api_address = 'http://worldtimeapi.org/api/timezone/Asia/Hong_Kong'
       time_api_address1 = 'http://worldtimeapi.org/api/timezone/Asia/Bangkok'
       time_api_address2 = 'http://worldtimeapi.org/api/timezone/Europe/London'
       time_api_address3 = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
       time_api_address3a = 'http://worldtimeapi.org/api/timezone/Europe/Paris'
       time_api_address4 = 'http://worldtimeapi.org/api/timezone/Europe/Rome'
       time_api_address5 = 'http://worldtimeapi.org/api/timezone/Australia/Sydney'
       time_api_address6 = 'http://worldtimeapi.org/api/timezone/America/Toronto'
       time_api_address7 = 'http://worldtimeapi.org/api/timezone/America/Vancouver'
       time_api_address8 = 'http://worldtimeapi.org/api/timezone/America/Los_Angeles'
       time_api_address9 = 'http://worldtimeapi.org/api/timezone/America/New_York'
       print(time_api_address)
       json_timedata = requests.get(time_api_address).json()
       json_timedata1 = requests.get(time_api_address1).json()
       json_timedata2 = requests.get(time_api_address2).json()
       json_timedata3 = requests.get(time_api_address3).json()
       json_timedata3a = requests.get(time_api_address3a).json()
       json_timedata4 = requests.get(time_api_address4).json()
       json_timedata5 = requests.get(time_api_address5).json()
       json_timedata6 = requests.get(time_api_address6).json()
       json_timedata7 = requests.get(time_api_address7).json()
       json_timedata8 = requests.get(time_api_address8).json()
       json_timedata9 = requests.get(time_api_address9).json()
       print(json_timedata)
       timezone_json_data = json_timedata['timezone']
       timezone_json_data1 = json_timedata1['timezone']
       timezone_json_data2 = json_timedata2['timezone']
       timezone_json_data3 = json_timedata3['timezone']
       timezone_json_data3a = json_timedata3a['timezone']
       timezone_json_data4 = json_timedata4['timezone']
       timezone_json_data5 = json_timedata5['timezone']
       timezone_json_data6 = json_timedata6['timezone']
       timezone_json_data7 = json_timedata7['timezone']
       timezone_json_data8 = json_timedata8['timezone']
       timezone_json_data9 = json_timedata9['timezone']
       datetime_json_data = json_timedata['datetime']
       datetime_json_data1 = json_timedata1['datetime']
       datetime_json_data2 = json_timedata2['datetime']
       datetime_json_data3 = json_timedata3['datetime']
       datetime_json_data3a = json_timedata3a['datetime']
       datetime_json_data4 = json_timedata4['datetime']
       datetime_json_data5 = json_timedata5['datetime']
       datetime_json_data6 = json_timedata6['datetime']
       datetime_json_data7 = json_timedata7['datetime']
       datetime_json_data8 = json_timedata8['datetime']
       datetime_json_data9 = json_timedata9['datetime']
       datetime_short = datetime_json_data[:19]
       datetime_short1 = datetime_json_data1[:19]
       datetime_short2 = datetime_json_data2[:19]
       datetime_short3 = datetime_json_data3[:19]
       datetime_short3a = datetime_json_data3a[:19]
       datetime_short4 = datetime_json_data4[:19]
       datetime_short5 = datetime_json_data5[:19]
       datetime_short6 = datetime_json_data6[:19]
       datetime_short7 = datetime_json_data7[:19]
       datetime_short8 = datetime_json_data8[:19]
       datetime_short9 = datetime_json_data9[:19]
       print(timezone_json_data)
       print(datetime_json_data)
       print(datetime_short)
       line_bot_api.reply_message(
           event.reply_token,
            TextSendMessage(text=timezone_json_data + '\n' + datetime_short + '\n\n' +
                           timezone_json_data1 + '\n' + datetime_short1 + '\n\n' +
                           timezone_json_data2 + '\n' + datetime_short2 + '\n\n' +
                           timezone_json_data3 + '\n' + datetime_short3 + '\n\n' +
                           timezone_json_data3a + '\n' + datetime_short3a + '\n\n' +
                           timezone_json_data4 + '\n' + datetime_short4 + '\n\n' +
                           timezone_json_data5 + '\n' + datetime_short5 + '\n\n' +
                           timezone_json_data6 + '\n' + datetime_short6 + '\n\n' +
                           timezone_json_data7 + '\n' + datetime_short7 + '\n\n' +
                           timezone_json_data8 + '\n' + datetime_short8 + '\n\n' +
                           timezone_json_data9 + '\n' + datetime_short9))

# implement currency conversion feature
    elif 'currency convert' in msg:
        print('CURRENCY')
        currency_api_key = currency_token
        currency_api_address = 'https://free.currconv.com/api/v7/convert?q='
        currency_pair = msg[17:]
        print(currency_pair)
        currency_pair_notrailspace = currency_pair.rstrip()
        print(currency_pair_notrailspace)
        currency_address = currency_api_address + currency_pair_notrailspace
        currency_address_full = currency_address.replace(' ', '_', 1) + '&compact=ultra&apiKey=' + currency_api_key
        print(currency_address_full)
        try:
            json_currency_pair = requests.get(currency_address_full).json()
            print(json_currency_pair)
            json_rate = str(json_currency_pair)
            print(json_rate)
            line_bot_api.reply_message(
                event.reply_token,
                 TextSendMessage(text=json_rate))
        except:
            print('CURRENCY PAIR NOT FOUND')
            line_bot_api.reply_message(
              event.reply_token,
               TextSendMessage(text='currency pair not found'))
    elif 'currency list' in msg:        
        print('CURRENCY LIST')
        currency_api_key = currency_token
        currency_api_list_address = 'https://free.currconv.com/api/v7/currencies?&compact=ultra&apiKey=' + currency_api_key
        print(currency_api_list_address)
        json_currency_api_list_address = requests.get(currency_api_list_address).json()
        json_list = []
        for key1, key2 in json_currency_api_list_address.items():
          print("\nSymbol:", key1)
          for key in sorted(key2):
            print(key + ':', key2[key])
            json_list.append(key + ':')
            json_list.append(key2[key])
        del json_list[1::2]
        print(*json_list, sep = "\n")
        symbol_list = str(json_list)
        line_bot_api.reply_message(
          event.reply_token,
           TextSendMessage(text='List of all currency symbols: \n\n' + symbol_list))

# implement tastedive similar taste API
    elif 'tastedive' in msg:
        print('TASTEDIVE')
        tastedive_api_key = tastedive_token
        tastedive_api_address = 'https://tastedive.com/api/similar?q='
        query = msg[10:]
        print(query)
        tastedive_address = tastedive_api_address + query
        tastedive_address_full = tastedive_address.replace(' ', '+') + '&k=' + tastedive_api_key + '&limit=5&info=1'
        print (tastedive_address_full)
        try:
           json_tastedive_data = requests.get(tastedive_address_full).json()
           print(json_tastedive_data)
           wTeaser_json_data_source = json_tastedive_data['Similar']['Info'][0]['wTeaser']
           wTeaser_json_data_source_short = wTeaser_json_data_source.partition(".")[0]
           name_json_data = json_tastedive_data['Similar']['Results'][0]['Name']
           type_json_data = json_tastedive_data['Similar']['Results'][0]['Type']
           wTeaser_json_data = json_tastedive_data['Similar']['Results'][0]['wTeaser']
           wTeaser_json_data_short = wTeaser_json_data.partition(".")[0]
           name_json_data1 = json_tastedive_data['Similar']['Results'][1]['Name']
           type_json_data1 = json_tastedive_data['Similar']['Results'][1]['Type']
           wTeaser_json_data1 = json_tastedive_data['Similar']['Results'][1]['wTeaser']
           wTeaser_json_data_short1 = wTeaser_json_data1.partition(".")[0]
           name_json_data2 = json_tastedive_data['Similar']['Results'][2]['Name']
           type_json_data2 = json_tastedive_data['Similar']['Results'][2]['Type']
           wTeaser_json_data2= json_tastedive_data['Similar']['Results'][2]['wTeaser']
           wTeaser_json_data_short2= wTeaser_json_data2.partition(".")[0]
           name_json_data3 = json_tastedive_data['Similar']['Results'][3]['Name']
           type_json_data3 = json_tastedive_data['Similar']['Results'][3]['Type']
           wTeaser_json_data3= json_tastedive_data['Similar']['Results'][3]['wTeaser']
           wTeaser_json_data_short3= wTeaser_json_data3.partition(".")[0]
           name_json_data4 = json_tastedive_data['Similar']['Results'][4]['Name']
           type_json_data4 = json_tastedive_data['Similar']['Results'][4]['Type']
           wTeaser_json_data4= json_tastedive_data['Similar']['Results'][4]['wTeaser']
           wTeaser_json_data_short4= wTeaser_json_data4.partition(".")[0]
           print(wTeaser_json_data_source_short)
           print(name_json_data)
           print(type_json_data)
           print(wTeaser_json_data_short)
           print(name_json_data1)
           print(type_json_data1)
           print(wTeaser_json_data_short1)
           print(name_json_data2)
           print(type_json_data2)
           print(wTeaser_json_data_short2)
           line_bot_api.reply_message(
              event.reply_token,
               TextSendMessage(text=wTeaser_json_data_source_short + '\n\n' + 'Top 5 recommendations if you like ' + query + ':\n\n' +
                          '#1 ' + name_json_data  + ', ' + type_json_data + '\n' + wTeaser_json_data_short + '\n\n' +
                          '#2 ' + name_json_data1  + ', ' + type_json_data1 + '\n' + wTeaser_json_data_short1 + '\n\n' + 
                          '#3 ' + name_json_data2  + ', ' + type_json_data2 + '\n' + wTeaser_json_data_short2 + '\n\n' +
                          '#4 ' + name_json_data3  + ', ' + type_json_data3 + '\n' + wTeaser_json_data_short3 + '\n\n' + 
                          '#5 ' + name_json_data4  + ', ' + type_json_data4 + '\n' + wTeaser_json_data_short4 + '\n'))
        except:
            print('SEARCH STRING NOT FOUND')
            line_bot_api.reply_message(
              event.reply_token,
               TextSendMessage(text='Search not found'))

# implement Rally time feature
    if msg == 'rally time!':
       line_bot_api.multicast(FifthID, #5thElement
                              TextSendMessage(text='RALLY TIME GET ON NOW!!'))
       line_bot_api.push_message(group_id4,TextSendMessage(text='RALLY TIME GET ON NOW!!'))#group 1UP Family
       line_bot_api.push_message(group_id3,TextSendMessage(text='RALLY TIME GET ON NOW!!'))#1UpUv Rally Chat
       line_bot_api.push_message(group_id2,TextSendMessage(text='RALLY TIME GET ON NOW!!'))#1UP Rally NO TALK
       line_bot_api.push_message(group_id1,TextSendMessage(text='RALLY TIME GET ON NOW!!'))#R4 Room
       line_bot_api.reply_message(
           event.reply_token,
            TextSendMessage(text='All groups and users have been notified!!'))

# implement kick bot
    elif msg == 'kick bot':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))

# implement weather forecast feature
    elif 'weather in' in msg:
        weather_api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=weather_token&units=metric&q='
        city = msg[11:]
        weather_url = weather_api_address + city
        json_data = requests.get(weather_url).json()
        print(json_data)
        description_json_data = json_data['weather'][0]['description']
        temperature_json_data = json_data['main']['temp']
        country = json_data['sys']['country']
        city = json_data['name']
        print(description_json_data)
        print(temperature_json_data)
        print(country)
        print(city)
        line_bot_api.reply_message(
            event.reply_token,
             [TextSendMessage(text=city + ', ' + country),
              TextSendMessage(text=description_json_data + ', ' +  'Temp=' + str(temperature_json_data) + 'c' + ' or ' +
                             str(temperature_json_data*1.8+32) + 'F')])

# define events for bot
@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Joined this ' + event.source.type))
@handler.add(MemberJoinedEvent)
def handle_member_join(event):
    usrid = event.joined.members
    print(usrid)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Welcome!'))
@handler.add(MemberLeftEvent)
def handle_member_left(event):
    usrid = event.left.members
    print(usrid)
    line_bot_api.push_message(event.source.group_id,TextSendMessage(text='Goodbye!'))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
