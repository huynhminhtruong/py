if __name__ == '__main__':
    x, y = map(int, input().split())
    y -= 1
    print("YNEOS"[y < 0 or y > x or (y == 0 and x != 0) or (x - y) % 2::2])