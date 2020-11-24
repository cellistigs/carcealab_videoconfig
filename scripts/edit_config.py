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
    var = "edit"
    print("Initial image saved: You can now edit and save the config file in a code browser. Once config is edited, type 'edit' to update the image. Otherwise, type anything else to quit.")
    while var == "edit":
        ce.visualize_config()
        print("Update image? (edit/done)")
        var = input()
        print("You typed {}. Taking appropriate action.".format(var))
    print("ending script.")


    

