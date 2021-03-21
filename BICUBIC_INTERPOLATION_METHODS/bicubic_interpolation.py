import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import imageio
import time as tim


######################################################
# .......Enter new image scaling value.......
Scaling_factor = 4 #  It must be in order of 2, 4, 8, 16 etc..

######################################################
#............ Enter image adress.............
Xorig = img.imread('test-images/Low_Res_bird.jpg')



start_time = tim.time()
X = Xorig
ny,nx,nz = X.shape
new_size = Scaling_factor*2

r,c,s= X.shape
X1 = np.zeros(X.shape)
for i in range(s):
    X1[:,:,i] = X[:,:,i]


for t in range(int(new_size/4)):
    r,c,s= X1.shape
    X2=np.zeros((r*2,c*2,s))
    for k in range(s):
        for i in range(r):
            for j in range(c):
                X2[:,:,k].flat[(c*2*i*2)+j*2] = X1[:,:,k].flat[(c*i)+j]
    X1 = np.zeros(X2.shape)
    for q in range(s):
        X1[:,:,q] = X2[:,:,q]
                
condi = True
count = 1
while condi:
    X1_ny, X1_nx, X1_nz = X1.shape
    X2=np.zeros((X1_ny+2,X1_nx+2,X1_nz))
    for i in range(nz):
        X2[:,:,i] = np.pad(X1[:,:,i], [(1, 1), (1, 1)], mode='constant')
    X3 = X1
    zero_num = (X1 == 0).astype(int)
    if 0 < np.sum(zero_num):
        print('Iteration number: ', count)
        count += 1
        for channel in range(nz):
            for i in range(len(X2[:,0,channel])-2):
                for j in range(len(X2[0,:,channel])-2):
                    r = i+1
                    c = j+1
                    #if (X2[r,c,channel] == 0):
                    mean = 0
                    k = 0
                    if (X2[r-1,c-1,channel] != 0):
                        mean += X2[r-1,c-1,channel]
                        k += 1
                    if (X2[r-1,c,channel] != 0):
                        mean += X2[r-1,c,channel]
                        k += 1
                    if (X2[r-1,c+1,channel] != 0):
                        mean += X2[r-1,c+1,channel]
                        k += 1
                    if (X2[r,c-1,channel] != 0):
                        mean += X2[r,c-1,channel]
                        k += 1
                    if (X2[r,c+1,channel] != 0):
                        mean += X2[r,c+1,channel]
                        k += 1
                    if (X2[r+1,c-1,channel] != 0):
                        mean += X2[r+1,c-1,channel]
                        k += 1
                    if (X2[r+1,c,channel] != 0):
                        mean += X2[r+1,c,channel]
                        k += 1
                    if (X2[r+1,c+1,channel] != 0):
                        mean += X2[r+1,c+1,channel]
                        k += 1
                    if (k != 0):
                        mean = mean / k
                        X1[i,j,channel] = mean
    else:
        condi=False

Execution_time = int(np.round(tim.time()-start_time))
print("Shape of Original Image: ",X.shape)
print("Shape of New Image     : ",X1.shape)
print("Scaling factor         : ",new_size)
print('Execution time         :  {} sec'.format(Execution_time))

        
fig, axs = plt.subplots(1, 2,figsize=(15,10))
axs[0].imshow(X)
axs[0].title.set_text("Original Image")
axs[0].axis('off')
#axs[1].imshow(X1)
axs[1].imshow((X1).astype(np.uint8))
axs[1].title.set_text("New Image formed with {} times scaling".format(new_size/2))
axs[1].axis('off')
imageio.imwrite('New_Image.jpg', (X1).astype(np.uint8))
