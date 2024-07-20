import os
import shutil


rewritten_folder = "blog/static/images/art"

file_names = os.listdir("blog/static/images/art-rewritten")
source_folder= "blog/static/images/art"
destination_folder= "blog/static/images/art-rewritten"
print(file_names)
count = 0

for name in file_names:
    # shutil.copy(f'{source_folder}/{name}', f'{destination_folder}/{count}.jpg')
    print(f'![my art work](/images/art-rewritten/{count}.jpg)\n\n')
    count += 1
