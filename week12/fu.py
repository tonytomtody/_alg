import numpy as np

import matplotlib.pyplot as plt

def dft(x):
    """離散傅立葉正轉換 (DFT)"""
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def idft(X):
    """離散傅立葉逆轉換 (IDFT)"""
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
        x[n] /= N
    return x

def main():
    # 建立測試訊號
    N = 128
    t = np.linspace(0, 1, N, endpoint=False)
    
    # 組合訊號：5Hz + 10Hz + 20Hz
    signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t) + 0.3 * np.sin(2 * np.pi * 20 * t)
    
    # 執行傅立葉正轉換
    frequency_spectrum = dft(signal)
    
    # 執行傅立葉逆轉換
    reconstructed_signal = idft(frequency_spectrum)
    
    # 頻率軸
    freqs = np.fft.fftfreq(N, t[1] - t[0])
    
    # 繪圖
    plt.figure(figsize=(12, 8))
    
    # 原始訊號
    plt.subplot(3, 1, 1)
    plt.plot(t, signal)
    plt.title('原始訊號')
    plt.xlabel('時間 (秒)')
    plt.ylabel('振幅')
    plt.grid(True)
    
    # 頻譜
    plt.subplot(3, 1, 2)
    plt.plot(freqs[:N//2], np.abs(frequency_spectrum)[:N//2])
    plt.title('頻譜 (傅立葉正轉換)')
    plt.xlabel('頻率 (Hz)')
    plt.ylabel('振幅')
    plt.grid(True)
    
    # 重建訊號
    plt.subplot(3, 1, 3)
    plt.plot(t, reconstructed_signal.real)
    plt.title('重建訊號 (傅立葉逆轉換)')
    plt.xlabel('時間 (秒)')
    plt.ylabel('振幅')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # 驗證重建誤差
    error = np.max(np.abs(signal - reconstructed_signal.real))
    print(f'重建誤差: {error:.2e}')

if __name__ == '__main__':
    main()