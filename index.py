import uuid
import time
import random
from compress import batch_zip
fom=open("temporary-file/manifest.json","w")
time1=str(time.time()+random.random())
time2=str(time.time()+random.random())
pack_name=input("输入压缩后音乐包名")
#pack_music_path=input("输入音乐路径(必须为ogg后缀,建议使用工具转换格式,不然可能会有意想不到的bug)")
#pack_icon_path=input("输入包封面路径(默认使用default-file/pack_icon.png,若无请回车跳过,若有请自行裁剪为256×256的png文件)")
#pack_texts_zhCN=[]
pack_description=input("输入音乐包的描述(若无可直接回车跳过)")
pack_uuid1=str(uuid.uuid3(uuid.NAMESPACE_DNS,time1))
pack_uuid2=str(uuid.uuid3(uuid.NAMESPACE_DNS,time2))
s1='''{\n  "format_version": 2,\n  "header": {\n    "name": "'''+pack_name+'''",\n    "description": "'''+pack_description+'''(Pack By @BlackOrange's MPCBE).",\n    "uuid": "'''+pack_uuid1+'''",\n    "version": [1, 0, 0],\n    "min_engine_version": [ 1, 14, 51 ]\n  },\n  "modules": [\n    {\n      "type": "resources",\n      "uuid": "'''+pack_uuid2+'''",\n      "version": [1, 0, 0]\n    }\n  ]\n}'''
fom.write(s1)
batch_zip("temporary-file",pack_name)
print("音乐包已输出，请在音乐包生成器目录中查看")