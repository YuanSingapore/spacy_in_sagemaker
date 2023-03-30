import argparse
import os
import subprocess
import shutil
import spacy

#list_files = subprocess.run(["ls", "-l"])
print("gpu? ",spacy.prefer_gpu())

#print("nvidia-smi",subprocess.run(["nvidia-smi"]))



if __name__ =='__main__':

    spacy.prefer_gpu()
    subprocess.run("pwd")
    dir='.'
    os.listdir('.')
    
   # export GPU_ID=1
    # prepare the environment for training 
    subprocess.run(["python3", "-m", "spacy", "project", "run", "all"])
    
    ## run spaCy training pipeline
    #subprocess.run("python", "-m", "spacy", "project", "run", "preprocess")
    
    #print("preprocess finished! the model is saved in: ", os.listdir("/opt/ml/data/training/UD_English-EWT")  )
    # os.listdir('./')
    # for dirpath, dirs, files in os.walk(dir):	 
    #     path = dirpath.split('/')
    #     print('|', '-', '[',os.path.basename(dirpath),']')
    #     for f in files:
    #         print('|', '-'+'-', f)
    ## save the model 
    
    src='/opt/ml/code/packages/en_ud_en_ewt-0.0.0/dist/en_ud_en_ewt-0.0.0.tar.gz'
    dst='/opt/ml/model/en_ud_en_ewt-0.0.0.tar.gz'
    shutil.copyfile(src, dst)
    print("copy finished")
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    