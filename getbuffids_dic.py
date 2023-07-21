import json


def create_data_dict(input_file):
    data_dict = {}
    with open(input_file, 'r', encoding='utf-8') as f:  # 显式指定使用UTF-8编码
        for line in f:
            item_id, item_name = line.strip().split(';')
            data_dict[int(item_id)] = item_name

    return data_dict


def save_dict_to_json(data_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:  # 保存为UTF-8编码的JSON文件
        json.dump(data_dict, f, ensure_ascii=False)  # ensure_ascii设为False，以保留非ASCII字符


# 输入文件
input_file_path = 'buffids.txt'

# 导出为字典文件
data_dict = create_data_dict(input_file_path)
output_file_path = 'buffids_dict.json'
save_dict_to_json(data_dict, output_file_path)

print("数据已成功导出为字典文件 'buffids_dict.json'")
