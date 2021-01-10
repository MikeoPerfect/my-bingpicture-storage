import json
from requests import get
import re
import os

def main():
    api_url = r'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    api = get(api_url)
    json_data = json.loads(api.text)
    pic_url = r'https://www.bing.com{0}'.format(json_data['images'][0]['url'])
    start_date = json_data['images'][0]['startdate']
    json_file_name = r'./json/{0}.json'.format(start_date)
    open(get_file_name(json_file_name), 'wb').write(api.content)
    print('save json file Success!')

    copy_right = json_data['images'][0]['copyright']
    pic_name = re.split(",|，", copy_right)[0]
    pic_file_name = r'./picture/{0}.png'.format(pic_name)
    pic = get(pic_url, stream=True)
    if(pic.status_code == 200):
        f = open(get_file_name(pic_file_name), 'wb')
        f.write(pic.content)
        f.close()
        print('Create Image Success!')
    else:
        print('Create Image Faild!')

def get_file_name(file_name):
    path_name = file_name
    temp = path_name
    print("v1 path_name:" + path_name)
    if os.path.isfile(file_name):
        print("exits path_name:" + file_name)
        name = file_name.split(".")
        path_name = "." + name[1] + "_1." + name[2]
        file_name = get_file_name(path_name)
    else:
        print("mkdir path_name:" + file_name)
        print("v2 path_name:" + file_name)
        return file_name
    return path_name

    

if __name__ == "__main__":
    main()