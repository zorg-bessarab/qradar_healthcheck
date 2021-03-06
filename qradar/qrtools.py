from config.api_tools import wrap_api_test, parse_from_api, categorise_the_dict, set_key


# Get all extensions
@wrap_api_test("/api/config/extension_management/extensions", {"fields": "name,version,status"})
@parse_from_api(list)
@categorise_the_dict('name')
def get_apps_by_name(app_dict):
    return app_dict


# Get LSs from QRadar
@wrap_api_test("/api/config/event_sources/log_source_management/log_sources")
@parse_from_api(list)
@categorise_the_dict('status')
def get_ls_types(ls_dict):
    return ls_dict


# Get all hosts
@wrap_api_test("/api/config/deployment/hosts",
               {"fields": "hostname,private_ip,appliance,average_eps,peak_eps,peak_fpm,total_memory,cpus,version,"
                          "status,eps_allocation,fpm_allocation, encryption_enabled, compression_enabled"})
@parse_from_api(list)
@categorise_the_dict('status')
def get_deployment_hosts(host_dict):
    return host_dict


# Get all offenses
@wrap_api_test("/api/siem/offenses")
@parse_from_api(list)
@categorise_the_dict('status')
def get_offenses(off_dict):
    return off_dict


# Get all rules
@wrap_api_test("/api/analytics/rules")
@parse_from_api(list)
@categorise_the_dict('type')
def get_rules(rules_dict):
    return rules_dict


# Get Network Hierarchy
@wrap_api_test("/api/config/network_hierarchy/networks")
@parse_from_api(list)
@categorise_the_dict('description')
def get_net_h(net_dict):
    return net_dict


# Get reference data set
@wrap_api_test("/api/reference_data/sets")
@parse_from_api(list)
@set_key('set')
def get_ref_set(set_list):
    return set_list


# Get reference data map
@wrap_api_test("/api/reference_data/maps")
@parse_from_api(list)
@set_key('map')
def get_ref_map(map_list):
    return map_list


# Get reference data map of set
@wrap_api_test("/api/reference_data/map_of_sets")
@parse_from_api(list)
@set_key('map_of_sets')
def get_ref_map_of_sets(map_of_sets_list):
    return map_of_sets_list


# Get reference data tables
@wrap_api_test("/api/reference_data/tables")
@parse_from_api(list)
@set_key('table')
def get_ref_tables(tables_list):
    return tables_list


# Sum all reference data in 1 list
def get_all_ref():
    return get_ref_set() + get_ref_map() + get_ref_map_of_sets() + get_ref_tables()


if __name__ == '__main__':
    print(get_all_ref())
 #   print(get_ref_tables())
