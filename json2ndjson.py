import json

print("Please enter the filename you want to transfer:")
input_file = input("Filename: ").strip()
output_file = input_file.rsplit('.', 1)[0] + ".ndjson"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    exit(1)

if not isinstance(data, list):
    raise ValueError("Top-level JSON is not a list")

with open(output_file, "w", encoding="utf-8") as out:
    for obj in data:
        out.write(json.dumps(obj, ensure_ascii=False) + "\n")

print("NDJSON written to", output_file)
