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

im = Image.open("./flower.png").convert('1')
data = np.asarray(im)
data2 = data.astype(int)

# space for calculations - our own sobel function
xdir = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]

xkernel = np.asarray(xdir)
ykernel = np.transpose(xkernel)
print(xkernel)
print(ykernel)

#convolution
conv = []
for i in range(len(data2)):
    row = []
    for j in range(len(data2[i])):
        convkernel = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for a in range(3):
            for b in range(3):
                if i+a-1 < 0 or j+b-1 < 0 or i+a-1 > len(data2) - 1 or j+b-1 > len(data2[i]) - 1:
                    convkernel[a][b] = 0
                else:
                    convkernel[a][b] = data2[i+a-1][j+b-1] * xkernel[a][b]
        row.append(np.mean(convkernel))
    conv.append(row)
        # if i == 0 and j == 0:
        #     print(datakernel)

ydir = np.transpose(data2)
for i in range(len(ydir)):
    row = []
    for j in range(len(ydir[i])):
        convkernel = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for a in range(3):
            for b in range(3):
                if i+a-1 < 0 or j+b-1 < 0 or i+a-1 > len(ydir) - 1 or j+b-1 > len(ydir[i]) - 1:
                    convkernel[a][b] = 0
                else:
                    convkernel[a][b] = ydir[i+a-1][j+b-1] * xkernel[a][b]
        val = np.mean(convkernel)
        conv[j][i] = np.sqrt(np.power(conv[j][i], 2) + np.power(val, 2))

# print(conv)
data3 = np.asarray(conv)

data4 = np.array(data3,dtype='bool')

im2 = Image.fromarray(data4)
fig, axs = plt.subplots(1)

axs.imshow(im2)

plt.show()