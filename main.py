import json
from requests import get

def main():
    api_url = r'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    api = get(api_url)
    json_data = json.loads(api.text)
    pic_url = r'https://www.bing.com{0}'.format(json_data['images'][0]['url'])
    start_date = json_data['images'][0]['startdate']

    open(r'./json/{0}.json'.format(start_date), 'wb').write(api.content)
    print('save json file Success!')
    copy_right = json_data['images'][0]['copyright']
    name = copyright.split("，")[0]
    pic = get(pic_url, stream=True)
    if(pic.status_code == 200):
        open(r'./picture/{0}.png'.format(name), 'wb').write(pic.content)
        print('Create Image Success!')
    else:
        print('Create Image Faild!')

if __name__ == "__main__":
    main()