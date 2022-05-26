from SendAutomatedMessage import SendAutomatedMessage


if __name__ == '__main__':
    # Get the api_id, api_hash from Telegram and enter the same here below.
    # The below entered api_id, api_hash, sender_phone_number and user_ids are dummy.

    api_id = 11111111
    api_hash = 'aabbccddeeff'
    sender_phone_number = '+912222222222'

    message = 'Hi. This is an automated message!'
    user_ids = [1718557619, 1718547613]
    s = SendAutomatedMessage(message, user_ids)
    result = s.send_message(api_id, api_hash, sender_phone_number)
