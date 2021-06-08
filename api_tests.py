from qradar import qrtools as qr
# from xforce import xftools as xf
import pandas as pd


# Create table with all Reference Data (excel)
def analyse_ref_set():
    ref_list = pd.read_json(qr.get_ref_set())
    ref_list.to_excel('report.xlsx', sheet_name='reference data', index=False)
    return ref_list


def analyse_ref_map():
    ref_list = pd.read_json(qr.get_ref_map())
    return ref_list


def analyse_ref_tables():
    ref_list = pd.read_json(qr.get_ref_tables())
    return ref_list


def analyse_ref_mset():
    ref_list = pd.read_json(qr.get_ref_map_of_sets())
    return ref_list


# Create table with rules (excel)
def print_rules():
    rules_list = pd.read_json(qr.get_rules())
    return rules_list


# Create table with offenses (excel)
def print_offenses():
    offenses_list = pd.read_json(qr.get_offenses())
    return offenses_list


def write_to_excel(path=r'results\report.xlsx'):
    writer = pd.ExcelWriter(path, engine='openpyxl')
    analyse_ref_set().to_excel(writer, sheet_name='ref set')
    analyse_ref_map().to_excel(writer, sheet_name='ref map')
    analyse_ref_mset().to_excel(writer, sheet_name='ref mset')
    analyse_ref_tables().to_excel(writer, sheet_name='ref table')
    print_rules().to_excel(writer, sheet_name='rules')
    print_offenses().to_excel(writer, sheet_name='offenses')
    writer.save()
    writer.close()


if __name__ == '__main__':
    write_to_excel()
