import subprocess
import datetime
import os

def capturar_fm(frequencia, duracao_segundos, nome_arquivo):
    """
    Usa o rtl_fm para sintonizar e o ffmpeg para salvar em .wav
    """
    caminho_saida = os.path.join("../data/raw_audio", f"{nome_arquivo}.wav")
    
    # Comando: sintoniza na frequencia, amostra a 170k, converte para wav via pipe
    comando = (
        f"rtl_fm -f {frequencia}M -M fm -s 170k -A fast -r 32k -l 0 -E deemp | "
        f"ffmpeg -f s16le -ar 32k -ac 1 -i - -t {duracao_segundos} -y {caminho_saida}"
    )
    
    print(f"Iniciando captura da frequência {frequencia}MHz...")
    try:
        subprocess.run(comando, shell=True, check=True)
        print(f"Áudio salvo em: {caminho_saida}")
    except subprocess.CalledProcessError as e:
        print(f"Erro na captura: {e}")

if __name__ == "__main__":
    # Teste: Gravar 30 segundos da rádio 98.9 (ajuste para uma rádio local ativa)
    agora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    capturar_fm(frequencia=98.9, duracao_segundos=30, nome_arquivo=f"teste_{agora}")