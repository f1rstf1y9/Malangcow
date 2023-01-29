import requests
from pprint import pprint


def recommendation(title):
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=46d51a41404efeaa0837c6fbe7a40257&language=ko&query={title}&page=1&include_adult=false'
    response = requests.get(URL).json()
    results = response.get('results')
    if results:
        first_id = results[0]['id']
    else:
        return None
            

    URL_1 = f'https://api.themoviedb.org/3/movie/{first_id}/recommendations?api_key=46d51a41404efeaa0837c6fbe7a40257&language=ko'
    response_1 = requests.get(URL_1).json()
    results_1 = response_1.get('results')
    title_list = []
    if not(results_1):
        return '[]'
    else:
        for movie in results_1:
            title_list.append(movie['title'])  
        return title_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
