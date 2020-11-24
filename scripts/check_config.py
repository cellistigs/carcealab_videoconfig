import sys
from configeditor.configeditor import ConfigEditor
## Script to check the current config file settings.
## This script takes three paths as input: 
### 1. The path to the video we want to analyze. 
### 2. The path to the config file corresponding to that video. 
### 3. The path to directory where images will be saved for checking. 

if __name__ == "__main__":
    videopath = sys.argv[1]
    configpath = sys.argv[2]
    savepath = sys.argv[3]
    ce = ConfigEditor(videopath,configpath,savepath)
    ce.visualize_config()

    

