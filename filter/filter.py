from PIL import Image
import sys

img = Image.open(sys.argv[1])
pix = img.load()
width, height = img.size

img.show()
pix_matrix = []

for i in range(0, width):
    line = []
    for j in range(0, height):
        line.append(pix[i, j])

    pix_matrix.append(line)

kernel = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]

mp = {}

def GetMatrix(pixels, x, y):
    matrix = []

    for i in range(-1, 2):
        matrix.append(pixels[x+i][y-1:y+2])

    return matrix

def Convolution(matrix):
    result = [0, 0, 0]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(result)):
                result[k] += matrix[i][j][k] * kernel[i][j]

    return tuple(result)



for i in range(1, width-1):
    for j in range(1, height-1):
        matrix = GetMatrix(pix_matrix, i, j)
        pix[i, j] = Convolution(matrix)


img.save("with_filter.jpg")

img.show()

