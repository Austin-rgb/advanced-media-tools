#!amt/Scripts/python
from flask import Flask, request, redirect, url_for, send_file, render_template, flash
from pydub import AudioSegment
import os
from threading import Thread
import webbrowser
from time import sleep
from lib import xformat, mp42mp3, cropmp3
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Directory for uploaded and converted files
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

# Ensure upload and converted folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

def allowed_audio_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp3', 'wav', 'ogg', 'm4a'}

def allowed_video_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp4', 'avi', 'ogg', 'm4a'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def icon():
    return open('favicon.ico',mode='rb')

@app.route('/results', methods=['POST'])
def dump_results():
    output_path = request.form.get('output_path')
    
    # Send the converted file back to the user for download
    return send_file(output_path,as_attachment=True)

@app.route('/cropmp3',methods=['POST','GET'])
def _crop_mp3():
    if request.method == 'GET':
        return render_template('cropmp3.html')
    
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file and allowed_audio_file(file.filename):
        filename = file.filename
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        start = request.form.get('start')
        stop = request.form.get('stop')
        if start:start=int(start)
        if stop:stop=int(stop)
        # Save uploaded file
        file.save(input_path)
        
        # Generate the output filename and path
        output_filename = f'{filename}.mp3'
        output_path = os.path.join(app.config['CONVERTED_FOLDER'], output_filename)
        
        # Execute the service 
        cropmp3.crop_mp3(input_path,start,stop,output_path)
        return render_template('ready.html',output_path=output_path)
        
@app.route('/mp42mp3',methods=['POST','GET'])
def _mp42mp3():
    if request.method == 'GET':
        return render_template('mp42mp3.html')
    
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file and allowed_video_file(file.filename):
        filename = file.filename
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save uploaded file
        file.save(input_path)
        
        # Generate the output filename and path
        output_filename = f'{filename}.mp3'
        output_path = os.path.join(app.config['CONVERTED_FOLDER'], output_filename)
        
        # Execute the service 
        mp42mp3.mp42mp3(input_path,output_path)
        
        return render_template('ready.html',output_path=output_path)
        
    

@app.route('/xformat', methods=['POST','GET'])
def _xformat():
    if request.method == 'GET':
        return render_template('xformat.html')
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    print(f'found file: {file}')
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_audio_file(file.filename):
        filename = file.filename
        output_format = request.form['format']
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save uploaded file
        file.save(input_path)
        
        # Generate the output filename and path
        output_filename = f"converted.{output_format}"
        output_path = os.path.join(app.config['CONVERTED_FOLDER'], output_filename)
        
        # Execute the service 
        xformat.change_format(input_path,output_path, target_format=output_format)
        
        return render_template('ready.html',output_path=output_path)
        
    
    else:
        flash('File type not allowed')
        return redirect(request.url)

def serve():
    app.run(debug=True)

if __name__ == '__main__':
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)
    
