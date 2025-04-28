# https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1
def floodFill(sr, sc, image, newColor):
    orig_color = image[sr][sc]
    if newColor == orig_color:
        return image
    rows = len(image)
    cols = len(image[0])

    def fillColor(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != orig_color:
            return

        image[r][c] = newColor
        fillColor(r + 1, c)
        fillColor(r - 1, c)
        fillColor(r, c + 1)
        fillColor(r, c - 1)
    fillColor(sr, sc)
    return image


sr = 6
sc = 3
newColor = 1
image = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 0],
    [1, 0, 1, 1]
]
result = floodFill(sr, sc, image, newColor)
print(result)