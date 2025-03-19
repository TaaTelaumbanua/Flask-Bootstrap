from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Variabel untuk menyimpan data dari form
    nama = ""
    pesan = ""
    form_submitted = False
    
    # Jika form dikirim dengan metode POST
    if request.method == 'POST':
        nama = request.form.get('nama')
        pesan = request.form.get('pesan')
        form_submitted = True
    
    # Render template dengan data yang diterima
    return render_template('index.html', 
                          nama=nama, 
                          pesan=pesan, 
                          form_submitted=form_submitted)

if __name__ == '__main__':
    app.run(debug=True)