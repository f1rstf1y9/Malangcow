import requests
from pprint import pprint


def credits(title):
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=46d51a41404efeaa0837c6fbe7a40257&language=ko&query={title}&page=1&include_adult=false'
    response = requests.get(URL).json()
    results = response.get('results')
    if results:
        first_id = results[0]['id']
    else:
        return None
    URL_1 = f'https://api.themoviedb.org/3/movie/{first_id}/credits?api_key=46d51a41404efeaa0837c6fbe7a40257&language=ko'
    response_1 = requests.get(URL_1).json()
    results_1 = response_1.get('cast')
    cast_direc = {}
    cast = []
    direc = []
    for i in results_1:
        if i['cast_id'] < 10:
            cast.append(i['name'])
    results_2 = response_1.get('crew')
    for i in results_2:
        if i['department'] == 'Directing':
            if i['name'] not in direc:
                direc.append(i['name'])
    cast_direc = { 
        'cast' : cast, 
        'directing' : direc
        }
    return cast_direc
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
