import zipfile # 导入zipfile,这个是用来做压缩和解压的Python模块；
import os 
import time

def batch_zip(start_dir,zip_file):
    # start_dir要压缩的文件路径
    # zip_file 输出zip文件的路径
    zip_file = zip_file + '.mcpack'
    z = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    print(z)
    for path, dirname, file_name in os.walk(start_dir):
#         print("文件夹根路径：", path)
        fpath = path.replace(start_dir, '') # 去除根路径名称
#         print("--去除根路径：", fpath)
        fpath = fpath and fpath + os.sep   # 在原fpath加上\
#         print("****去除根路径+\ ：", fpath)

        for filename in file_name: # 逐个循环读取文档名称
#             print('--', fpath+filename)
#             fpath + filename完整构成每个文档的去根绝对路径
#             s = os.path.join(path, filename)   # 补齐全部的绝对路径
#             print('*-*',s)

            z.write(os.path.join(path, filename), fpath + filename) # 实现在输出路径的Zip压缩操作
    z.close()
    return zip_file