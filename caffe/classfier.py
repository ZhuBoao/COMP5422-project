import numpy as np
import matplotlib.pyplot as plt
import caffe

caffe.set_mode_gpu()

net = caffe.Classifier(model_file='prototxt/deploy.augm_32r-2-64r-2-64r-2-128r-2-128r-2-256r-2-1024rd0.3-1024rd0.3.prototxt',
                       pretrained_file='models/augm_dropout0.3_on_augm84K-lr0.01_30K_90K_iter_2000.caffemodel')

input_image = caffe.io.load_image('/home/leonardo/Music/CloudMusic/f2.png')
plt.imshow(input_image)



prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
print 'prediction shape:', prediction[0].shape
plt.plot(prediction[0])
print 'predicted class:', prediction[0].argmax()
plt.show()
