import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('data.csv')

# 'district' sütununda "Sincan" ile başlayan satırları seç
df_sincan = df[df['district'].str.startswith('Etimesgut')]

print(df_sincan)
