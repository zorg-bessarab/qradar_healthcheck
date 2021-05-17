import api_tests
import csv


# Save result of a function to csv file (for recommendations)
def save_result_dict_to_csv(result_name):
    result = api_tests.recommend_ext()
    with open(f'{result_name}.csv', 'w', newline='') as result_file:
        writer = csv.writer(result_file)
        for k, v in result.items():
            writer.writerow([k, v])


if __name__ == '__main__':
    save_result_dict_to_csv('save_recommend_v1')
