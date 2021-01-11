import cv2

IMAGE = "girl.jpg"
OUT_IMAGE = "girl_circle.jpg"

def draw_circle(image,
              center_x,
              center_y,
              radius_px,
              size=0.01, # -1: filled
              color_bgr=[255, 0, 0],
              line_type=cv2.LINE_AA,
              is_copy=True):
    
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
    x_abs = int(center_x * w)
    y_abs = int(center_y * h)
    
    # docs: https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670
    cv2.circle(img=image,
            center=(x_abs, y_abs),
            radius=radius_px,
            color=color_bgr,
            thickness=thickness,
            lineType=line_type,
            shift=0)
    return image

def main():
    img = cv2.imread(IMAGE)
    img_circle = draw_circle(image=img,
                             center_x=0.45,
                             center_y=0.35,
                             radius_px=150,
                             color_bgr=[0, 0, 255],
                             size=0.005,
                             is_copy=True)
    img_circle = draw_circle(image=img_circle,
                             center_x=0.77,
                             center_y=0.23,
                             radius_px=30,
                             size=0.007,
                             color_bgr=[0, 255, 255],
                             is_copy=False)
    cv2.imwrite(OUT_IMAGE, img_circle)
    print("Done drawing circle @ %s" % OUT_IMAGE)

if __name__ == "__main__":
    main()
    print('* Follow me @ ' + "\x1b[1;%dm" % (34) + ' https://www.facebook.com/kyznano/' + "\x1b[0m")
    print('* Minh fanpage @ ' + "\x1b[1;%dm" % (34) + ' https://www.facebook.com/minhng.info/' + "\x1b[0m")    
    print('* Join GVGroup @ ' + "\x1b[1;%dm" % (34) + 'https://www.facebook.com/groups/ip.gvgroup/' + "\x1b[0m")    
    print('* Thank you ^^~')