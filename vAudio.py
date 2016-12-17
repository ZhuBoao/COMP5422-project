# all the imports
import os
import caffe_model as cm
from collections import Counter
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash, send_from_directory
from werkzeug.utils import secure_filename

# create our little application :)
app = Flask(__name__,static_url_path='')
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

app.config['UPLOAD_FOLDER'] = './static/audios'
ALLOWED_EXTENSIONS = set(['mp3'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def show_page():
    return render_template('index.html')

@app.route('/error')
def show_error():
    return render_template('error.html')

@app.route('/<path:path>')
def static_proxy(path):
  return app.send_static_file(path)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/error')
        file = request.files['file']
        if file.filename == '':
            return redirect('/error')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/play?file='+filename)

@app.route('/play')
def play():
    music_file = request.args.get('file')
    music_path = '/audios/' + music_file
    wavfile = 'tmp.wav'
    audio_file = 'static' + music_path
    pred_classes = [];
    for augmentIdx in range(0, 10):
        command = 'mpg123 -q -m -n500 -k'+str((augmentIdx+1)*500)+' -w' + wavfile + ' "' + audio_file+'"'
        print command
        os.system(command)
        out_png = audio_file+ '_'+str(augmentIdx)+'.png'
        # spec_names.append(out_png)
        cm.plotstft(wavfile, channel=0, name=out_png,alpha=1.0)
        pred_classes.append(cm.get_predict_class(out_png))
        os.remove(out_png)
    os.remove(wavfile)
    final_class,final_pricise = Counter(pred_classes).most_common(1)[0]
    final_class
    return render_template('play.html',file=music_file,path=music_path,cls=final_class)

if __name__ == '__main__':
  app.run()
