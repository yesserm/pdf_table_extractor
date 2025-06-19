import json
import os
from typing import List


def export_to_json(table: List[List[str]], output_path: str) -> None:
    """
    Export a table to a json file
    :param table:
    :param output_path:
    :return:
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(table, file, ensure_ascii=False, indent=2)