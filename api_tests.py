from config.api_tools import wrap_api_test, parse_from_api, write_result_to_csv, write_list_to_csv
from qradar import qrtools
from xforce import xftools
import datetime


# Test 1 check current version of QRadar
@wrap_api_test("/api/system/about")
@parse_from_api(dict)
@write_result_to_csv(r'results\qradar_version')
def version_test(response):
    return response


# Test 24 Validates system backup settings
@wrap_api_test("/api/backup_and_restore/backups")
@parse_from_api(list)
def backup_test(response):
    time_delta = datetime.datetime.now() - datetime.timedelta(days=3)
    for i in response:
        start_time = datetime.datetime.fromtimestamp(i['time_initiated'] / 1000)
        if i["status"] != "SUCCESS":
            print(f"""Incomplete {i["type"]} backup {i["name"]}@{i["id"]} detected:
            initiated by {i["intiated_by"]}, 
            started on {start_time}, 
            description - {i["description"]}""")
        else:
            if time_delta.timestamp() < i['time_completed'] / 1000:
                print(f"""The last 3 day backup: {i["name"]}@{i["id"]} """
                      f"""initiated by {i["intiated_by"]} on {start_time}.""")


# Return recommended apps based on LS (write to csv file)
@write_result_to_csv(r'results\recommended_log_source_extensions')
def recommend_ext():
    recommendations_dict = {}
    ls_list = qrtools.get_ls_types()['SUCCESS']
    # Find not installed apps
    qapps = qrtools.get_apps_by_name()
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


# Create table with all Reference Data
@write_list_to_csv(r'results\reference_data_table')
def analyse_ref_data():
    ref_list = qrtools.get_all_ref()
    return ref_list


if __name__ == '__main__':
#    recommend_ext()
#    version_test()
    analyse_ref_data()
