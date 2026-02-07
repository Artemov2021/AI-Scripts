from openai import OpenAI
import pandas as pd
from pathlib import Path
import sys
import json
import os

client = OpenAI()


def get_base_dir() -> Path:
    # Folder containing the running script/exe
    if getattr(sys, "frozen", False):
        here = Path(sys.executable).resolve().parent
    else:
        here = Path(__file__).resolve().parent

    # Prefer folders next to exe/script
    if (here / "input").is_dir() and (here / "output").is_dir():
        return here

    # Fallback: one folder above (your case: dist is inside project)
    parent = here.parent
    if (parent / "input").is_dir() and (parent / "output").is_dir():
        return parent

    # Otherwise: stick with 'here' (and your existing error messages will trigger)
    return here

BASE_DIR = get_base_dir()
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

print(INPUT_DIR)

if not INPUT_DIR.exists(): 
    print("Error: Input folder is not found.")
    print("Print Enter to exit.")
    input()
    sys.exit()

if not OUTPUT_DIR.exists(): 
    print("Error: Output folder is not found.")
    print("Print Enter to exit.")
    input()
    sys.exit()

if not any(INPUT_DIR.iterdir()):
    print("Error: Input folder is empty! It should contain at least one Excel file.")
    print("Print Enter to exit.")
    input()
    sys.exit()

if not any(INPUT_DIR.glob("*.xls*")):
    print("Error: Input folder doesn't contain any Excel file! The folder should contain at least one.")
    print("Print Enter to exit.")
    input()
    sys.exit()

print("Excel file is being generated...")

for output_file in OUTPUT_DIR.iterdir():
    output_file.unlink()


pd.set_option("display.max_colwidth",None)

df_list = []
input_excel_names = []

for input_file in INPUT_DIR.glob("*.xls*"):
    df_list.append(pd.read_excel(INPUT_DIR / input_file))
    input_excel_names.append(input_file.stem)
    input_table = str(df_list[-1])


input_tables_list = []

for df in df_list:
    input_tables_list.append(str(df))


developer_prompt = """
You are a product assistant. You have to make unclear descriptions more meaningful.
Return them only in the following JSON format:

[
    ["improved descriptions from table 1",...],
    ["improved descriptions from table 2",...],
    ...
]

Each table should not contain line numbers. Do not mention meal name in its description. Keep each description not longer that 70 characters.
"""
input_tables = "\n\n".join(input_tables_list)

response = client.responses.create(
    model="gpt-4.1-mini",
    input= [
        {"role":"developer","content":developer_prompt},
        {"role":"user","content":input_tables}
    ]
)


descriptions_json_object = json.loads(response.output_text)

for i in range(len(df_list)):
    # print(df_list[i])
    # print(descriptions_json_object)

    desc_col = df_list[i].columns[df_list[i].columns.str.contains("description", case=False)][0]
    df_list[i][desc_col] = descriptions_json_object[i]

   


for i, df in enumerate(df_list):
    file_path = os.path.join(OUTPUT_DIR,input_excel_names[i] + "_updated.xlsx")
    df.to_excel(file_path, index=False)


print("New Excel file was generated! ")
print("Print Enter to exit.")
input()
