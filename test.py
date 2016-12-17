# -*- coding: utf-8 -*-
import caffe_model as cm
from collections import Counter
import os
# get_predict_class('caffe_model/16_9.png')
# print cm.get_predict_class('caffe_model/16_9.png')
wavfile = 'tmp.wav'
audio_file = 'static/audios/7AND5 - Crossroads.mp3'
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
print pred_classes
most_common,num_most_common = Counter(pred_classes).most_common(1)[0]
print most_common,num_most_common
