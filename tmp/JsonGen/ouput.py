import json
import os
from itertools import product

# Đọc dữ liệu từ tệp input.json
with open('input_2.json', 'r') as file:
    input_data = json.load(file)

# Lấy danh sách items từ input_data
items_list = input_data["items_list"]

# Tạo dictionary từ danh sách items
initial_json = {}
variations = {}

for item in items_list:
    prop = item["property"]
    desc = item["desc"]
    
    # Nếu isNull là True, thêm None vào các giá trị có thể
    if desc["isNull"]:
        values = desc["listvalue"] + [None]
    else:
        values = desc["listvalue"]
    
    initial_json[prop] = values[0]  # Giá trị đầu tiên làm giá trị mặc định
    variations[prop] = values

# Hàm để tạo các pattern JSON
def generate_json_patterns(data, key_variations):
    keys, values = zip(*key_variations.items())
    patterns = [dict(zip(keys, v)) for v in product(*values)]
    return patterns

# Tạo các pattern JSON từ initial_json
json_patterns = generate_json_patterns(initial_json, variations)

# Tạo thư mục để lưu các tệp JSON
output_dir = "json_patterns"
os.makedirs(output_dir, exist_ok=True)

# Lưu từng JSON pattern vào một tệp riêng lẻ
for i, pattern in enumerate(json_patterns):
    # Bỏ qua các trường có giá trị là None
    pattern = {k: v for k, v in pattern.items() if v is not None}
    
    filename = os.path.join(output_dir, f'json_pattern_{i+1}.json')
    with open(filename, 'w') as file:
        json.dump(pattern, file, indent=4)

print("Các tệp JSON đã được tạo thành công trong thư mục 'json_patterns'.")
