from flask import Flask, render_template
import subprocess
import platform

app = Flask(__name__)

hosts = ["8.8.8.8", "1.1.1.1", "google.com"]

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"

    comando = ["ping", param, "1", host]

    resultado = subprocess.run(
        comando,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if resultado.returncode == 0:
        return "ONLINE"
    else:
        return "OFFLINE"

@app.route("/")
def index():
    resultados = []

    for host in hosts:
        status = ping(host)
        resultados.append({"host": host, "status": status})

    return render_template("index.html", resultados=resultados)


if __name__ == "__main__":
    import webbrowser

webbrowser.open("http://127.0.0.1:5000")
app.run(host="0.0.0.0", port=5000, debug=False)