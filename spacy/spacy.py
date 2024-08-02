import spacy

print(dir(spacy))
# Carregue o modelo em português
nlp = spacy.load("pt_core_news_sm")

# Texto de entrada
texto = "O gato preto saltou sobre o muro."

# Processamento do texto com spaCy
doc = nlp(texto)

# Mostrar as classes gramaticais de cada palavra
print("Classes gramaticais:")
for token in doc:
    print(f"{token.text}: {token.pos_}")

# Identificar sujeito e predicado
sujeito = None
predicado = None

for token in doc:
    if "subj" in [child.dep_ for child in token.children]:
        sujeito = token.text
    elif token.dep_ == "ROOT":
        predicado = token.text

print(f"Sujeito: {sujeito}")
print(f"Predicado: {predicado}")
