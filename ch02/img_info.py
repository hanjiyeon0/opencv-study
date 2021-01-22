import cv2

img1 = cv2.imread('assets/jjeong.jpeg', cv2.IMREAD_GRAYSCALE) 
img2 = cv2.imread('assets/miru2.jpeg', cv2.IMREAD_COLOR)

print('type(img1):', type(img1)) # type(img1): <class 'numpy.ndarray'>
print('img1.shape:', img1.shape) # img1.shape: (480, 640) 
print('img2.shape:', img2.shape) # img2.shape: (480, 640, 3) 
print('img2.dtype:', img2.dtype) # img2.dtype: uint8

h, w = img2.shape[:2] # h: 480, w: 640 
print('img2 size: {} x {}'.format(w, h))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3: 
    print('img1 is a truecolor image')
 