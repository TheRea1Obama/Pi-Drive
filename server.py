from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return "<a href='/upload'>Upload</a> <a href='/download'>Download</a>"

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file'] 
        if file.filename == '':
            return "No selected file"
        # save the file 
        file.save(dst=os.path.join(str(app.config['UPLOAD_FOLDER']), str(file.filename))) 
        
    return render_template('upload.html')


@app.route('/download')
def downloads():
    # List all files in the directory
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('download.html', files=files)

# Route to serve a specific file for download
@app.route('/files/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

