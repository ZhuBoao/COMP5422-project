CAFFE_ROOT=/home/leonardo/caffe
PROJECT_PATH=/home/leonardo/caffe-project

$CAFFE_ROOT/build/tools/caffe train \
    --solver=$PROJECT_PATH/prototxt/solver.augm.nolrcoef.prototxt\
    --snapshot=$PROJECT_PATH/models/augm_dropout0.3_on_augm84K-lr0.01_30K_90K_iter_30000.solverstate
    # --weights=$PROJECT_PATH/models/augm_dropout0.3_on_augm84K-lr0.01_30K_90K_iter_30000.caffemodel\
