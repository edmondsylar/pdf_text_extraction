from logging import debug
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    url_for
)
import os
from analysis import get_invoice_number, get_invoice_description


app = Flask(__name__)
app.config['UPLOAD_PATH']='uploads'

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html', name='homepage')
    elif request.method == 'POST':
        file = request.files['file']
        file_name=os.path.join(app.config['UPLOAD_PATH'],file.filename)
        file.save(file_name)


        inv_num = get_invoice_number(file_name)
        inv_dec = get_invoice_description(file_name)
        info = {
            'inv':inv_num,
            'desc': inv_dec
        }

        return render_template('index.html', info={'info': info})

if __name__ == "__main__":
    app.run(port=1050, debug=True)