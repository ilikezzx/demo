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
# 返回全部信息
def queryAllMessage(collection):
    data = collection.find({})
    return data

# 根据某种约束条件 返回信息
def queryAllMessageAboutCondition(collection, condition, conditionData):
    data = collection.find({condition:conditionData})
    return data

# 根据年份查询
def queryAboutYear(collection,year):
    dataTimeStart = datetime(year, month, 1, 0, 0, 0)
    dataTimeEnd = datetime(year, 12, 31, 23, 59, 59)
    expression = {'time':{'$gte':str(dataTimeStart),'$lte':str(dataTimeEnd)}}
    data = collection.find(expression)
    return data

# 根据月份查询
def queryAboutMonth(collection,year,month):
    thisMonthDay = calendar.monthrange(year,month)[1]  # 算出这一月有多少天
    dataTimeStart = datetime(year,month,1,0,0,0)
    dataTimeEnd = datetime(year,month,thisMonthDay,23,59,59)
    expression = {'time':{'$gte':str(dataTimeStart),'$lte':str(dataTimeEnd)}}
    data = collection.find(expression)
    return data

# 根据日期查询
def queryAboutDay(collection,year,month,day):
    dataTimeStart = datetime(year, month, day, 0, 0, 0)
    dataTimeEnd = datetime(year, month, day, 23, 59, 59)
    expression = {'time': {'$gte': str(dataTimeStart), '$lte': str(dataTimeEnd)}}
    data = collection.find(expression)
    return data