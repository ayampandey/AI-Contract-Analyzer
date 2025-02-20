import os
import glob

#Path to Contract Folder
txt_folder = r"C:\Users\hp\Downloads\CUAD_v1.zip\CUAD_v1\full_contract_txt"
#glob to get a list of all text files
text_files = glob.glob(os.path.join(txt_folder, "**/*.txt"), recursive=True)

#Dictionary to store contract text keyed by file path or name
contracts_txt= {}

for file in text_files:
    with open(file, "r", encoding="utf-8") as f:
        contracts_txt[os.path.basename(file)] = f.read()

# Check if the dictionary is empty
if not contracts_txt:
    print("No contracts found or files were not loaded.")
else:
    print(f"Contracts found: {list(contracts_txt.keys())[:5]}")  # Display first 5 files

print(text_files)

file_path = r"C:\Users\hp\Downloads\CUAD_v1\CUAD_v1\full_contract_txt\AlliedEsportsEntertainmentInc_20190815_8-K_EX-10.19_11788293_EX-10.19_Content License Agreement.txt"

# Try reading a single file
try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content[:500])  # Print the first 500 characters
except Exception as e:
    print(f"Error: {e}")

# #Check one example
# sample_filename = list(contracts_txt.keys())[0]
# print(f"Contract File: {sample_filename}\n")
# print(contracts_txt[sample_filename][:500]) #first 500 characters
