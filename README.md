# Lumi App

Lumi é um aplicativo de acessibilidade que oferece ferramentas para leitura e interpretação de conteúdos multimídia:

- **OCR**: Leitura de textos de imagens.
- **STT**: Reconhecimento de fala para texto.
- **TTS**: Síntese de fala para leitura de textos.
- **Descrição de imagens**: Geração de descrição automática de imagens.

---

## Índice

- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Como rodar](#como-rodar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Funcionalidades

Descreva aqui cada funcionalidade com exemplos de uso. Por exemplo:

```python
# Exemplo de OCR
from backend.modules.ocr import ler_imagem

texto = ler_imagem("images/exemplo.png")
print(texto)


Instalação

Clone o repositório:
git clone https://github.com/JulianaAigueira/lumi-app.git


Crie um ambiente virtual:

python -m venv venv


Ative o ambiente:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Como rodar
python backend/app.py


Substitua app.py pelo arquivo principal do seu backend.

Estrutura do Projeto
Lumi_App/
│
├─ backend/         # Código principal
│   ├─ __init__.py
│   ├─ app.py       # Arquivo principal
│   ├─ modules/     # Funcionalidades separadas (OCR, STT, TTS, etc.)
│   └─ utils/       # Funções auxiliares
│
├─ images/          # Recursos estáticos
├─ venv/            # Ambiente virtual (ignorado pelo git)
├─ .gitignore
├─ README.md
└─ requirements.txt

Contribuição

Contribuições são bem-vindas!

Faça um fork do projeto.

Crie uma branch com sua feature: git checkout -b minha-feature

Faça suas alterações e teste.

Commit e push:

git commit -m "Minha contribuição"
git push origin minha-feature
