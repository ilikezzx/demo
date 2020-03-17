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

# 插入数据
def insertData(collection, newJsonData):
    collection.insert_many(newJsonData)

def insertOneData(collection,newJsonData):
    collection.insert_one(newJsonData)

# 根据本地文件 插入其中的json数据
def insertDataAboutLocalJson(collection, jsonUrl,imagesNum):
    items=[]
    plt.axis('off')
    with open(jsonUrl, 'r', encoding='utf-8')as f:
        for item in f.readlines():
            items.append(json.loads(item))

    for i,item in enumerate(items):
        print(i,"正在输入,共",len(items),"个")

        # 更改数据 img
        data = loads(json.dumps(item))
        ByteImage = data['info']['img']
        ArrayImage = pickle.loads(ByteImage)

        plt.imshow(ArrayImage)
        plt.savefig('pic/%d.jpg' % (imagesNum))
        data['info']['img']=str("%d.jpg" % imagesNum)
        imagesNum += 1                                  # 命名数更改

        item.pop('_id', None)  # 删除id，为转化json做准备
        insertOneData(collection, data)                 # 插入数据

        # 更新图片命名数
        return imagesNum
