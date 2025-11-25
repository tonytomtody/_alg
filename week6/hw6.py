def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    # 建立 DP 表格，大小 (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化邊界條件
    for i in range(m + 1):
        dp[i][0] = i  # 把 s1[0..i] 轉成空字串，需要 i 次刪除
    for j in range(n + 1):
        dp[0][j] = j  # 把空字串轉成 s2[0..j]，需要 j 次插入

    # 填表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 字元相同，不需操作
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # 刪除
                    dp[i][j - 1],     # 插入
                    dp[i - 1][j - 1]  # 替換
                )
    return dp[m][n]

# 測試
print(edit_distance("kitten", "sitting"))  # 輸出 3
print(edit_distance("flaw", "lawn"))       # 輸出 2
print(edit_distance("onion","option"))