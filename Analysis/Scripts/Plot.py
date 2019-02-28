#create full files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import ROOT
import sys

Rootfile = ROOT.TFile.Open("~/Desktop/plot.root", "rw")
Canvas = Rootfile.Get("Canvas/data_4041-1")
Canvas.SaveAs("Test.png")






