# TODO здесь писать код

import json

diff_list = ["services", "staff", "datetime"]
result_dict = dict()

with open('json_old.json', 'r') as old_file, \
        open('json_new.json', 'r') as new_file:
    old_data = json.load(old_file)['data']
    new_data = json.loads(new_file.read())['data']

    for i_parm in diff_list:
        if new_data[i_parm] != old_data[i_parm]:
            result_dict[i_parm] = [new_data[i_parm], old_data[i_parm]]

    with open('result.json', 'w') as result_file:
        result_file.write(json.dumps(result_dict, indent=4))
    print(result_dict)