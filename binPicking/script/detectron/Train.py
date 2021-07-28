#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch, torchvision
print(torch.__version__, torch.cuda.is_available())


# In[ ]:


from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2, random
from PIL import Image
from matplotlib.pyplot import imshow
import json

#import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets import register_coco_instances

print("finish importing")


# # Prepare Data

# In[ ]:


'''
The file structure of the dataset
coco (DATA_ROOT)
    L modified_train2017.json
    L modified_val2017.json
    L image/
'''
DATA_ROOT = './coco'


# In[ ]:


register_coco_instances(
    "modify_coco_train", 
    {}, 
    os.path.join( DATA_ROOT, "modified_train2017.json"), 
    os.path.join( DATA_ROOT, "image")
)
#register_coco_instances("modify_coco_val"  , {}, f"{DATA_ROOT}/jmodified_val2017.json"  , f"{DATA_ROOT}/image")


# In[ ]:


with open('./modified_category.json', 'r') as f:
    NUM_CLASSES = len(json.load(f))
print(f"NUM_CLASSES = {NUM_CLASSES}")


# # Prepare for Training

# In[ ]:


from detectron2.engine import DefaultTrainer

cfg = get_cfg()
cfg.merge_from_file( model_zoo.get_config_file(  "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
"""
Model Zoo Link: 
https://github.com/facebookresearch/detectron2/blob/master/
MODEL_ZOO.md#coco-instance-segmentation-baselines-with-mask-r-cnn
"""
cfg.DATASETS.TRAIN = ("modify_coco_train",)
cfg.DATASETS.TEST  = ()
# Detectron default 4
cfg.DATALOADER.NUM_WORKERS = 4
# Detectron default 40000
cfg.SOLVER.MAX_ITER = 160_000
'''
Detectron default 
Base Learning rate 0.001
GAMMA              0.1 
STEP               (30000,)
    GAMMA : Learning rate decay factor
    STEPS: num of iter for learning rate decay by gamma
   
MASK RCNN PAPER : https://arxiv.org/pdf/1703.06870.pdf
    Base LR 0.02
    decay by 10 @ 120k/160k
    
    Cityscapes finetuning 
        Base LR 0.001
        decay by 10 @ 18k/24k
    
    update baseline
        Base LR 0.001
        decay by 10 @ 120k,160k/180k
    
    Benefit form deeper model
'''   
cfg.SOLVER.BASE_LR      = 0.001  
cfg.SOLVER.GAMMA        = 0.1 
cfg.SOLVER.STEPS        = (120_000,)
cfg.SOLVER.WEIGHT_DECAY = 0.000_1

# Detectron default 16
cfg.SOLVER.IMS_PER_BATCH = 32
# Detectron default 512
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 2048

# Number of classes 
cfg.MODEL.ROI_HEADS.NUM_CLASSES = NUM_CLASSES 

# Confident Level
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7   # set a custom testing threshold

cfg.OUTPUT_DIR = './model'
os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
#cfg.dump()


# In[ ]:


trainer = DefaultTrainer(cfg) 
trainer.resume_or_load(resume=False)
trainer.train()


# In[ ]:
from IPython import get_ipython

# Look at training curves in tensorboard:
get_ipython().run_line_magic('load_ext', 'tensorboard')
get_ipython().run_line_magic('tensorboard', '--logdir output')


# In[ ]:


from detectron2.modeling import build_model
from detectron2.checkpoint import DetectionCheckpointer
final_model = build_model(cfg)

checkpointer = DetectionCheckpointer(final_model, save_dir="model")
checkpointer.save("save_final_model") 

# secondary save cfg as pickle
import pickle
with open('model_cfg.pickle' , 'wb') as f:
    pickle.dump(cfg,f)
