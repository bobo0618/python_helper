from easydict import *
import numpy as np
import simplejson as jason

CFG = EasyDict()
CFG.TRAIN = EasyDict()
CFG.TRAIN.IMS_PER_BATCH = 1  # Images to use per minibatch

#rpn
CFG.TRAIN.RPN_BATCHSIZE    = 256
CFG.TRAIN.RPN_FG_FRACTION  = 0.5
CFG.TRAIN.RPN_FG_THRESH_LO = 0.7
CFG.TRAIN.RPN_BG_THRESH_HI = 0.3

CFG.TRAIN.RPN_NMS_THRESHOLD = 0.7
CFG.TRAIN.RPN_NMS_MIN_SIZE  = 8
CFG.TRAIN.RPN_NMS_PRE_TOPN  = 6000
CFG.TRAIN.RPN_NMS_POST_TOPN = 1200


#rcnn
CFG.TRAIN.RCNN_BATCH_SIZE   = 128
CFG.TRAIN.RCNN_FG_FRACTION  = 0.25
CFG.TRAIN.RCNN_BG_THRESH_HI = 0.5
CFG.TRAIN.RCNN_BG_THRESH_LO = 0.1
CFG.TRAIN.RCNN_FG_THRESH_LO = 0.5
CFG.TRAIN.RCNN_box_NORMALIZE_STDS = (0.1, 0.1, 0.2, 0.2)


#test -----------------------------------------
CFG.TEST  = EasyDict()

CFG.TEST.RCNN_NMS_AFTER = 0.3
CFG.TEST.RCNN_box_NORMALIZE_STDS = CFG.TRAIN.RCNN_box_NORMALIZE_STDS
CFG.TEST.USE_box_VOTE = 1

def write_cfg(file):
    with open(file, 'w') as f:
        jason.dump(CFG, f, indent =4)

def read_cfg(file):
    with open(file,'r') as f:
        cfg = EasyDict(jason.load(f))
        return cfg

file = "test.json"
# write_cfg(file)
cfg = read_cfg(file)
print (cfg)
