from PIL import Image
import os

os.chdir(r'C:\Users\adnan\Desktop')

def convert_image(image):

    try:     
        im = Image.open(image).convert('RGB')

        image_spilt = os.path.splitext(image)[0]

        im.save(f"{image_spilt}.jpg", 'jpeg')

        print('Converting is successfuly')

    except Exception as e:
        print(f'There is wrong while converting: {e}')
   

my_image = 'test.webp'
convert_image(my_image)