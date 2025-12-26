import pandas as pd
import json
import sys
from pathlib import Path


def ler_planilha(caminho: Path):
    if caminho.suffix.lower() == ".xlsx":
        df = pd.read_excel(caminho, engine="openpyxl")

    elif caminho.suffix.lower() == ".xls":
        try:
            df = pd.read_excel(caminho, engine="xlrd")
        except Exception:
            try:
                tabelas = pd.read_html(caminho)
                df = tabelas[0]
            except Exception:
                raise ValueError("Formato não reconhecido ou arquivo inválido.")

    else:
        raise ValueError("Formato não suportado.")

    # 🔹 converte valores vazios para None (null no JSON)
    df = df.where(pd.notna(df), None)

    return df


def main():
    if len(sys.argv) < 2:
        print("Uso: python conversor.py arquivo.xls|arquivo.xlsx")
        sys.exit(1)

    caminho = Path(sys.argv[1])

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    df = ler_planilha(caminho)

    saida = caminho.with_suffix(".json")

    with open(saida, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"JSON gerado com sucesso: {saida}")


if __name__ == "__main__":
    main()
