import time

def truth_table_manual(n):
    rows = []
    for i in range(2**n):
        row = [(i >> j) & 1 for j in reversed(range(n))]
        rows.append(tuple(row))
    return rows

# 測試效率
n = 10
start = time.time()
rows = truth_table_manual(n)
end = time.time()

print(f"手寫版本產生 {len(rows)} 列，耗時 {end - start:.6f} 秒")