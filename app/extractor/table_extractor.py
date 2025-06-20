import pdfplumber
from typing import List, Dict

def extract_tables(pdf_path: str) -> List[Dict]:
    """
    Extract tables from pdf file
    :param pdf_path:
    :return:
    """
    extracted_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            raw_tables = page.extract_tables()
            for table in raw_tables:
                if not table:
                    continue

                extracted_tables.append({
                    'table': table,
                })
    return extracted_tables