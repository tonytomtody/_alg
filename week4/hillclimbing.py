def hill_climbing(f,p,m,h):
    c = 0
    while (c < m):
        fxy = -f(p)
        if -f([p[0] + h, p[1]]) >= fxy:
            p = [p[0] + h, p[1]]
        elif -f([p[0] - h, p[1]]) >= fxy:
            p = [p[0] - h, p[1]]
        elif -f([p[0], p[1] + h]) >= fxy:
            p = [p[0], p[1] + h]
        elif -f([p[0], p[1] - h]) >= fxy:
            p = [p[0], p[1] - h]
        else:
            break
        c += 1
        print(f'Step {c}: f(p)={fxy:.2f} p={p}')
    return p