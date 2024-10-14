import streamlit as st # Mengimpor library Streamlit, yang digunakan untuk membangun aplikasi web interaktif dan visualisasi data dengan mudah menggunakan Python.
import joblib # Mengimpor library joblib, yang digunakan untuk menyimpan dan memuat objek Python, seperti model machine learning, dalam format file yang efisien (misalnya pkl).
import os # Mengimpor library os, yang menyediakan fungsi untuk berinteraksi dengan sistem operasi, termasuk operasi file dan pengelolaan direktori.
import numpy as np # Mengimpor library NumPy, yang menyediakan dukungan untuk array multidimensi dan operasi matematis yang efisien pada data numerik.

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Hasil Panen Padi",
    page_icon="🌾",
)

# Memuat model
def load_prediction_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

def main():
    """Prediksi Hasil Panen Padi Berdasarkan Curah Hujan"""

    # HTML Template untuk tampilan
    html_template = """
    <div style="background-color:#6A9FB5;padding:10px;border-radius:10px;">
    <h3 style="color:white">Prediksi Hasil Panen Padi Menggunakan Regresi Linier</h3>
    </div>
    """
    
    # Pilihan menu
    activity = ["Prediksi Hasil Panen", "Apa itu Regresi?"]
    choice = st.sidebar.selectbox("Menu", activity)

    # Pilihan Prediksi Hasil Panen
    if choice == 'Prediksi Hasil Panen':
        st.title("🌾 Prediksi Hasil Panen Padi 🌾")
        st.markdown(html_template, unsafe_allow_html=True)
        st.subheader("Masukkan Data Curah Hujan")

        # Input untuk curah hujan
        rainfall_input = st.text_input("Masukkan Curah Hujan (<= 500mm)", "")

        if st.button("Proses"):
            # Memvalidasi input
            if rainfall_input:
                try:
                    rainfall = float(rainfall_input)
                    if rainfall < 0 or rainfall > 500:
                        st.error("Curah hujan harus antara 0 dan 500 mm.")
                    else:
                        # Memuat model regresi linear
                        regressor = load_prediction_model("panenmodel.pkl")
                        rainfall_reshaped = np.array(rainfall).reshape(-1, 1)

                        # Melakukan prediksi
                        predicted_yield = regressor.predict(rainfall_reshaped)

                        # Menampilkan hasil prediksi
                        st.success(f"Hasil panen padi yang diprediksi untuk curah hujan {rainfall} mm adalah: {predicted_yield[0]:.2f} ton")
                except ValueError:
                    st.error("Input tidak valid. Harap masukkan angka yang valid untuk curah hujan.")
            else:
                st.error("Silakan masukkan nilai curah hujan.")

    else:
        st.title("Apa itu Regresi?")
        st.success("Regresi adalah metode statistik yang digunakan untuk memperkirakan hubungan antara variabel dependen (hasil) dan satu atau lebih variabel independen (fitur).")

if __name__ == '__main__':
    main()