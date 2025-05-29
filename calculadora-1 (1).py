import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import geocoder

# === CONFIGURAÇÕES ===
API_KEY = 'f735300abb8fadb243af1cbcba5d4d81'

# Detectar localização
g = geocoder.ip('me')
cidade = g.city
pais = g.country
CIDADE = f"{cidade},{pais}"

URL_ATUAL = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
URL_FORECAST = f"http://api.openweathermap.org/data/2.5/forecast?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

# === JANELA PRINCIPAL ===
tela = tk.Tk()
tela.title("Water Diary - Previsão do Tempo")
tela.geometry("900x700")
tela.configure(bg="white")
tela.attributes('-fullscreen', True)
def sair_fullscreen(event=None):
    tela.attributes('-fullscreen', False)
def fulltela(evente=None):
    tela.attributes('-fullscreen', True)

# === ELEMENTOS UI ===
label_local = tk.Label(tela, text="", font=("Helvetica", 16), bg="white")
label_icone = tk.Label(tela, bg="white")
label_temp = tk.Label(tela, font=("Helvetica", 48, "bold"), bg="white")
label_desc = tk.Label(tela, font=("Helvetica", 20), bg="white")
label_infos = tk.Label(tela, font=("Helvetica", 14), bg="white")
label_alerta = tk.Label(tela, font=("Helvetica", 14, "bold"), bg="white", fg="red")

label_local.pack(pady=(10, 0))
label_icone.pack()
label_temp.pack()
label_desc.pack()
label_infos.pack(pady=(5, 5))
label_alerta.pack()

frame_grafico = tk.Frame(tela, bg="white")
frame_grafico.pack(fill='both', expand=True)

# === ATUALIZAR CLIMA ===
def atualizar_clima():
    try:
        r = requests.get(URL_ATUAL)
        d = r.json()

        if r.status_code != 200:
            raise Exception(d.get("message", "Erro ao obter dados."))

        temp = d['main']['temp']
        descricao = d['weather'][0]['description']
        umidade = d['main']['humidity']
        vento = d['wind']['speed']
        chuva = d.get('rain', {}).get('1h', 0)
        icone_id = d['weather'][0]['icon']

        label_local.config(text=f"{cidade}, {pais}")
        label_temp.config(text=f"{temp:.1f} °C")
        label_desc.config(text=descricao.capitalize())
        label_infos.config(text=f"Chuva: {chuva:.0f}mm | Umidade: {umidade}% | Vento: {vento:.0f} km/h")

        # Ícone
        icon_url = f"http://openweathermap.org/img/wn/{icone_id}@2x.png"
        icon_data = Image.open(BytesIO(requests.get(icon_url).content))
        icon_img = ImageTk.PhotoImage(icon_data)
        label_icone.config(image=icon_img)
        label_icone.image = icon_img

    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível atualizar o clima:\n{e}")

# === GRÁFICO DE PREVISÃO ===
def mostrar_grafico():
    try:
        r = requests.get(URL_FORECAST)
        dados = r.json()

        if r.status_code != 200:
            raise Exception(dados.get("message", "Erro ao obter previsão."))

        previsoes = dados['list'][:8]

        horas = [p['dt_txt'][11:16] for p in previsoes]
        temps = [p['main']['temp'] for p in previsoes]
        chuvas = [p.get('pop', 0) * 100 for p in previsoes]

        fig, ax1 = plt.subplots(figsize=(9, 4))

        ax1.bar(horas, chuvas, color='skyblue', alpha=0.4, label='Chuva (%)')
        ax2 = ax1.twinx()
        ax2.plot(horas, temps, color='orange', marker='o', label='Temperatura (\u00b0C)')

        for i, (x, y) in enumerate(zip(horas, temps)):
            ax2.text(i, y + 0.5, f"{y:.0f}°", ha='center', fontsize=8, color='darkorange')

        alerta = ""
        if any(c >= 70 for c in chuvas):
            alerta = "\u26a0\ufe0f Tempestade a caminho! Leve guarda-chuva."
        elif any(50 <= c < 70 for c in chuvas):
            alerta = "\u2614 Pode chover mais tarde, fique atento."
        elif all(c <= 20 for c in chuvas):
            alerta = "☀ Clima estável hoje. Aproveite!"

        label_alerta.config(text=alerta)

        ax1.set_xlabel('Hora')
        ax1.set_ylabel('Chuva (%)', color='blue')
        ax2.set_ylabel('Temperatura (°C)', color='orange')
        fig.suptitle('Próximas horas')

        ax1.set_ylim(0, 100)
        ax2.set_ylim(min(temps)-2, max(temps)+2)
        ax1.tick_params(axis='x', rotation=45)

        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar gráfico:\n{e}")

# === EXECUTAR ===
tela.bind("<Escape>" or "<F12>", sair_fullscreen)
tela.bind("<F11>", fulltela)
atualizar_clima()
mostrar_grafico()
tela.mainloop()
