import os
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel, InputPeerChat
from telethon import TelegramClient, sync, events


class SendAutomatedMessage(object):
    def __init__(self, message, user_ids):
        self.message = message
        self.user_ids = user_ids

    def send_message(self, api_id, api_hash, sender_phone_number):

        # get your api_id, api_hash, token from telegram as described above
        # creating a telegram session and assigning it to a variable client
        client = TelegramClient('session', api_id, api_hash)

        # connecting and building the session
        client.connect()

        # in case of script ran first time it will ask either to input token or
        # otp sent to number or sent or your telegram id

        if not client.is_user_authorized():
            client.send_code_request(sender_phone_number)

            # signing in the client
            client.sign_in(sender_phone_number, input('Enter the code: '))

        for user_id in self.user_ids:
            try:
                # receiver user_id and access_hash, use
                # my user_id and access_hash for reference

                receiver = InputPeerUser(user_id, 0)

                # sending message using telegram client
                client.send_message(receiver, self.message, parse_mode='html')

            except Exception as e:
                # there may be many error coming in while like peer error, wrong access_hash, flood_error, etc
                print(e)

            # disconnecting the telegram session
        client.disconnect()
