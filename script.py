import requests
import sys, time
import shutil

def get_image(url, filename):
    with open(filename, 'wb') as file, \
        requests.get(url, stream=True) as response:
        shutil.copyfileobj(response.raw, file)

def download(input_file, output_path=''):
    """input_file='/home/user/Pictures/images.txt'
       output_path='/home/user/Pictures/'
    """
    with open(input_file, 'r') as file:
        index = 1
        for url in file:
            output_file = output_path + f"image-{index}.jpg"
            get_image(str(url).rstrip(), output_file)

            index += 1

if __name__ == '__main__':
    download('images.txt')
