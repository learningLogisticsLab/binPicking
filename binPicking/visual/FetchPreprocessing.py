import os
import pickle
from PIL import Image

import numpy as np
from torch import nn 

from detectron2.engine import DefaultPredictor
import torch

################################################################
'''
README

# constructor
preprocessor = Preprocessor(
    MODEL_ROOT = '{MODEL_ROOT}'
)

# use

preprocessed_feature_vector = preprocessor( img )  
# img should have shape => ( Height, Width, Channel )


'''
################################################################
"""
MODEL_ROOT
    L model_cfg.pickle
    L {cfg.OUTPUT_DIR}
        L model_final.pth
"""

class Preprocessor(nn.modules):
    def __init__(
        self,
        MODEL_ROOT = './',
        mask_size = (128,128)
        ):
        
        # Load the config and weight of model and construct the predictor 
        with open(os.path.join(MODEL_ROOT, 'model_cfg.pickle')) as f:
            cfg = pickle.load(f)

        cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")  # path to the model we just trained
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7   # set a custom testing threshold

        self.predictor = DefaultPredictor(cfg)

        self.mask_size = mask_size

    
    ## img should have shape of ( Height, Width, Channel )
    def forward(self, img):
        instances = self.predictor(img)["instances"]
        '''
        instances.pred_boxes
            Boxes object storing N object
            instances.pred_boxes.tensor return => (N, 4) matrix

        instances.pred_classes
            shape: (N)

        instnaces.pred_mask
            shape: (N, H, W)

        instances.score
            shape: (N)
        '''
        info = torch.cat( 
        (
            instances.pred_boxes.tensor,
            instances.pred_classes.unsqueeze(1),
            instances.scores.unsqueeze(1)
        ), dim = 1)

        masks = [ 
            np.asarray(
                Image.fromarray(
                    m.detach().numpy()
                ).resize( self.mask_size )
                # tiny decision
                # .convert("RGB") can convert the mask into a RGB
            )
            for m in instances.pred_masks
        ]
        masks = torch.tensor( np.asarray(masks) , dtype = torch.uint8)
        '''
        N
            number of instances idenify in the image
        HS, WS
            pre-defined number of the resized mask, default (128,128)
        info
            tensor shape: (N, 6) <- the six dim are : (x1, y1, x2, y2, classes_id, score)
        masks
            tensor shape: (N, HS, WS)
        '''



