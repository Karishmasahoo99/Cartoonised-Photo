import os
import cv2

codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'generated'))

def process(ip_image):
     ip_image=cv2.GaussianBlur(ip_image,(5,5),170,180)
     ip_image=cv2.stylization(ip_image,sigma_s=90,sigma_r=0.1)
     #sketch_gray,sketch_color=cv2.pencilSketch(ip_image,sigma_s=100,sigma_r=0.05,shade_factor=0.09)
     return ip_image
    
def main():
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        cartoon_image = process(ip_image)
        ## saving the output in  an image of said name in the Generated folder
        cv2.imwrite(generated_folder_path+"/"+"cartoonised " + image_name, cartoon_image)
        
if __name__=='__main__':
    main()