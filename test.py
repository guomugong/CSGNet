import numpy as np
import scipy.misc
from PIL import Image
import scipy.io
import os
import scipy
import sys
import time
import decimal

os.environ['GLOG_minloglevel'] = '2'
caffe_root = '..'
sys.path.insert(0, caffe_root+'/python/')
import caffe

run_on_cpu = 0

if run_on_cpu == 1:
    caffe.set_mode_cpu()
else:
    caffe.set_mode_gpu()
    caffe.set_device(0)

net_struct = './deploy_csg.prototxt'

data_root = '/xxx/'
data_source = './xxx.lst'

##
save_root = './results/'

with open(data_source) as f:
    imnames = f.readlines()

test_lst = [data_root + x.strip() for x in imnames]
# load net
net = caffe.Net(net_struct,'./pretrain_model/pretrain_hrf.caffemodel', caffe.TEST);
    

totaltime = 0
for idx in range(0,len(test_lst)):
    print("Scoring for image " + data_root + imnames[idx][:-1])

    start = time.time()
    
    #Read and preprocess data
    im = Image.open(test_lst[idx])

    im = im.resize((876,584)) # resize
    in_ = np.array(im, dtype=np.float32)
    in_ = in_[:,:,::-1] #BGR
    in_ = in_.transpose((2,0,1))   # HWC -> CHW

    # Feed Data
    net.blobs['data'].reshape(1, *in_.shape)
    net.blobs['data'].data[...] = in_

    # Inference
    net.forward()

    # Save Prediction
    scipy.misc.imsave(save_root+imnames[idx][:-1][0:-4]+'.png', net.blobs['output'].data[0][0,:,:])

    end = time.time()
    print('Running time: %s seconds'%(end-start)) 
    if (idx != 0):
      totaltime = totaltime + (end-start)
print('Average processing time %s seconds'%(totaltime/(len(test_lst)-1)))
