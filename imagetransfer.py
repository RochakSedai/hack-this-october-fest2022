import os
import shutil

source_path = r"D:\Major Project on CBIR and Recommendation\New Dataset\category_data - Copy"
destination_path = r"D:\Major Project on CBIR and Recommendation\New Dataset\images"


for files in os.listdir(source_path):
    if files.endswith('.jpg' or '.JPG'):
        src_path = os.path.join(source_path, files)
        dst_path = os.path.join(destination_path, files)
        shutil.move(src_path, dst_path)