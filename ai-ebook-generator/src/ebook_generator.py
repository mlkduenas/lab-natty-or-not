import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_indice(tema, publico, nivel):
    prompt = f"""
Crie o índice de um e-book técnico.
Tema: {tema}
Público-alvo: {publico}
Nível: {nivel}
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response.choices[0].message.content


def gerar_capitulo(tema, capitulo):
    prompt = f"""
Escreva o capítulo "{capitulo}" de um e-book técnico sobre {tema}.
Use linguagem didática e exemplos práticos.
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


def gerar_capa(tema):
    prompt = f"""
Professional minimalist ebook cover about: {tema}.
Cybersecurity and technology style.
No text.
"""
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open("output/capa.png", "wb") as f:
        f.write(image_bytes)


def main():
    tema = input("Tema do e-book: ")
    publico = input("Público-alvo: ")
    nivel = input("Nível: ")

    print("Gerando índice...")
    indice = gerar_indice(tema, publico, nivel)
    capitulos = [c for c in indice.split("\n") if c.strip()]

    ebook = f"# {tema}\n\n"

    for cap in capitulos:
        print(f"Gerando {cap}...")
        conteudo = gerar_capitulo(tema, cap)
        ebook += f"\n## {cap}\n{conteudo}\n"

    os.makedirs("output", exist_ok=True)
    with open("output/ebook.md", "w", encoding="utf-8") as f:
        f.write(ebook)

    print("Gerando capa do e-book...")
    gerar_capa(tema)

    print("E-book e capa gerados com sucesso!")


if __name__ == "__main__":
    main()

