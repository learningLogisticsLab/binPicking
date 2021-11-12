#may use the command before:
#sudo apt install zip
#to install zip and unzip

import os

#download the KIT meshes from https://h2t-projects.webarchiv.kit.edu/Projects/ObjectModelsWebUI/
#to the KIT/KIT_mesh
print(os.system("./download_KIT_list.sh"))

#make dir x
print(os.system("./mkdir.sh"))

#extract and delete the .zip files
#maybe need to install the zip and unzip
#use the command:
#sudo apt install zip
print(os.system("./KIT_mesh/extract_command.sh"))

#rename x to 000_x
#set the first index @var n
n=191
f1 = open("./KIT_mesh/namelist.txt", "r")
with open("index.txt","w+") as f:
        for num in range(n,n+145):
                m=str(f1.readline())
                if num<10:
                        #print(f1.readline)
                        f.write("mv ./KIT_mesh/"+m.rstrip()+" ./KIT_mesh/00"+str(num)+'_'+m)
                elif n<100:
                        f.write("mv ./KIT_mesh/"+m.rstrip()+" ./KIT_mesh/0"+str(num)+'_'+m)
                else :
                        f.write("mv ./KIT_mesh/"+m.rstrip()+" ./KIT_mesh/"+str(num)+'_'+m)
print(os.system("./index.txt"))