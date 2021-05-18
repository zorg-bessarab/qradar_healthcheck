from api_tools import wrap_api_test, parse_from_api, write_result_to_csv
import qrtools
import xftools
import datetime


# Test 1 check current version of QRadar
@wrap_api_test("/api/system/about")
@parse_from_api(dict)
@write_result_to_csv('version_test')
def version_test(response):
    return response


# Test 2 Validates hosts with ERROR status
@wrap_api_test("/api/config/deployment/hosts", {"filter": "status!=Active"})
@parse_from_api(list)
def hosts_test(response):
    for i in response:
        print(f"""ServerID: {i["id"]} {i["hostname"]}@{i["private_ip"]} is in {i["status"]} state""")


# Test 2 Validates hosts Versions + encryption...
@wrap_api_test("/api/config/deployment/hosts",
               {"fields": "hostname,private_ip,appliance,average_eps,peak_eps,peak_fpm,total_memory,cpus,version,"
                          "eps_allocation,fpm_allocation, encryption_enabled, compression_enabled",
                "filter": "status=Active"})
@parse_from_api(list)
def deployment_hosts(response):
    for i in response:
        print(i)
        if i["peak_eps"] is not None and i["peak_eps"] > i["eps_allocation"] \
                or i["peak_fpm"] is not None and i["peak_fpm"] > i["fpm_allocation"]:
            print(f"""Host {i["appliance"]} on {i["private_ip"]} """
                  f"""needs to review EPS({i["peak_eps"]})/FPM({i["peak_fpm"]}) allocation""")
        elif not i["encryption_enabled"]:
            print(f"""Host {i["appliance"]} on {i["private_ip"]} """
                  f"""encryption disabled. Check settings on Admin Tab""")


# Test 19 Offense opened + general
@wrap_api_test("/api/siem/offenses", {"filter": "status=OPEN"})
@parse_from_api(list)
def test_offenses(response):
    of_count = sum(1 for i in response)
    print(f"Now {of_count} Offenses are opened.")
    if of_count >= 2500:
        print(f"Threshold of 2500 OPENed Offenses is crossed, "
              f"please close at least {of_count - 2500} or contact support")


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


# Test opt to check deployment errors
@wrap_api_test("/api/staged_config/deploy_status")
@parse_from_api(dict)
def check_deploy(response):
    print(f"Last deployment status: {response}")


# Return recommended apps based on LS (write to csv file)
@write_result_to_csv('result_1')
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


# Return recommended apps based on LS and apps from example files (write to csv file) - OFFLINE mode
@write_result_to_csv('result_ga_8_file')
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


if __name__ == '__main__':
    recommend_ext_file()
 #   version_test()
