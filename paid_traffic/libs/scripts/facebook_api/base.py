import os

from dotenv import load_dotenv

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

class InvalidAccessTokenError(Exception): #TODO create a exceptions of all error for the facebook_api, inside scripts
    pass

load_dotenv()

access_token = os.environ['ACCESS_TOKEN']

if not access_token:
    raise InvalidAccessTokenError("Please, put the secret_tokens inside .env to work properly or change manually")

app_id = os.environ['APP_ID']
app_secret = os.environ['APP_SECRET']
ad_account_id = os.environ['AD_ACCOUNT_ID']

FacebookAdsApi.init(app_id, app_secret, access_token)