# KIT_models_tool
This tool is written in python3, designed for downloading meshes files of KIT 3D models and creating XML files for MuJoCo engine.
-   The official websites for KIT ObjectModels Web Database is <https://h2t-projects.webarchiv.kit.edu/Projects/ObjectModelsWebUI/>

This Database contains 145 different objects meshes, you can find a namelist for this database in ./KIT_mesh/namelist.txt. Originally provided four level of resolutions(800,5k,25k and original). 
 Referenced from the official description: 
-   XXX_Orig.(obj|wrl|mdl) - this is the original resolution, usually between 200,000 and 400,000 faces
-    XXX_25k.(obj|wrl) - this is a reduced version to approximately 25,000 faces
-    XXX_5k.(obj|wrl) - this is a reduced version to approximately 5,000 faces
-    XXX_800.(obj|wrl) - this is the lowest resolution at approximately 800 faces

Notice that not all Orig resolution have _tex_.obj
We chose to use the obj file of each mesh and convert it to .stl format for MuJoCo traning. (You can also view .wrl format in FreeWRL program.)
We used part scripts from <https://github.com/doitmaan/obj2stl>

The default resolution is 25k, you can change the resolution in the `./create_stl.py` and `create_ycb_xml.py`

-Expected Free Space 7Gb.
-   open /KIT_models_tool in terminal and execute: 
  `python3 KIT_script.py`
   to download meshes from server.
-   Then 
    `python3 create_stl.py`
-    we use some Ruby scripy here, pls make sure Ruby has already been installed.
-   Then execute `python3 create_ycb_xml.py`