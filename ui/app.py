import streamlit as st
import requests

st.set_page_config(page_title="Tıbbi Özet Asistanı", layout="wide")
st.title("🩺 Tıbbi Özet Denetim Döngüsü")

user_input = st.text_area("Hasta şikayetlerini buraya girin:", height=200)

if st.button("Analiz Et"):
    if user_input:
        with st.spinner("Ajanlar tartışıyor, lütfen bekleyin..."):
            try:
                # API'ye istek atıyoruz
                response = requests.post(
                    "http://api:8000/analyze", 
                    json={"text": user_input},
                    timeout=60 # Gemini bazen yavaş cevap verebilir
                )
                
                if response.status_code == 200:
                    data = response.json()
                    st.subheader("✅ Onaylanmış Tıbbi Özet")
                    st.success(data.get("final_summary", "Özet oluşturulamadı."))
                    
                    with st.expander("🕵️ Ajanların Çalışma Geçmişi"):
                        for log in data.get("history", []):
                            st.write(log)
                else:
                    st.error(f"API Hatası: {response.status_code} - {response.text}")
                    
            except Exception as e:
                st.error(f"Bağlantı Hatası: {str(e)}")
    else:
        st.warning("Lütfen bir metin girin.")