file = open('input.txt', 'r')
pts = [[int(x) for x in line.rstrip().split(',')] for line in file]

edges = []
for i in range(len(pts)):
    pt1 = pts[i-1]
    pt2 = pts[i]
    edges.append((pt1, pt2))


# geometry magic
# https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
# https://silentmatt.com/rectangle-intersection/
def overlaps(r1, r2):
    if r1 == r2:
        return False
    r1_max_x, r1_min_x = max(r1[0][1], r1[1][1]), min(r1[0][1], r1[1][1])
    r2_max_x, r2_min_x = max(r2[0][1], r2[1][1]), min(r2[0][1], r2[1][1])
    r1_max_y, r1_min_y = max(r1[0][0], r1[1][0]), min(r1[0][0], r1[1][0])
    r2_max_y, r2_min_y = max(r2[0][0], r2[1][0]), min(r2[0][0], r2[1][0])
    overlaps =  (
        r1_min_x < r2_max_x and
        r1_max_x > r2_min_x and
        r1_min_y < r2_max_y and
        r1_max_y > r2_min_y
    )
    return overlaps

area = 0
for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
        rect = (pts[i], pts[j])

        has_overlap = any(overlaps(edge, rect) for edge in edges)
        if not has_overlap:
            s1 = abs(pts[i][0] - pts[j][0]) + 1
            s2 = abs(pts[i][1] - pts[j][1]) + 1
            area = max(s1 * s2, area)
        
print(area)