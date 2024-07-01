def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_symmetric_pascals_triangle(rows):
    triangle = generate_pascals_triangle(rows)
    max_width = len(" ".join(map(str, triangle[-1]))) 
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

print_symmetric_pascals_triangle(8)

def pascalsTri(r):
    tri = []
    
    for row in range(r):
        line = 8**row
        
        listLine = list(str(line))
        tri.append(listLine)

        # print(tri)
    return tri

def pspt(r):
    triangle = pascalsTri(r)
    max_width = len(" ".join(map(str, triangle[-1]))) 
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))
    return " "