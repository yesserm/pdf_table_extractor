import pandas as pd
import json

def show_tables_from_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for idx, bloque in enumerate(data):
        try:
            df = pd.DataFrame(bloque)
            if df.shape[0] > 0 and df.iloc[0].notnull().any():
                df.columns = [f"Col{i}" if col is None or str(col).strip() == "" else col for i, col in enumerate(df.iloc[0])]
                df = df.drop(index=0).reset_index(drop=True)
            print(f"\nTabla {idx + 1}:\n", df)
        except Exception as e:
            print(f"Error al convertir tabla {idx + 1}: {e}")