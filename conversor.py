import pandas as pd
import json
import sys
from pathlib import Path


def xlsx_para_json(caminho_arquivo: str):
    arquivo = Path(caminho_arquivo)

    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

    df = pd.read_excel(arquivo)
    return df.to_dict(orient="records")


def main():
    if len(sys.argv) < 2:
        print("Uso: python conversor.py arquivo.xlsx")
        sys.exit(1)

    caminho_xlsx = sys.argv[1]
    dados = xlsx_para_json(caminho_xlsx)

    arquivo_saida = Path(caminho_xlsx).with_suffix(".json")

    with open(arquivo_saida, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print(f"Arquivo JSON gerado com sucesso: {arquivo_saida}")


if __name__ == "__main__":
    main()
