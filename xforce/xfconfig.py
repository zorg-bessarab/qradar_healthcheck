import os
import base64
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('XF_KEY')
api_pass = os.getenv('XF_PASS')

xf_url = 'https://api.xforce.ibmcloud.com'


def create_xf_cred():
    return b"Basic " + base64.b64encode((api_key+':'+api_pass).encode('ascii'))


xf_headers = dict(Authorization=create_xf_cred(), Accept='application/json')
