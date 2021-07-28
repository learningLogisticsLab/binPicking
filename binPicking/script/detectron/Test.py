# In[]
# import some common libraries
import numpy as np
import os, json, cv2, random, pickle
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

# In[ ]:


## load the model and the weight
"""
MODEL_ROOT
    L model_cfg.pickle
    L {cfg.OUTPUT_DIR}
        L model_final.pth
"""
MODEL_ROOT = './'
cfg = {}
with open('model_cfg.pickle' , 'rb') as f:
    cfg = pickle.load(f)

print(cfg.OUTPUT_DIR)

cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")  # path to the model we just trained
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7   # set a custom testing threshold
predictor = DefaultPredictor(cfg)


# In[ ]:


pic = np.asarray(Image.open('name_0.png'))
imshow(pic)
#pic = pic.transpose((2,0,1))
print(pic.shape)


# In[ ]:


outputs = predictor(pic)
# look at the outputs. See https://detectron2.readthedocs.io/tutorials/models.html#model-output-format for specification
print(outputs["instances"].pred_classes)
print(outputs["instances"].pred_boxes)
print(outputs['instances'])


# In[1]:


# We can use `Visualizer` to draw the predictions on the image.
v = Visualizer(pic[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
imshow(out.get_image()[:, :, ::-1])
im = Image.fromarray(out)
out.save('output_name_0.jpg')
