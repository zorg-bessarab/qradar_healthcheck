from config.api_tools import categorise_the_dict, parse_from_file, set_key


# Get extensions from file
@parse_from_file(r'..\offline\sources\ext_ga_8')
@categorise_the_dict('name')
def get_apps_file(ext_dict):
    return ext_dict


# Get LSs from file
@parse_from_file(r'..\offline\sources\ls_ga_8')
@categorise_the_dict('status')
def get_ls_types_file(ls_dict):
    return ls_dict


# Get all hosts
@parse_from_file(r'..\offline\sources\hosts_ga_8')
@categorise_the_dict('status')
def get_deployment_hosts(host_dict):
    return host_dict


# Get all offenses
@parse_from_file(r'..\offline\sources\offenses_ga_8')
@categorise_the_dict('status')
def get_offenses(off_dict):
    return off_dict


# Get all rules
@parse_from_file(r'..\offline\sources\rules_ga_8')
@categorise_the_dict('type')
def get_rules(rules_dict):
    return rules_dict


# Get Network Hierarchy
@parse_from_file(r'..\offline\sources\networkh_ga_8')
@categorise_the_dict('description')
def get_net_h(net_dict):
    return net_dict


# Get reference data set
@parse_from_file(r'..\offline\sources\refset_ga_8')
@set_key('set')
def get_ref_set(set_list):
    return set_list


# Get reference data map
@parse_from_file(r'..\offline\sources\refmap_ga_8')
@set_key('map')
def get_ref_map(map_list):
    return map_list


# Get reference data map of set
@parse_from_file(r'..\offline\sources\mapofset_ga_8')
@set_key('map_of_sets')
def get_ref_map_of_sets(map_of_sets_list):
    return map_of_sets_list


# Get reference data tables
@parse_from_file(r'..\offline\sources\reftables_ga_8')
@set_key('table')
def get_ref_tables(tables_list):
    return tables_list


# Sum all reference data in 1 list
def get_all_ref():
    return get_ref_set() + get_ref_map() + get_ref_map_of_sets() + get_ref_tables()