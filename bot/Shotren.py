import requests
import random
import base64
import string
from urllib.parse import quote
from urllib3 import disable_warnings

SHORTENER = "https://atglinks.com/"
SHORTENER_API = "498ee7efdd27b59fa6436070a5a3eb28d1a39e80"

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def short_url(longurl):
    disable_warnings()
    random_string = generate_random_string()
    short_url = f'{SHORTENER}{random_string}'
    return requests.get(f'{short_url}api?api={SHORTENER_API}&url={longurl}&format=text').text

def checking_access(user_id, button=None):
    if not config_dict['TOKEN_TIMEOUT']:
        return None, button
    user_data.setdefault(user_id, {})
    data = user_data[user_id]
    expire = data.get('time')
    isExpired = (expire is None or expire is not None and (
        time() - expire) > config_dict['TOKEN_TIMEOUT'])
    if isExpired:
        token = data['token'] if expire is None and 'token' in data else str(
            uuid4())
        if expire is not None:
            del data['time']
        data['token'] = token
        user_data[user_id].update(data)
        if button is None:
            button = ButtonMaker()
        button.ubutton('Refresh Token', short_url(
            f'https://t.me/{bot_name}?start={token}'))
        return 'Token is expired, refresh your token and try again.', button
    return None, button
    
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token
