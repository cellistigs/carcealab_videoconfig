import pytest 
from configeditor.configeditor import ConfigEditor

testvideopath = "/Volumes/TOSHIBA EXT STO/TempTrial2.mpg"
testconfigpath = "~/Downloads/TempTrial27config.yaml"

class Test_ConfigEditor():
    def test_ConfigEditor(self):
        ConfigEditor(testvideopath,testconfigpath)

