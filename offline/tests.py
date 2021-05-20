from config.api_tools import write_result_to_csv
import offline.qrtools as qrtools
from xforce import xftools


# Return table with recommended apps based on LS and apps from example files (write to csv file) - OFFLINE mode
@write_result_to_csv(r'..\offline\results\result_ga_8_file_not_installed')
def recommend_ext_file():
    recommendations_dict = {}
    ls_list = qrtools.get_ls_types_file()['SUCCESS']
    # Find not installed apps
    qapps = qrtools.get_apps_file()
    xfapps = xftools.get_content_ext()
    new_app_keys = xfapps.keys()-qapps.keys()
    # Dict of not installed apps
    new_apps = dict((key, value) for key, value in xfapps.items() if key in new_app_keys)
    # Check by type_id
    for ls in ls_list:
        for key in new_apps:
            if ls['type_id'] in new_apps[key]['type_id']:
                if ls['name'] in recommendations_dict:
                    recommendations_dict[ls['name']].append(key)
                else:
                    recommendations_dict[ls['name']] = [key]
    return recommendations_dict

# Return table with !!!ALL!!! apps based on LS and apps from example files (write to csv file) - OFFLINE mode
@write_result_to_csv(r'..\offline\results\result_ga_8_file_all')
def recommend_ext_file_all():
    recommendations_dict = {}
    ls_list = qrtools.get_ls_types_file()['SUCCESS']
    xfapps = xftools.get_content_ext()
    # Check by type_id
    for ls in ls_list:
        for key in xfapps:
            if ls['type_id'] in xfapps[key]['type_id']:
                if ls['name'] in recommendations_dict:
                    recommendations_dict[ls['name']].append(key)
                else:
                    recommendations_dict[ls['name']] = [key]
    return recommendations_dict


# Return table with hosts (Version, Status, Hostname, IP, HA, DR, Requirements for latest version)

if __name__ == '__main__':
    recommend_ext_file()
    recommend_ext_file_all()
