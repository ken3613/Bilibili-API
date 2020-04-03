import requests
import json
import time


class Api:
    def getVideoInfo(self, av=None, bv=None):
        if av:
            url = f'https://api.bilibili.com/x/web-interface/view?aid={av}'
        elif bv:
            url = f'https://api.bilibili.com/x/web-interface/view?bvid={bv}'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        response = requests.request(method='GET', url=url, headers=header).content.decode('utf-8')
        res_data = json.loads(response)['data']
        ret_dict = {
            'title': res_data['title'],
            'author': res_data['owner']['name'],
            'AV': res_data['aid'],
            'BV': res_data['bvid'],
            'pubtime': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(res_data['pubdate'])),
            'description': res_data['desc'],
            'classification': res_data['tname'],
            'copyright': bool(res_data['copyright']),
            'view': res_data['stat']['view'],
            'danmaku': res_data['stat']['danmaku'],
            'comment': res_data['stat']['reply'],
            'favorite': res_data['stat']['favorite'],
            'coin': res_data['stat']['coin'],
            'share': res_data['stat']['share'],
            'like': res_data['stat']['like']
            }
        return ret_dict


if __name__ == '__main__':
    pass
