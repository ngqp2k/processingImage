import cv2

IMAGE = "girl.jpg"
OUT_IMAGE = "girl_rect.jpg"

def draw_rect(image,
              x_from,
              y_from,
              x_to,
              y_to,
              color_bgr=[255, 0, 0], 
              size=0.01, # 1%
              line_type=cv2.LINE_AA,
              is_copy=True):
    assert size > 0
    
    image = image.copy() if is_copy else image # copy/clone a new image
    
    # calculate thickness
    h, w = image.shape[:2]
    if size > 0:        
        short_edge = min(h, w)
        thickness = int(short_edge * size)
        thickness = 1 if thickness <= 0 else thickness
    else:
        thickness = -1
    
    # calc x,y in absolute coord
    x_from_abs = int(x_from * w)
    y_from_abs = int(y_from * h)
    x_to_abs = int(x_to * w)
    y_to_abs = int(y_to * h)
    
    # docs: https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga07d2f74cadcf8e305e810ce8eed13bc9
    cv2.rectangle(img=image,
            pt1=(x_from_abs, y_from_abs),
            pt2=(x_to_abs, y_to_abs),
            color=color_bgr,
            thickness=thickness,
            lineType=line_type,
            shift=0)
    return image

def main():
    img = cv2.imread(IMAGE)
    img_rect = draw_rect(image=img,
                         x_from=0.25,
                         y_from=0.10,
                         x_to=0.61,
                         y_to=0.60,
                         color_bgr=[0, 0, 255],
                         is_copy=True)
    img_rect = draw_rect(image=img_rect,
                         x_from=0.70,
                         y_from=0.12,
                         x_to=0.85,
                         y_to=0.35,
                         size=0.005,
                         color_bgr=[0, 255, 255],
                         is_copy=False)
    cv2.imwrite(OUT_IMAGE, img_rect)
    print("Done drawing rect @ %s" % OUT_IMAGE)

if __name__ == "__main__":
    main()
    print('* Follow me @ ' + "\x1b[1;%dm" % (34) + ' https://www.facebook.com/kyznano/' + "\x1b[0m")
    print('* Minh fanpage @ ' + "\x1b[1;%dm" % (34) + ' https://www.facebook.com/minhng.info/' + "\x1b[0m")    
    print('* Join GVGroup @ ' + "\x1b[1;%dm" % (34) + 'https://www.facebook.com/groups/ip.gvgroup/' + "\x1b[0m")    
    print('* Thank you ^^~')
