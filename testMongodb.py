from queryFile import *
from insertFile import *
from deleteFile import *

imagesNum = 0 # 初始图片数量，为命名做准备
# 返回数据库集合,参数：数据库名，集合名
def Login(dataBaseName, collectionName):
    myclient = pymongo.MongoClient(host='127.0.0.1', port=27017)  # 指定主机和端口号创建客户端
    mydb = myclient[dataBaseName]  # 数据库使用
    mycol = mydb[collectionName]  # 表（集合）使用

    return mycol


if __name__ == '__main__':
    imagesNum = len(os.listdir('pic')) + 1
    mycol=Login('data','picAboutNotWearHat')
    deleteAllData(mycol)
    imagesNum = insertDataAboutLocalJson(mycol, 'C:\\Users\\asus\\Desktop\\data1.json',imagesNum)
    # deleteDataAboutAllContidions(mycol,['info.img','info.video_name'],['14.jpg','test.mp4'])

    results = queryAllMessage(mycol)
    for result in results:
        print(result,'\n')