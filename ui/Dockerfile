# Python 3.11 tabanlı sistem (Python 3.11 based system)
FROM python:3.11-slim

# Çalışma dizini (Working directory)
WORKDIR /app

# Gerekli dosyaları kopyala (Copy requirements)
COPY requirements.txt .

# Kütüphaneleri yükle (Install libraries)
RUN pip install --no-cache-dir -r requirements.txt

# Tüm UI kodlarını kopyala (Copy UI code)
COPY . .

# Streamlit arayüzünü başlat (Start Streamlit)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]