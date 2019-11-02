import requests
import sys
import shutil

def download(input_file, output_path=''):
    """ input_file='/home/user/Pictures/images.txt'
        output_path='/home/user/Pictures' """
    with open(input_file, 'r') as file:
        index = 1
        for url in file:
            output_file = f"image-{index}.jpg"
            if output_path:
                output_file = output_path + '/' + output_file
            # get_image(str(url).rstrip(), output_file)
            with open(output_file, 'wb') as file, \
                requests.get(str(url).rstrip(), stream=True) as response:
                shutil.copyfileobj(response.raw, file)

            index += 1

if __name__ == '__main__':
    download('images.txt')
