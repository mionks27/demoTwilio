# Create your views here.
import os

from django.shortcuts import render
from twilio.base.exceptions import TwilioRestException

import twilio_demo
from twilio.rest import Client


def create_room(request):
    # Your Account Sid and Auth Token from twilio_demo.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'AC897928457dc1bd04e8e02254d1279244'
    auth_token = '66ab7e8dfefa2a529cbc580a23fd49dc'
    client = Client(account_sid, auth_token)
    try:
        room = client.video.rooms.create(unique_name='xdd')
        print(room.sid)
        context = {'room': room}
    except TwilioRestException as ex:
        print(ex)
    return render(request, 'xd.html', context)


def index(request):
    return render(request, 'index.html')
