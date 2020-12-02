import os
import pytest 
import matplotlib.pyplot as plt
from configeditor.configeditor import ConfigEditor

testdir = os.path.realpath(os.path.dirname(__file__))
rootdir = os.path.dirname(testdir)


testvideopath = os.path.join(testdir,"test_fixtures/test_video.mpg")
test1configpath = os.path.join(testdir,"test_fixtures/test1config.yaml") 
test2configpath = os.path.join(testdir,"test_fixtures/test2config.yaml") 

class Test_ConfigEditor():
    def test_ConfigEditor(self):
        ConfigEditor(testvideopath,test1configpath,savepath = testdir)
    def test_ConfigEditor_visualize_config1(self):
        ce = ConfigEditor(testvideopath,test1configpath,savepath = testdir)
        ce.visualize_config()
    def test_ConfigEditor_visualize_config2(self):
        ce = ConfigEditor(testvideopath,test2configpath,savepath = testdir)
        ce.visualize_config()
    def test_ConfigEditor_draw_rectangle(self):
        fig,ax = plt.subplots()
        ce = ConfigEditor(testvideopath,test1configpath,savepath = testdir)
        ce.draw_rectangle(ax,(10,10),10,10,1,"red")
        ax.set_xlim(0,20)
        ax.set_ylim(0,20)
        plt.savefig(os.path.join(testdir,"test_ConfigEditor_visualize_config.png"))


