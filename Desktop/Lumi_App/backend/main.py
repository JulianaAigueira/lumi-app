from fastapi import FastAPI, UploadFile, File
from ocr_service import ler_texto

app = FastAPI(title="Lumi OCR API 🚀")

@app.get("/")
def raiz():
    return {"mensagem": "API Lumi_App rodando com FastAPI 🚀"}

@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    # Salva a imagem temporariamente
    conteudo = await file.read()
    temp_file = "temp_img.png"
    with open(temp_file, "wb") as f:
        f.write(conteudo)

    # Executa OCR
    texto = ler_texto(temp_file, idioma="por")
    return {"texto_extraido": texto}
