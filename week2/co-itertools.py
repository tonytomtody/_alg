import itertools
import time

def truth_table_itertools(n):
    return list(itertools.product([0, 1], repeat=n))

# 測試效率
n = 10  # 變數數量
start = time.time()
rows = truth_table_itertools(n)
end = time.time()

print(f"itertools 產生 {len(rows)} 列，耗時 {end - start:.6f} 秒")