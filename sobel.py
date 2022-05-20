from scipy import ndimage, misc
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# implementing the built-in sobel function
# im = Image.open("./sleep_apnea.jpg").convert('1')
# data = np.asarray(im)
# data2 = data.astype(int)

# data3 = ndimage.sobel(data)
# data4 = np.array(data3,dtype='bool')

# im2 = Image.fromarray(data4)
# fig, axs = plt.subplots(1)

# axs.imshow(im2)

# plt.show()

im = Image.open("./sleep_apnea.jpg").convert('1')
data = np.asarray(im)
data2 = data.astype(int)

# space for calculations - our own sobel function
xdir = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]

xkernel = np.asarray(xdir)
ykernel = np.transpose(xkernel)
print(xkernel)
print(ykernel)

#convolution
for i in range(len(data2)):
    datakernel = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for j in range(len(data2[i])):
        for a in range(len(datakernel)):
            for b in range(len(datakernel[a])):
                if i+a-1 < 0 or j+b-1 < 0 or i+a-1 > len(data2) - 1 or j+b-1 > len(data2[i]) - 1:
                    datakernel[a][b] = 0 
                else:
                    datakernel[a][b] = data2[i+a-1][j+b-1]
        if i == 0 and j == 0:
            print(datakernel)

# data4 = np.array(data3,dtype='bool')

# im2 = Image.fromarray(data4)
# fig, axs = plt.subplots(1)

# axs.imshow(im2)

# plt.show()