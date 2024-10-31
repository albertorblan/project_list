from locale import currency
from openai import OpenAI
import json
import os

product_list = []
categories_processed = set()

#marketplace = "mercadona"
#location = "C. de la Natación, S/N, 28911 Leganés, Madrid"
currency = "euros"

model = "gpt-4o"
client = OpenAI(
    api_key="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"
)

def normalize(text):
    return text.strip().lower().rstrip(".").rstrip(" ")

def query_openai(prompt):
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        max_tokens=100,
    )
    return normalize(chat_completion.choices[0].message.content)

def classify(prod, marketplace, location):
    print(f"Clasificando {prod} para {normalize(marketplace)} en {normalize(location)}")

    prompt = (
        f"Dado el producto '{normalize(prod)}', devuelve un JSON con las siguientes claves: "
        f"'nombre' (el nombre estándar del prducto), 'categoria', 'distancia' y 'precio'. "
        f"Clasifica el producto en una categoría del supermercado '{normalize(marketplace)}' en la ubicación '{normalize(location)}'. "
        f"La distancia debe ser un número del 0 al 999 que simule el tiempo que tardarías en llegar al producto. "
        f"El precio debe ser un valor razonable en {normalize(currency)} acompañado del símbolo de la moenda. "
        "Por favor, responde siempre en este formato JSON: {\"nombre\": \"\", \"categoria\": \"\", \"distancia\": 0, \"precio\": 0.0}."
    )

    response = query_openai(prompt)


    response_data = json.loads(response)
    name = response_data.get("nombre")
    category = response_data.get("categoria")
    distance = response_data.get("distancia")
    price = response_data.get("precio")

    product_entry = {
        "Producto": prod,
        "Categoria": category,
        "Distancia": distance,
        "Precio": price
    }
    print("Nuevo producto: ", name)
    #product_list.append(product_entry)

    return product_entry

if __name__ == "__main__":
    while True:
        classify(input("Añade un producto: "), "mercadona", "C. de la Natación, S/N, 28911 Leganés, Madrid")
