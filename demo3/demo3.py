

def mathc_img(Target,value):
    import cv2
    import numpy as np
    from PIL import ImageGrab
    from PIL import Image
    import pyautogui
    
    img_rgb = np.array(ImageGrab.grab()) #PIL截图获取
    #img_rgb = cv2.imread(image) #载入图像
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    print(int(loc[1][0]), int(loc[0][0])) #定位的左上角
    im = Image.open(Target)
    a=int(loc[1][0])+im.size[0]//2 
    b=int(loc[0][0])+im.size[1]//2 
    print("坐标：",a,b) 
    pyautogui.moveTo(a,b)

    #标记框
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)   
    # cv2.imshow('Detected',img_rgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

Target=('target.png')
value=0.9
mathc_img(Target,value)
