T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1 - x2)**2 + (y1 - y2)**2)**0.5 # 두원의 거리 r

    if r == 0 and r1 == r2: # 두 원이 반지름이 같고 동심원일때 모든 점이 접점
        print(-1) # 모든 곳에 위치 -> -1 출력
    elif (abs(r1 - r2) == r) or (r == (r1 + r2)): # 접점이 1개인 원
        print(1) # 한점에서 만나기에 한곳에 위치 -> 1 출력
    elif abs(r1 - r2) < r < (r1 + r2): # 접점이 2개인 원
        print(2) # 두 점에서 만나기에 두곳에 위치 -> 2출력
    else:
        print(0)