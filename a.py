from skimage import io
from tqdm import tqdm
from os import listdir
from time import sleep
lister = listdir()
list_image = list()
for i in lister:
    if "jpg" in i: list_image.append(i)

for i in range(len(list_image)): print(f"{i+1}: {list_image[i]}")
while True:
    x = int(input("Enter number image: "))
    if x in range(len(list_image) + 1):
        image = io.imread(list_image[x - 1])
        break
    else:
        print("Error")

for d in tqdm(range(len(image))):
    for i in range(len(image[d])):
        for j in range(len(image[d][i])):
            if image[d][i][j] >= 0 and image[d][i][j] < 40: image[d][i][j] = 20
            elif image[d][i][j] >= 40 and image[d][i][j] < 80: image[d][i][j] = 60
            elif image[d][i][j] >= 80 and image[d][i][j] < 120: image[d][i][j] = 100
            elif image[d][i][j] >= 120 and image[d][i][j] < 160: image[d][i][j] = 140
            elif image[d][i][j] >= 160 and image[d][i][j] < 200: image[d][i][j] = 180
            elif image[d][i][j] >= 200 and image[d][i][j] < 240: image[d][i][j] = 220
            else: image[d][i][j] = 255
io.imshow(image)
io.show()