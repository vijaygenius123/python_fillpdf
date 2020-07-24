from flask import Flask, render_template,request

import os

from pdfjinja import PdfJinja

app = Flask(__name__)

dirname = os.path.dirname(__file__)
template_pdf_file = os.path.join(dirname, 'input.pdf')

template_pdf = PdfJinja(template_pdf_file)

@app.route('/',methods = ['GET'])
@app.route('/send',methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        print(name, age, gender)
        rendered_pdf = template_pdf({
            "Name": name,
            "Age": age,
            "Gender": gender,
        })

        output_file = os.path.join(dirname, 'output.pdf')
        rendered_pdf.write(open(output_file, 'wb'))
        
        return render_template('thanks.html',)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)