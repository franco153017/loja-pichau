from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo para os Produtos
produtos = [
    {"id": 1, "nome": "Camiseta Gamer", "preco": 79.90, "images": "camiseta_gamer.jpg"},
    {"id": 2, "nome": "Mousepad RGB", "preco": 49.90, "images": "mousepad_rgb.jpg"},
    {"id": 3, "nome": "Fone de Ouvido", "preco": 199.90, "images": "fone_ouvido.jpg"},
    {"id": 4, "nome": "Teclado Mecânico", "preco": 299.90, "images": "teclado_mecanico.jpg"},
]
# Dados de exemplo para os perifericos
Periféricos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.00, "images": "teclado_mecanico.jpg"},
    {"id": 2, "nome": "Mouse Gamer", "preco": 150.00, "images": "mouse.jpg"},
    {"id": 3, "nome": "Headset", "preco": 300.00, "images": "fone_ouvido.jpg"},
    {"id": 4, "nome": "Monitor 144Hz", "preco": 1200.00, "images": "monitor.jpg"},
]
# Dados de exemplo para os Hardwares
Hardwares = [  
    {"id": 1, "nome": "Placa de Vídeo RTX 3080", "preco": 4500.00, "images": "rtx3080.jpg"},
    {"id": 2, "nome": "Processador Intel i9", "preco": 3500.00, "images": "i9.jpg"},
    {"id": 3, "nome": "Memória RAM 32GB", "preco": 800.00, "images": "ram32gb.jpg"},
    {"id": 4, "nome": "SSD 1TB", "preco": 600.00, "images": "ssd1tb.jpg"},
]   
# Dados de exemplo para os consoles
consoles = [
    {"id": 1, "nome": "PlayStation 5", "preco": 4999.00, "images": "ps5.jpg"},
    {"id": 2, "nome": "Xbox Series X", "preco": 4999.00, "images": "xbox_series_x.jpg"},
    {"id": 3, "nome": "Nintendo Switch", "preco": 2999.00, "images": "nintendo_switch.jpg"},
    {"id": 4, "nome": "PlayStation 4 Pro", "preco": 2499.00, "images": "ps4_pro.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def mostrar_produtos():
    return render_template('produtos.html', produtos=produtos)
 

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/perifericos')
def perifericos():
    return render_template('perifericos.html')

@app.route('/hardware')
def hardware():
    return render_template('hardware.html')

@app.route('/consoles')
def consoles():     
    return render_template('consoles.html')


if __name__ == '__main__':
    app.run(debug=True)