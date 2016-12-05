# coding: utf-8

# In[ ]:

from random import random

import pymongo
import numpy as np
import pandas as pd

_client = pymongo.MongoClient('localhost', 27017)
_db = _client['thalamus-4']

def getInterviewArchive():
    return _db.interview_archive

def setPlotly():
    import plotly
    plotly.offline.init_notebook_mode(connected=True)
    from plotly.graph_objs import Box, Histogram, Layout, Figure, Bar, Scatter, Marker
    return plotly, Box, Histogram, Layout, Figure, Bar, Scatter, Marker

allowedStatus = ["abandoned", "completed", "exitPointAbandoned", "rejected", "scheduleCompleted", "scheduleRejected", "startedEpilogue"]
allowedDomains = {'greenville': ["-greenville-smartexam-com-443", "greenville-smartexam-com-443"]}

