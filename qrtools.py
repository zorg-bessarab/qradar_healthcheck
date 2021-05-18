from api_tools import wrap_api_test, parse_json, categorise_the_dict, parse_from_file


# Get all extentions
@wrap_api_test("/api/config/extension_management/extensions", {"fields": "name,version,status"})
@parse_json(list)
@categorise_the_dict('name')
def get_apps_by_name(app_dict):
    return app_dict


# Get LSs from QRadar
@wrap_api_test("/api/config/event_sources/log_source_management/log_sources")
@parse_json(list)
@categorise_the_dict('status')
def get_ls_types(ls_dict):
    return ls_dict


# Get extensions from file
@parse_from_file('ext_ga_8')
@categorise_the_dict('name')
def get_apps_file(ls_list):
    return ls_list


# Get LSs from file
@parse_from_file('ls_ga_8')
@categorise_the_dict('status')
def get_ls_types_file(ls_dict):
    return ls_dict



# Get LS from file
@parse_json(list)
def get_from_file(content):
    return content


# Get all hosts
@wrap_api_test("/api/config/deployment/hosts",
               {"fields": "hostname,private_ip,appliance,average_eps,peak_eps,peak_fpm,total_memory,cpus,version,"
                          "status,eps_allocation,fpm_allocation, encryption_enabled, compression_enabled"})
@parse_json(list)
@categorise_the_dict('status')
def deployment_hosts(host_dict):
    return host_dict


# Get all offenses
@wrap_api_test("/api/siem/offenses")
@parse_json(list)
@categorise_the_dict('status')
def test_offenses(off_dict):
    return off_dict


if __name__ == '__main__':
    print(get_apps_by_name())
    print(get_ls_types())
    print(deployment_hosts())
    print(test_offenses())
