import spacy
import pandas as pd
import os
from collections import Counter

# Carrega o modelo de português do spaCy
# (Lembre-se de rodar: python -m spacy download pt_core_news_sm no terminal)
nlp = spacy.load("pt_core_news_sm")

def extrair_insights(nome_arquivo_texto):
    caminho_entrada = os.path.join("../data/processed_text", nome_arquivo_texto)
    caminho_saida = os.path.join("../data/clean_data", "dados_finais.csv")
    
    with open(caminho_entrada, "r", encoding="utf-8") as f:
        texto = f.read()

    # Processa o texto com IA
    doc = nlp(texto)

    # 1. Extração de Entidades (Nomes próprios, Lugares, Organizações)
    # Isso vai captar coisas como "Acre", "Rio Branco", "Prefeitura", etc.
    entidades = [(ent.text, ent.label_) for ent in doc.ents]

    # 2. Filtragem de Palavras-Chave (Substantivos e Verbos importantes)
    palavras_chave = [token.lemma_.lower() for token in doc 
                      if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]

    # Contagem de frequência
    contagem = Counter(palavras_chave).most_common(10)

    # 3. Criar DataFrame para exportar
    # Aqui estruturamos para o seu Power BI
    df = pd.DataFrame(entidades, columns=["Termo", "Categoria"])
    df["Data_Processamento"] = pd.Timestamp.now()
    df["Fonte_Audio"] = nome_arquivo_texto
    
    # Salva ou anexa ao CSV existente
    if not os.path.isfile(caminho_saida):
        df.to_csv(caminho_saida, index=False, encoding="utf-8")
    else:
        df.to_csv(caminho_saida, mode='a', header=False, index=False, encoding="utf-8")

    print(f"Análise concluída! Dados exportados para: {caminho_saida}")
    print(f"Top 5 palavras detectadas: {contagem[:5]}")

if __name__ == "__main__":
    # Teste: Analisar o arquivo gerado na etapa anterior
    # extrair_insights("teste_exemplo.txt")
    pass