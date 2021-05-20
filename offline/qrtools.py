from config.api_tools import categorise_the_dict, parse_from_file


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
