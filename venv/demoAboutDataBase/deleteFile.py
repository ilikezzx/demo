import pymongo
import json
from PIL import Image
from io import BytesIO,StringIO
import pickle
from bson.json_util import dumps,loads
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
import calendar

# 删除一个数据，根据时间
def deleteDataAboutTime(collection,time):
    deleteData={"time":time}
    collection.delete_many(deleteData)

# 删除所有数据
def deleteAllData(collection):
    collection.delete_many({})

# 删除数据，根据视频源
def deleteDataAboutVideoName(collection,video_name):
    deleteData = {"info.video_name":video_name}
    collection.delete_many(deleteData)

# 删除数据根据任意条件
def deleteDataAboutAllContidions(collection, contidions,contidionsData):
    expression = {}
    for i,contidion in enumerate(contidions):
        expression.setdefault(contidion,contidionsData[i])

    collection.delete_many(expression)