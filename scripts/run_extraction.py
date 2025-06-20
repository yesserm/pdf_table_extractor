import sys

from app.exporter.json_exporter import export_to_json
from app.extractor.dataframe_format import show_tables_from_json
from app.extractor.table_extractor import extract_tables
import os

INPUT_DIR = "data/input/"
OUTPUT_DIR = "data/output/"
FORMATO = "json"

def process(pdf_name: str):
    pdf_path = os.path.join(INPUT_DIR, pdf_name)
    extracted_tables = extract_tables(pdf_path)
    tables_cleaned_extracted = []

    for table in extracted_tables:
        table_extracted = table["table"]
        tables_cleaned_extracted.append(table_extracted)

    file_name = f"{os.path.splitext(pdf_name)[0]}_t"

    if FORMATO == "json":
        output_file = os.path.join(OUTPUT_DIR, f"{file_name}.json")
        export_to_json(tables_cleaned_extracted, output_file)
        show_tables_from_json(output_file)
    if FORMATO == "pandas":
        output_file = os.path.join(OUTPUT_DIR, f"{file_name}.json")
        show_tables_from_json(output_file)

    print(f"{len(tables_cleaned_extracted)} tables extracted from {pdf_name}")


if __name__ == "__main__":
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
    if len(files) == 0:
        print("No pdf files found")
        exit(1)
    else:
        for f in files:
            process(f)