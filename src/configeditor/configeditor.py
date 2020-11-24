import os
import yaml
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip

class ConfigEditor():
    """Object class to hold configuration data. Assumes a video that we want to analyze, and can be initalized from a file. Will assume yaml format. 
    """
    def __init__(self,videopath,configpath):
        """Initialize objects with the paths: videopath, configpath. 

        """
        ## First clean the videopath:
        assert os.path.exists(videopath),"No file can be found at location {}".format(videopath)
        try:
            self.clip = VideoFileClip(self.videopath)
        except Exception:
            print("This file could not be loaded as a video.")
            raise
        self.videopath = videopath

        ## Now clean the yaml path:
        assert os.path.exists(configpath),"No file can be found at location {}".format(configpath)
        try:
            with open(configpath) as f:
                config = yaml.full_load(f)
                self.config = config 
        except Exception:
            print("This file could not be loaded as a config file.")
            raise

    def visualize_config(self,frame = 0):
        """

        """

        






