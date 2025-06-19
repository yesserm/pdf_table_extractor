import sys

from app.exporter.json_exporter import export_to_json
from app.extractor.table_extractor import extract_tables
import os

INPUT_DIR = "data/input/"
OUTPUT_DIR = "data/output/"
FORMATO = "json"

def process(pdf_name: str):
    pdf_path = os.path.join(INPUT_DIR, pdf_name)
    extracted_tables = extract_tables(pdf_path)

    iterator = 0
    for table in extracted_tables:
        table_extracted = table["table"]

        file_name = f"{os.path.splitext(pdf_name)[0]}_t{iterator}"

        if FORMATO == "json":
            output_file = os.path.join(OUTPUT_DIR, f"{file_name}.json")
            export_to_json(table_extracted, output_file)
            iterator += 1

        print(f"{len(table_extracted)} tables extracted from {pdf_name}")


if __name__ == "__main__":
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
    if len(files) == 0:
        print("No pdf files found")
        exit(1)
    else:
        for f in files:
            process(f)