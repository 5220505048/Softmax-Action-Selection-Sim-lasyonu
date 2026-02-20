import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('Agg') 

class LoadBalancer:
    def __init__(self, k_servers, temperature=0.1):
        self.k = k_servers
        self.temperature = temperature
        self.q_values = np.zeros(k_servers)
        self.counts = np.zeros(k_servers)

    def select_server(self):
        # --- NÜMERİK STABİLİTE ÇÖZÜMÜ ---
        # e^x hesaplarken overflow olmaması için max değer çıkarılır.
        shifted_q = (self.q_values - np.max(self.q_values)) / self.temperature
        exp_q = np.exp(shifted_q)
        probabilities = exp_q / np.sum(exp_q)
        return np.random.choice(self.k, p=probabilities)

    def update(self, server_index, latency):
        reward = 1.0 / (latency + 1e-6) 
        alpha = 0.1 # Öğrenme oranı
        self.q_values[server_index] += alpha * (reward - self.q_values[server_index])

# --- SİMÜLASYON ---
n_requests = 1000
k_servers = 5
balancer = LoadBalancer(k_servers, temperature=0.05)
true_latencies = [10, 50, 100, 20, 200]
history = []

for i in range(n_requests):
    server = balancer.select_server()
    actual_latency = true_latencies[server] + np.random.normal(0, 5)
    balancer.update(server, actual_latency)
    history.append(actual_latency)
    
    if i == 500: # 500. adımda sistem değişiyor (Non-stationary)
        true_latencies[0] = 500 

print(f"Simülasyon Tamamlandı. Ortalama Gecikme: {np.mean(history):.2f} ms")

# --- GRAFİK OLUŞTURMA VE KAYDETME ---
plt.figure(figsize=(12, 6))
plt.plot(history, label='Anlık Gecikme (ms)', color='skyblue', alpha=0.4)

if len(history) > 20:
    moving_avg = np.convolve(history, np.ones(20)/20, mode='valid')
    plt.plot(range(19, len(history)), moving_avg, label='Trend (SMA-20)', color='red', linewidth=2)

plt.axvline(x=500, color='black', linestyle='--', label='Sistem Değişimi (500. İstek)')
plt.title('Softmax Yük Dengeleyici Performans Analizi')
plt.xlabel('İstek Sayısı')
plt.ylabel('Gecikme (ms)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.savefig('sonuc.png', dpi=300)
print("Grafik başarıyla 'sonuc.png' olarak kaydedildi. Masaüstünde/Klasörde görebilirsin.")