import requests
import urllib.parse
from qradar.qconfig import qr_url, qr_headers


# Wrapper for api requests to QRadar. Set filters and filed in dictionary {"filter": "1field=abc,2filed=..."}
def wrap_api_test(api_method, data=None, headers=qr_headers, url=qr_url):
    def wrapper(func):
        def api_get():
            if not data:
                response = requests.get(f"{url}{api_method}", params=data,
                                        headers=headers, verify=False)
            else:
                req_fl_n_par = urllib.parse.urlencode(data)
                response = requests.get(f"{url}{api_method}?", params=req_fl_n_par,
                                        headers=headers, verify=False)
            if response.status_code != 200:
                print(f"Error HTTP: {response.status_code}")
            else:
                return func(response.text)

        return api_get

    return wrapper