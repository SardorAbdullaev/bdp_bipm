import pickle
import pandas as pd
from scipy import misc
import urllib.request
import os
import io
import time


target_column = "auto_category_id"

limit_for_each_category = 2000

processed_images_column = "processed_images"

all_images_by_category = pd.read_pickle("all_images_by_category.pkl")

errors = 0
for folderName,imageUrls in all_images_by_category[processed_images_column].items():
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    for i,url in enumerate(imageUrls[:limit_for_each_category]):
        try:
            urllib.request.urlretrieve(url, folderName+"/image"+str(i)+".jpg")
        except:
            errors += 1
            print("Couldn't load ",url)

print(errors, " loading errors detected!")

