from flask import Flask, render_template_string

app = Flask(__name__)

# 🔹 Dummy Data
data = [
    {"id": "A12", "bpm": "0x5A", "oxygen": None, "med": "khoor"},
    {"id": "B13", "bpm": "0x3C", "oxygen": 92, "med": "sdudfhwdpro"},
    {"id": "C14", "bpm": "0x70", "oxygen": None, "med": "grfwr"},
]

# 🔹 Caesar Cipher Decode
def decode_med(text):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr(ord(char) - 3)
        else:
            result += char
    return result

# 🔹 Process Data
def process_data(data):
    processed = []
    for d in data:
        bpm = int(d["bpm"], 16)  # hex → int
        oxygen = d["oxygen"] if d["oxygen"] else 95
        med = decode_med(d["med"])

        ward = "A" if int(d["id"][-1]) % 2 == 0 else "B"

        alert = "🚨 ALERT" if bpm < 60 or bpm > 100 else "Normal"

        processed.append({
            "id": d["id"],
            "bpm": bpm,
            "oxygen": oxygen,
            "med_before": d["med"],
            "med_after": med,
            "ward": ward,
            "alert": alert
        })
    return processed

@app.route("/")
def home():
    processed = process_data(data)

    return render_template_string("""
    <html>
    <head>
        <title>Lazarus Dashboard</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #0f172a;
                color: white;
                margin: 0;
                padding: 20px;
            }

            h1 {
                text-align: center;
                color: #38bdf8;
            }

            .container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }

            .card {
                background: #1e293b;
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.5);
                transition: 0.3s;
            }

            .card:hover {
                transform: scale(1.05);
            }

            .title {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
                color: #facc15;
            }

            .label {
                color: #94a3b8;
            }

            .value {
                font-size: 18px;
                margin-bottom: 8px;
            }

            .alert {
                padding: 8px;
                border-radius: 8px;
                font-weight: bold;
                text-align: center;
            }

            .normal {
                background: #16a34a;
            }

            .danger {
                background: #dc2626;
                animation: blink 1s infinite;
            }

            @keyframes blink {
                50% { opacity: 0.5; }
            }
        </style>
    </head>

    <body>

    <h1>🏥 Lazarus Medical Dashboard</h1>

    <div class="container">
        {% for p in data %}
        <div class="card">
            <div class="title">👤 Patient {{p.id}}</div>

            <div class="value"><span class="label">Ward:</span> {{p.ward}}</div>
            <div class="value"><span class="label">❤️ BPM:</span> {{p.bpm}}</div>
            <div class="value"><span class="label">🫁 Oxygen:</span> {{p.oxygen}}</div>

            <div class="value">
                <span class="label">💊 Medicine:</span><br>
                <small>{{p.med_before}}</small> ➡ <b>{{p.med_after}}</b>
            </div>

            {% if p.alert == "🚨 ALERT" %}
                <div class="alert danger">🚨 CRITICAL</div>
            {% else %}
                <div class="alert normal">✅ NORMAL</div>
            {% endif %}
        </div>
        {% endfor %}
    </div>

    </body>
    </html>
    """, data=processed)

if __name__ == "__main__":
    app.run(debug=True)
