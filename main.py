import os
import datetime
from src.captura import capturar_fm
from src.transcricao import transcrever_audio
from src.analise import extrair_insights

def executar_pipeline(frequencia, duracao):
    """
    Executa o fluxo completo: Captura -> Transcrição -> Análise
    """
    # 1. Gerar nome único baseado no horário atual
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    nome_base = f"radio_{frequencia}_{timestamp}"
    arquivo_audio = f"{nome_base}.wav"
    arquivo_texto = f"{nome_base}.txt"

    print(f"\n--- Iniciando Ciclo de Processamento [{timestamp}] ---")

    # Passo 1: Captura via Antena/SDR
    try:
        capturar_fm(frequencia, duracao, nome_base)
    except Exception as e:
        print(f"❌ Falha na captura: {e}")
        return

    # Passo 2: Transcrição com Whisper
    if os.path.exists(f"data/raw_audio/{arquivo_audio}"):
        try:
            transcrever_audio(arquivo_audio)
        except Exception as e:
            print(f"❌ Falha na transcrição: {e}")
            return
    else:
        print("❌ Arquivo de áudio não encontrado para transcrição.")
        return

    # Passo 3: Extração de Entidades e NLP
    if os.path.exists(f"data/processed_text/{arquivo_texto}"):
        try:
            extrair_insights(arquivo_texto)
        except Exception as e:
            print(f"❌ Falha na análise de dados: {e}")
    else:
        print("❌ Arquivo de texto não encontrado para análise.")

    print(f"\n--- Ciclo Finalizado com Sucesso para {frequencia}MHz! ---")

if __name__ == "__main__":
    # CONFIGURAÇÃO DE TESTE
    FREQUENCIA_ALVO = 98.9  # Ajuste para uma rádio forte de Rio Branco
    TEMPO_GRAVACAO = 60     # Segundos para o primeiro teste
    
    executar_pipeline(FREQUENCIA_ALVO, TEMPO_GRAVACAO)