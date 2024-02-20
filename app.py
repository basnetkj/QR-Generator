from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    qr = qrcode.make(text)
    qr.save('static/qrcode.png')
    return render_template('generated.html')

if __name__ == '__main__':
    app.run(debug=True)
