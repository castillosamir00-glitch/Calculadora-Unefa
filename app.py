from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def pagina_principal():
  archivo = open("templates/index.html", "r", encoding="utf-8")
  html = archivo.read()
  archivo.close()

  if request.method == "POST":
    n1 = int(request.form.get("num1", 0))
    n2 = int(request.form.get("num2", 0))
    suma = str(n1 + n2)
  else:
    suma = ""

  html = html.replace("RESULTADO_AQUI", suma)
  return html


if __name__ == "__main__":
  app.run(debug=True)