import numpy as np
class Sobel(object):
    def sobel(self,arr):
        rgb_arr = self.rgb2gray(arr)
        return self.sobel_ex(rgb_arr)

    def sobel_ex(self,arr):
        result = np.empty(shape=arr.shape)
        fx = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
        fy = fx.transpose()
        i_dim = arr.shape
        for x in range(i_dim[0]-2):
            for y in range(i_dim[1]-2):
                # you had to think with space way
                sx = sum(sum(arr[x:x+3,y:y+3] * fx))
                sy = sum(sum(arr[x:x+3,y:y+3] * fy))
                result[x,y] = np.sqrt(sx**2 + sy**2)
        return result

    def rgb2gray(self,arr):
        value = 0.299*arr[:,:,0] + 0.587*arr[:,:,1] + 0.114*arr[:,:,2]
        return value
