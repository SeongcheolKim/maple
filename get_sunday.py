import requests
from bs4 import BeautifulSoup

def get_sunday_maple_image_url():
    api_keys = 'live_2cde2f31943bfe968c9af85f768c0c185cc8407c98376dc9c288ea533c166ca90eeac3677a8c437c7c7f3ce2716d8a2c'
    base_url = 'https://open.api.nexon.com/maplestory'
    endpoint = '/v1/notice-event'
    url = base_url + endpoint
    headers = {'x-nxopen-api-key': api_keys}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        sunday_maple_id = None
        for notice in data['event_notice']:
            if '썬데이 메이플' in notice['title']:
                sunday_maple_id = notice['notice_id']
                break
        
        if sunday_maple_id:
            detail_endpoint = '/v1/notice-event/detail'
            detail_url = base_url + detail_endpoint
            params = {'notice_id': sunday_maple_id}

            detail_response = requests.get(detail_url, headers=headers, params=params)

            if detail_response.status_code == 200:
                detail_data = detail_response.json()
                soup = BeautifulSoup(detail_data['contents'], 'html.parser')
                images = soup.find_all('img')
                return [image['src'] for image in images]
            else:
                return detail_response.status_code
        else:
            raise ValueError("썬데이 메이플 이벤트를 찾을 수 없습니다.")
    else:
        return response.status_code


