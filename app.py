from flask import Flask, jsonify
import google.generativeai as genai

app = Flask(__name__)

# 🔑 API anahtarı
genai.configure(api_key="AIzaSyC_RCbQjtKrQCFhrZs-QHOBV0rSUi_CfHI")

# 🧠 "models/gemini-pro"
model = genai.GenerativeModel(model_name="models/gemini-pro")

@app.route("/get-products")
def get_products():
    with open("transkript.txt", "r", encoding="utf-8") as f:
        transcript = f.read()

    prompt = f"""
Aşağıdaki metni analiz et. Metinde geçen somut ürünleri listele. 
Her biri için:
- Ürün adı
- Kısa tanım (1-2 cümle)

Metin:
\"\"\"{transcript}\"\"\"

Format:
[
  {{ "name": "...", "desc": "..." }},
  ...
]
"""

    response = model.generate_content(prompt)
    
    try:
        # .text 
        result = eval(response.text)
        return jsonify(result)
    except Exception as e:
        print("HATA:", e)
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
