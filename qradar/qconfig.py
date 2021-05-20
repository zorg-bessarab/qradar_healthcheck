import os
from dotenv import load_dotenv
import base64

load_dotenv()

quser = os.getenv('Q_U')
qpassword = os.getenv('Q_P')
q_token = os.getenv('Q_T')
q_endpoint = os.getenv('Q_E')
api_v = os.getenv('A_V')
qr_url = f'https://{q_endpoint}'


def create_qr_cred():
    if quser and qpassword:
        qr_header = {
            'Authorization': b"Basic " + base64.b64encode((quser + ':' + qpassword).encode('ascii')),
            'Version': api_v,
            'Accept': 'application/json'
        }
    elif q_token:
        qr_header = {
            'SEC': q_token,
            'Version': api_v,
            'Accept': 'application/json'
        }
    else:
        raise AttributeError('Specify user:pass or token')
    return qr_header


qr_headers = create_qr_cred()


if __name__ == '__main__':
    create_qr_cred()
