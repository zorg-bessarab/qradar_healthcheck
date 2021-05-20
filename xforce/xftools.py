from config.api_tools import wrap_api_test, parse_from_api
from xforce.xfconfig import xf_headers, xf_url


@wrap_api_test('/hub/extensions', {'filter': 'key=QRADAR_APP'}, xf_headers,
               xf_url)
@parse_from_api(dict)
def get_content_ext(response):
    stupid_dict = {}
    ext_gen = (ext for ext in response['extensions'] if 'search_tags' in ext['value']['app_details']['tags'])
    for ext in ext_gen:
        # Get app name
        ext_name = ext['value']['app_details']['locale']['en']['extension_name']
        # Get latest ver
        for key in ext['value']['app_versions']:
            if ext['value']['app_versions'][key]['status'] == 'published':
                ext_ver = key
        # Create list of hidden type_id
        s_tags = ext['value']['app_details']['tags']['search_tags']
        ls_list = [int(ls_type[ls_type.rindex('_') + 1:]) for ls_type in s_tags if 'hidden_log_source' in ls_type]
        # Create Dict
        if ls_list:
            stupid_dict[ext_name] = {'version': ext_ver, 'type_id': ls_list}
    return stupid_dict


if __name__ == '__main__':
    print(get_content_ext())
