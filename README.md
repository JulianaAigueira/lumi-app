# 🌟 Lumi - MVP

O **Lumi** é um aplicativo de acessibilidade que ajuda pessoas com deficiência visual e auditiva a interagir com o mundo físico de forma mais autônoma.  
Ele utiliza **inteligência artificial** para leitura, descrição de imagens e transcrição de áudio.

---

## 🎯 Objetivo
Oferecer recursos essenciais de acessibilidade em um aplicativo simples e intuitivo, com botões grandes, contraste acessível e retorno em texto/voz.

---

## 🔹 Funcionalidades do MVP

### 1. 📷 Câmera Inteligente
- O usuário tira uma foto.
- O backend processa e a IA descreve a cena.
- A descrição pode ser exibida na tela ou narrada em voz (TTS).

### 2. 📄 Leitura de Texto (OCR + TTS)
- O usuário fotografa um texto (placa, documento, livro, cardápio).
- O OCR converte a imagem em texto.
- O texto pode ser exibido ou narrado em voz.

### 3. 🎙️ Transcrição de Áudio (STT)
- O usuário grava um áudio ou fala no microfone.
- O backend converte em texto.
- O texto é exibido na tela.

### 4. 🎤 Comando de Voz
- O usuário emite comandos simples (ex: “ler texto”).
- O app ativa automaticamente a funcionalidade correspondente.

---

## 🔹 Funcionalidades Futuras
- Configurações de acessibilidade (volume, contraste, velocidade da fala).
- Suporte multilíngue (português e inglês).
- Histórico das últimas 5 ações.

---

## 🛠️ Tecnologias
- **Frontend:** (a definir – ex: React Native / Flutter)  
- **Backend:** FastAPI (Python)  
- **IA:** OCR, TTS, STT, visão computacional  
- **Banco de dados:** (se necessário para histórico)

---

## 📂 Estrutura do Projeto


lumi-app/
├── backend/ # Código do backend (API FastAPI, IA, OCR, TTS, STT)
├── frontend/ # Aplicativo mobile/web
├── docs/ # Documentação, wireframes, anotações
├── README.md # Documentação inicial do projeto
├── .gitignore # Arquivos/pastas ignorados pelo Git
└── requirements.txt # Dependências do backend



---

## 🚀 Como rodar (inicialmente)
```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/lumi-app.git

cd lumi-app

# Instalar dependências do backend
pip install -r requirements.txt

👥 Contribuidores

Juliana Aigueira – Idealizador(a) e desenvolvedor(a) inicial
