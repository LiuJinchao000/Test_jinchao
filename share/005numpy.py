import numpy as np
objp = np.zeros((3,4), np.float32)
#objp[:, :2] = np.mgrid[0:1, 0:3].T.reshape(-1, 2)
b=np.reshape(objp,12)
print(b)