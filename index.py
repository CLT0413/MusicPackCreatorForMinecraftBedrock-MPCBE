import uuid
from compress import batch_zip
fom=open("temporary-file/manifest.json","w")
pack_name=input("输入压缩后音乐包名")
#pack_path=input("输入音乐路径(必须为ogg后缀,建议使用工具转换格式,不然可能会有意想不到的bug)")
pack_description=input("输入音乐包的描述(若无可直接回车跳过)")
pack_uuid1=str(uuid.uuid3(uuid.NAMESPACE_X500,"0123456789abcdefghijklmnopqrstuvwxyz"))
pack_uuid2=str(uuid.uuid3(uuid.NAMESPACE_X500,"0123456789abcdefghijklmnopqrstuvwxyz"))
s1='''{\n  "format_version": 2,\n  "header": {\n    "name": "'''+pack_name+'''",\n    "description": "'''+pack_description+'''(Pack By @BlackOrange's MPCBE).",\n    "uuid": "'''+pack_uuid1+'''",\n    "version": [1, 2, 2],\n    "min_engine_version": [ 1, 14, 51 ]\n  },\n  "modules": [\n    {\n      "type": "resources",\n      "uuid": "'''+pack_uuid2+'''",\n      "version": [1, 2, 2]\n    }\n  ]\n}'''
fom.write(s1)
batch_zip("temporary-file",pack_name)
print("音乐包已输出，请在音乐包生成器目录中查看")