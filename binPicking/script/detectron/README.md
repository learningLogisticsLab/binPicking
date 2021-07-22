# Train Model for visual 
## 1. Download the COCO dataset
Download dataset: https://cocodataset.org/#download

download 

- 2017 Train images[118K/18GB]
- 2017 Train/Val annotations [241MB]

save the file in structure

    coco (DATA_ROOT)
        L instances_train2017.json
        L instance_val2017.json
        L image/

## 2. Preprocess the Data 
open the 'Preprocess_Data.ipynb' notebook

update the ```DATA_ROOT```  and ```PROPRECRESS_DATA_ROOT```

run the notebook and preprocess the COCO data to strip all useless classes' annotation.

## 3. Train the pretrain Model on the modified COCO data
install ```cuda, torch, detectron2```

Detectron2: https://detectron2.readthedocs.io/en/latest/tutorials/install.html#install-pre-built-detectron2-linux-only

update the ```DATA_ROOT```

run the notebook to train the model.