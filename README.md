# Projeto TCC: Análise de Rádio FM com IA

## Como iniciar
1. Instale as dependências do sistema: `sudo apt install rtl-sdr ffmpeg`
2. Instale as bibliotecas Python: `pip install -r requirements.txt`
3. Execute o teste de captura: `python src/captura.py`
4. Execute a transcrição: `python src/transcricao.py`

## Fluxo de Dados
Antena -> RTL_FM -> .WAV -> Whisper IA -> .TXT -> NLP -> CSV -> Power BI