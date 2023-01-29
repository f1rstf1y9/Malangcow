import requests


def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=46d51a41404efeaa0837c6fbe7a40257&language=ko'

    response = requests.get(URL).json()
    

    results = response.get('results')
    return len(results)
    # return(results)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
