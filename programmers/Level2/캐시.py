def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    
    if cacheSize == 0:
        return 5 * len(cities) # 캐시사이즈 0인 경우 존재. 다 miss 처리해줌.
    
    for city in cities:
        city = city.lower() # 대소문자 구분을 하지 않는다. 라는 조건 존재

        if city in cache: # 이미 캐시에 존재하면 최근(맨 뒤)으로 이동
            cache.remove(city)
            cache.append(city)
            answer += 1
        elif len(cache) < cacheSize: # 캐시 사이즈 아직 여유 있으면 그냥 추가
            cache.append(city)
            answer += 5
        else: # 제일 먼저 들어온(사용한지 오래된) 애 캐시에서 제거후 추가
            cache.pop(0)
            cache.append(city)
            answer += 5
    
    return answer