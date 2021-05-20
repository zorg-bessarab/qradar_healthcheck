import requests
import urllib.parse
import json
import csv
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


# Wrapper for parse response type from QRadar. define type for expected input i.e list, dict.
def parse_from_api(expected_type):
    def wrapper(func):
        def wrapper_parse_json(response):
            result = json.loads(response)
            if not isinstance(result, expected_type):
                raise TypeError(f"Test function {func} expects result as {expected_type}. Check params...")
            else:
                if expected_type == list:
                    result_gen = [i for i in json.loads(response)]
                    return func(result_gen)
                else:
                    return func(result)
        return wrapper_parse_json
    return wrapper


# Wrapper to parse results from files in case no access to console
def parse_from_file(file_path):
    def wrapper(func):
        def parse_json_from_file():
            with open(file_path) as f:
                result = [i for i in json.loads(f.read())]
            return func(result)
        return parse_json_from_file
    return wrapper


# Wrapper to create sorted dicts for hosts, LSs, Offenses, etc.
# Provide a key fro qradar api field
# Use only with list responses
def categorise_the_dict(key):
    def wrapper(func):
        def categorise_wr_dict(response):
            if type(response) != list:
                raise TypeError('Use categorise_the_dict only with list type of response from api')
            cat_dict = {}
            for r in response:
                if type(r[key]) == dict:
                    s_key = r[key][key]
                else:
                    s_key = r[key]
                if s_key in cat_dict:
                    cat_dict[s_key].append(r)
                else:
                    cat_dict[s_key] = [r]
            return func(cat_dict)
        return categorise_wr_dict
    return wrapper


# Decorator to write test result to csv
def write_result_to_csv(result_name):
    def save_result_dict_to_csv(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(f'{result_name}.csv', 'w', newline='') as result_file:
                writer = csv.writer(result_file)
                for k, v in result.items():
                    writer.writerow([k, v])
        return wrapper
    return save_result_dict_to_csv


# Adds type field to ref-data
def set_key(key):
    def iter_dec(func):
        def wrapper(r_list):
            for r in r_list:
                r['type'] = key
            return func(r_list)
        return wrapper
    return iter_dec
