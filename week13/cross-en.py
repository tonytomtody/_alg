from math import log2

def greedy(f,p,q,m,h):
    c = 0
    while (c < m):
        fxy = -f(p,q)
        fxyp1 = -f(p,genpq1(q,h))
        fxyp2 = -f(p,genpq2(q,h))
        fxyp3 = -f(p,genpq3(q,h))
        fxym1 = -f(p,genmq1(q,h))
        fxym2 = -f(p,genmq2(q,h))
        fxym3 = -f(p,genmq3(q,h))
        if fxyp1 >= fxy and fxyp1 >= fxyp2 and fxyp1 >= fxyp3 and fxyp1 >= fxym1 and fxyp1 >= fxym2 and fxyp1 >= fxym3:
            q = genpq1(q,h)
        elif fxyp2 >= fxy and fxyp2 >= fxyp1 and fxyp2 >= fxyp3 and fxyp2 >= fxym1 and fxyp2 >= fxym2 and fxyp2 >= fxym3:
            q = genpq2(q,h)
        elif fxyp3 >= fxy and fxyp3 >= fxyp1 and fxyp3 >= fxyp2 and fxyp3 >= fxym1 and fxyp3 >= fxym2 and fxyp3 >= fxym3:
            q = genpq3(q,h)
        elif fxym1 >= fxy and fxym1 >= fxyp1 and fxym1 >= fxyp2 and fxym1 >= fxyp3 and fxym1 >= fxym2 and fxym1 >= fxym3:
            q = genmq1(q,h)
        elif fxym2 >= fxy and fxym2 >= fxyp1 and fxym2 >= fxyp2 and fxym2 >= fxyp3 and fxym2 >= fxym1 and fxym2 >= fxym3:
            q = genmq2(q,h)
        elif fxym3 >= fxy and fxym3 >= fxyp1 and fxym3 >= fxyp2 and fxym3 >= fxyp3 and fxym3 >= fxym1 and fxym3 >= fxym2:
            q = genmq3(q,h)
        else:
            break
        c += 1
        print(f'Step {c}: f(p,q)={fxy:.2f} q={q}')
    print('Final q:', q)

def genpq1(q,h):
    q = [q[0]+h, q[1]-(h/2), q[2]-(h/2)]
    return q

def genpq2(q,h):
    q = [q[0]-(h/2), q[1]+h, q[2]-(h/2)]
    return q

def genpq3(q,h):
    q = [q[0]-(h/2), q[1]-(h/2), q[2]+h]
    return q

def genmq1(q,h):
    q = [q[0]-h, q[1]+(h/2), q[2]+(h/2)]
    return q

def genmq2(q,h):
    q = [q[0]+(h/2), q[1]-h, q[2]+(h/2)]
    return q

def genmq3(q,h):
    q = [q[0]+(h/2), q[1]+(h/2), q[2]-h]
    return q

def cross_entropy(p,q):
    r = 0
    for i in range(len(p)):
        r += p[i]*log2(1/q[i])
    return r

if __name__ == '__main__':
    # 真實分佈
    p = [0.2, 0.5, 0.3]
    # 初始猜測分佈
    q = [0.1, 0.7, 0.2]
    # 最大迭代次數
    m = 100
    # 步長
    h = 0.01
    # 執行貪婪演算法最小化交叉熵
    greedy(cross_entropy, p, q, m, h)