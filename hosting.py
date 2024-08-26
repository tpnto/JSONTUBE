from flask import Flask, render_template, request, redirect, url_for
import os
import uuid
from archiver import JSONproc

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def urlid():
    return str(uuid.uuid4())

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        unique_id = urlid()
        filename = unique_id + '.json'

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        output_filename = f"{unique_id}.html"
        JSONproc(file_path, output_filename)

        
        return redirect(url_for('jsonfile', unique_id=unique_id))

@app.route('/uploads/<unique_id>')
def jsonfile(unique_id):
    
    output_filename = f"{unique_id}.html"
    output_filepath = os.path.join('templates', output_filename)


    if not os.path.exists(output_filepath):
        return "File not found", 404

    json_filename = f"{unique_id}.json"
    json_filepath = os.path.join(app.config['UPLOAD_FOLDER'], json_filename)
    if os.path.exists(json_filepath):
        os.remove(json_filepath)


    return render_template(output_filename)



#@app.route("/unlisted")
#def unlisted():
#    return render_template("output backup.html")

# @app.route("/index")
# def index():
    # return render_template("index.html")

@app.errorhandler(404)
def noexiste(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)