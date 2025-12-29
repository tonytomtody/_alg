import numpy as np  # 匯入 NumPy，用來做數值運算（例如乘積）

def riemann_nd(f, bounds, m):
    """
    f: 目標函數 f(x1, x2, ..., xn)，Python 函數，接受 n 個參數
    bounds: list，[(a1,b1), (a2,b2), ..., (an,bn)]，每一維的積分上下限
    m: 每一維切成 m 份（等距切分）
    """

    # 取得維度數 n，等於 bounds 的長度
    n = len(bounds)

    # 計算每一維的 Δx_i = (b_i - a_i) / m，結果是一個 list，長度為 n
    deltas = [(b - a) / m for (a, b) in bounds]

    # 定義遞迴函數，用來走訪所有 n 維格點
    # level: 目前正在處理第幾維（0-based）
    # current_point: 到目前為止已經選好的座標列表 [x1, x2, ..., x_level-1]
    def recurse(level, current_point):
        # 如果 level == n，代表已經為 x1...xn 都選好值
        if level == n:
            # 此時 current_point 長度為 n，可以直接丟進 f 做評估
            # 用 *current_point 把 list 展開成多個參數
            return f(*current_point)

        # 取得當前這一維的區間起點 a，以及對應的 Δx
        a, _ = bounds[level]
        delta = deltas[level]

        # total 用來累加這一維所有切點的貢獻
        total = 0

        # 在這一維上做 m 個小區間，使用「中點公式」取樣
        for i in range(m):
            # 中點位置：a + (i + 0.5) * Δx
            x = a + (i + 0.5) * delta

            # 將這一維的 x 加進 current_point，往下一維遞迴
            # current_point + [x] 會產生一個新的 list，不會改到原本的
            total += recurse(level + 1, current_point + [x])

        # 回傳在此維度上所有切點累加的結果
        return total

    # 從第 0 維開始（level=0），當前點為空 list
    total_sum = recurse(0, [])

    # 每個小超方塊的體積 = Δx1 * Δx2 * ... * Δxn
    volume_element = np.prod(deltas)

    # 黎曼和的結果 = 所有格點 f 值總和 × 每個小格子的體積
    return total_sum * volume_element

def monte_carlo_nd(f, bounds, N=100000):
    """
    f: 目標函數 f(x1, x2, ..., xn)
    bounds: [(a1,b1), (a2,b2), ..., (an,bn)]
    N: 隨機取樣點數，預設 100000
    """

    # 維度數 n，等於 bounds 的長度
    n = len(bounds)

    # 建立一個陣列 a，存放每一維的下界 [a1, a2, ..., an]
    a = np.array([b[0] for b in bounds])

    # 建立一個陣列 b，存放每一維的上界 [b1, b2, ..., bn]
    b = np.array([b[1] for b in bounds])

    # 產生形狀為 (N, n) 的亂數矩陣，每一個元素在 [0,1) 之間
    samples = np.random.rand(N, n) * (b - a) + a
    # 解釋：
    # np.random.rand(N, n) 產生 N 個點，每點是 n 維，值在 [0,1)
    # 乘上 (b - a)：縮放到每一維的長度
    # 再加上 a：平移到 [a_i, b_i] 之間

    # 對每一個樣本點 x（長度為 n），計算 f(*x)
    # np.apply_along_axis 會沿著 axis=1（每一列）套用 lambda 函數
    values = np.apply_along_axis(lambda x: f(*x), 1, samples)

    # 取所有 f 值的平均值
    mean_value = np.mean(values)

    # 區域體積 = (b1-a1) * (b2-a2) * ... * (bn-an)
    volume = np.prod(b - a)

    # 蒙地卡羅估計的積分值 = 平均值 × 體積
    return mean_value * volume

#------Test--------

# 定義一個三維函數 f3，接受三個變數 x, y, z
def f3(x, y, z):
    # 回傳 x + y + z
    return x + y + z

# 設定積分區間 [0,1] × [0,1] × [0,1]
# bounds 是一個 list，裡面有三個 tuple
bounds = [(0,1), (0,1), (0,1)]

# 呼叫 n 維黎曼積分函數
# m=20 表示每一維切成 20 等份，總共會有 20^3 個格點
print("Riemann 3D:", riemann_nd(f3, bounds, m=20))

# 呼叫 n 維蒙地卡羅積分
# N=50000 表示隨機取樣 50000 個三維點
print("Monte Carlo 3D:", monte_carlo_nd(f3, bounds, N=50000))

# 定義一個五維函數 f5，接受五個參數 x1, x2, x3, x4, x5
def f5(x1, x2, x3, x4, x5):
    # 函數定義：x1*x2 + x3 + x4*x5
    return x1 * x2 + x3 + x4 * x5

# 設定 5 維的積分區間，每一維都是 [0,1]
# 用 [(0,1)] * 5 來快速產生 [(0,1),(0,1),(0,1),(0,1),(0,1)]
bounds_5d = [(0,1)] * 5

# 用黎曼積分估計 5 維積分，m=10 每維切 10 份 => 總格點數 10^5
print("Riemann 5D:", riemann_nd(f5, bounds_5d, m=10))

# 用蒙地卡羅估計 5 維積分，取樣 100000 個點
print("Monte Carlo 5D:", monte_carlo_nd(f5, bounds_5d, N=100000))