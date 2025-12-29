import json
import os

def search_field_in_data(data, target_field, found_values):
    """递归搜索目标字段"""
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_field:
                if isinstance(value, (str, int, float, bool)):
                    found_values.add(str(value).strip())
                elif value is None:
                    found_values.add("null")
                else:
                    # 如果值是复杂类型，我们也记录其类型
                    found_values.add(f"[{type(value).__name__}]")
            else:
                search_field_in_data(value, target_field, found_values)
    elif isinstance(data, list):
        for item in data:
            search_field_in_data(item, target_field, found_values)

def main():
    # 第一次提问：文件名
    print("Please enter the filename you want to search (e.g., dataset.ndjson):")
    input_file = input("Filename: ").strip()
    
    # 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"\nError: File '{input_file}' not found.")
        print("Please check the filename and try again.")
        return
    
    # 第二次提问：字段名
    print("\nPlease enter the field name you want to search (e.g., laterality):")
    target_field = input("Field name: ").strip()
    
    # 存储所有唯一的值
    unique_values = set()
    field_found = False
    count = 0
    
    print(f"\nSearching for field '{target_field}' in file '{input_file}'...")
    
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                try:
                    obj = json.loads(line)
                    
                    # 搜索字段
                    search_field_in_data(obj, target_field, unique_values)
                    
                    # 如果找到了至少一个值，标记字段已找到
                    if unique_values and not field_found:
                        field_found = True
                    
                    count += 1
                    
                    if count % 10000 == 0:
                        print(f"Scanned {count:,} records, found {len(unique_values):,} unique values...")
                        
                except json.JSONDecodeError:
                    # 跳过JSON解析错误的行
                    continue
                    
    except Exception as e:
        print(f"\nError reading file: {str(e)}")
        return
    
    # 检查是否找到字段
    if not field_found:
        print(f"\nError: Field '{target_field}' not found in any record.")
        print("Please check the field name and try again.")
        return
    
    # 转换为排序列表
    sorted_values = sorted(unique_values)
    
    # 生成输出文件名
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_{target_field}_values.json"
    
    # 保存结果
    result = {
        "source_file": input_file,
        "field": target_field,
        "total_records": count,
        "unique_values_count": len(sorted_values),
        "values": sorted_values
    }
    
    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(result, out, ensure_ascii=False, indent=2)
    
    # 输出总结
    print(f"\nDone!")
    print(f"Total records scanned: {count:,}")
    print(f"Unique values found for '{target_field}': {len(sorted_values):,}")
    if sorted_values:
        print(f"Values: {', '.join(sorted_values[:10])}" + 
              ("..." if len(sorted_values) > 10 else ""))
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    main()
