# Python 3.11 tabanlı bir sistem kullan (Use a Python 3.11 based system)
FROM python:3.11-slim

# Çalışma dizinini ayarla (Set the working directory)
WORKDIR /app

# Gerekli dosyaları kopyala (Copy necessary files)
COPY requirements.txt .

# Kütüphaneleri yükle (Install libraries)
RUN pip install --no-cache-dir -r requirements.txt

# Tüm API kodlarını kopyala (Copy all API codes)
COPY . .

# Sunucuyu başlat (Start the server)
CMD ["uvicorn", "main:main_app", "--host", "0.0.0.0", "--port", "8000"]