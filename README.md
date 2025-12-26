
# 📊 Conversor XLS/XLSX → JSON (CLI)

Uma ferramenta simples, robusta e multiplataforma para conversão de planilhas **Excel (.xls / .xlsx)** em **JSON**, desenvolvida em Python e pensada para lidar com arquivos oriundos de sistemas legados, exportações institucionais e planilhas malformadas.

O conversor trata automaticamente campos vazios, gerando `null` no JSON, e tenta diferentes estratégias de leitura para garantir maior compatibilidade.

---

## ✨ Funcionalidades

O sistema foi projetado para ser prático e resiliente, oferecendo:

  * **📥 Leitura de arquivos `.xls` e `.xlsx`**
  * **🧠 Detecção automática do formato real do arquivo**
  * **🧩 Suporte a planilhas malformadas ou exportadas por sistemas legados**
  * **🔄 Conversão automática para JSON**
  * **🚫 Tratamento de valores vazios (`NaN`, células vazias → `null`)**
  * **📁 Geração automática do arquivo `.json`**
  * **💻 Execução via linha de comando (CLI)**
  * **🪟 Compatível com Linux e Windows**

---

## 🛠️ Tecnologias Utilizadas

  * **Linguagem:** [Python 3](https://www.python.org/)
  * **Manipulação de dados:** `pandas`
  * **Leitura de planilhas modernas:** `openpyxl`
  * **Leitura de planilhas antigas (.xls):** `xlrd`
  * **Serialização:** biblioteca padrão `json`
  * **Execução:** CLI (terminal)

---

## 🚀 Como Executar

### ✅ Pré-requisitos

Verifique se o Python está instalado:

```bash
python --version
````

ou

```bash
python3 --version
```

---

## 🐧 Instalação no Linux

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

### 2️⃣ Ativar o ambiente

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install pandas openpyxl xlrd
```

---

## 🪟 Instalação no Windows

### 1️⃣ Criar ambiente virtual

```powershell
python -m venv venv
```

### 2️⃣ Ativar o ambiente

```powershell
venv\Scripts\activate
```

### 3️⃣ Instalar dependências

```powershell
pip install pandas openpyxl xlrd
```

---

## ▶️ Como usar

Coloque o arquivo Excel na mesma pasta do script ou informe o caminho completo.

```bash
python conversor.py arquivo.xls
```

ou

```bash
python conversor.py arquivo.xlsx
```

---

## 📤 Resultado gerado

O programa criará automaticamente um arquivo JSON com o mesmo nome:

```
arquivo.json
```

---

## 📄 Exemplo de saída

```json
[
    {
        "nome": "João",
        "idade": 30,
        "email": null
    },
    {
        "nome": "Ana",
        "idade": null,
        "email": "ana@email.com"
    }
]
```

✔ Campos vazios são convertidos corretamente para `null`.

---

## ⚙️ Funcionamento interno

O conversor executa os seguintes passos:

1. Identifica a extensão do arquivo (`.xls` ou `.xlsx`)
2. Tenta leitura com o engine apropriado
3. Em arquivos `.xls`, tenta múltiplas estratégias de leitura
4. Normaliza valores ausentes (`NaN`, `NaT`) → `None`
5. Converte os dados para JSON
6. Salva automaticamente o arquivo final

---

## 📂 Estrutura do Projeto

```
/
├── conversor.py        # Script principal
├── venv/               # Ambiente virtual Python
├── arquivo.xls         # Planilha de entrada
├── arquivo.json        # JSON gerado automaticamente
└── README.md           # Documentação
```

---

## 🧠 Observações Técnicas

* Muitos sistemas exportam arquivos `.xls` que **não seguem o padrão oficial do Excel**
* O script foi projetado para lidar com essas inconsistências
* A conversão prioriza robustez e compatibilidade
* O JSON gerado é adequado para:

  * APIs REST
  * bancos de dados
  * sistemas web
  * processamento posterior

---

## 🚧 Possíveis Evoluções

* Conversão automática via LibreOffice (fallback)
* Leitura de múltiplas abas
* Conversão em lote de arquivos
* CLI avançada com argumentos (`--input`, `--output`)
* Normalização de nomes de colunas
* Validação de schema
* Integração com FastAPI
* Logs estruturados
* Dockerização do projeto

---

## 🤝 Contribuição

Contribuições são bem-vindas.

1. Faça um **Fork** do projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Faça o commit (`git commit -m "Adiciona nova funcionalidade"`)
4. Faça o push (`git push origin feature/NovaFuncionalidade`)
5. Abra um **Pull Request**

---

*Desenvolvido com Python, foco em robustez e compatibilidade multiplataforma.*
