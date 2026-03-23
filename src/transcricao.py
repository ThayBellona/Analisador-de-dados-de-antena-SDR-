import whisper
import os

def transcrever_audio(nome_arquivo_audio):
    caminho_audio = os.path.join("../data/raw_audio", nome_arquivo_audio)
    caminho_texto = os.path.join("../data/processed_text", nome_arquivo_audio.replace(".wav", ".txt"))

    print("Carregando modelo Whisper (base)...")
    model = whisper.load_model("base") # 'base' é rápido e eficiente para português

    print(f"Transcrevendo {nome_arquivo_audio}...")
    result = model.transcribe(caminho_audio, language="pt")

    with open(caminho_texto, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"Transcrição concluída! Salvo em: {caminho_texto}")
    return result["text"]

if __name__ == "__main__":
    # Teste: Transcrever o último arquivo gravado (se existir)
    # transcrever_audio("teste_exemplo.wav")
    pass