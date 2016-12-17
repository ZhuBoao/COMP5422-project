CAFFE_ROOT=/home/leonardo/caffe
TRAIN_PATH=/home/leonardo/caffe-project/dataset/spectrograms/train
VAL_PATH=/home/leonardo/caffe-project/dataset/spectrograms/val

GLOG_logtostderr=1

$CAFFE_ROOT/build/tools/convert_imageset \
    --shuffle  \
    $TRAIN_PATH/ \
    $TRAIN_PATH/data.txt \
    $TRAIN_PATH/train_lmdb

$CAFFE_ROOT/build/tools/convert_imageset \
    --shuffle  \
    $VAL_PATH/ \
    $VAL_PATH/data.txt \
    $VAL_PATH/val_lmdb
