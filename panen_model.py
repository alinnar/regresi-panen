import pandas as pd # Mengimpor library Pandas yang digunakan untuk manipulasi dan analisis data, serta untuk memudahkan pengolahan data dalam bentuk DataFrame.
import numpy as np # Mengimpor library NumPy yang menyediakan dukungan untuk array dan operasi matematika yang efisien serta fungsi numerik lainnya.
from sklearn.model_selection import train_test_split  # Mengimpor fungsi train_test_split dari scikit-learn untuk membagi dataset menjadi set pelatihan dan set pengujian.
from sklearn.linear_model import LinearRegression  # Mengimpor kelas LinearRegression dari scikit-learn yang digunakan untuk membuat model regresi linear.
import joblib # Mengimpor library joblib yang digunakan untuk menyimpan dan memuat model machine learning dalam format file yang efisien.

# Menghasilkan data sintetik
np.random.seed(42)
data_size = 100

# Curah hujan (mm) dan hasil panen (ton)
rainfall = np.random.uniform(0, 500, data_size)  # Curah hujan antara 0 dan 500 mm
yield_values = 0.1 * rainfall + np.random.normal(0, 5, data_size)  # Hubungan linear dengan noise

# Membuat DataFrame
data = pd.DataFrame({
    'Curah Hujan (mm)': rainfall,
    'Hasil Panen (ton)': yield_values
})

# Menyimpan DataFrame ke file CSV (optional)
data.to_csv("data_curah_hujan_hasil_panen.csv", index=False)
data = [['Produksi', 'Curah Hujan']]

# Memisahkan fitur dan target
X = data[['Curah Hujan (mm)']]
y = data['Hasil Panen (ton)']

# Membagi data menjadi set pelatihan dan set pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat dan melatih model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# Menyimpan model ke file PKL
joblib.dump(model, "panenmodel2.pkl")

print("Model regresi linear telah disimpan sebagai 'panenmodel2.pkl'.")