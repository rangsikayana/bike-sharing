import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat dataset
day_data = pd.read_csv('dashboard/day.csv')
hour_data = pd.read_csv('dashboard/hour.csv')

# Mengonversi kolom 'dteday' ke tipe datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Menambahkan judul dan deskripsi
st.title("Proyek Analisis Data: Bike Sharing Dataset")
st.write("Selamat datang di dashboard analisis data peminjaman sepeda menggunakan Streamlit.")
st.write("Nama: Rangsi Ridho Kayana")
st.write("Email: rangsikayana@gmail.com")
st.write("ID Dicoding: rangsikayana")

# Analisis Musim
st.write("---")
st.header("Analisis Musim")
st.write("Grafik di bawah ini menampilkan jumlah total sepeda yang dipinjam per musim pada tahun 2011.")

# Analisis Musim
musim = {
    1: "Musim Semi",
    2: "Musim Panas",
    3: "Musim Gugur",
    4: "Musim Dingin"
}
jumlah_peminjaman_musim = [day_data[(day_data["yr"] == 0) & (day_data["season"] == kode_musim)]["cnt"].sum() for kode_musim in musim]

# Plot data musim
plt.figure(figsize=(10, 5))
sns.barplot(x=list(musim.values()), y=jumlah_peminjaman_musim, palette="viridis")
plt.title("Jumlah Total Sepeda yang Dipinjam per Musim di Tahun 2011")
plt.xlabel("Musim")
plt.ylabel("Jumlah Dipinjam")
st.pyplot(plt)

# Ringkasan Analisis Musim
st.write("Grafik menunjukkan bahwa musim gugur memiliki jumlah peminjaman sepeda tertinggi, diikuti oleh musim panas dan musim semi. Ini konsisten dengan kesimpulan awal bahwa permintaan peminjaman sepeda meningkat dari musim semi ke musim panas, mencapai puncaknya di musim gugur, dan kemudian sedikit menurun di musim dingin.")

# Analisis Total Peminjaman Sepeda per Bulan pada Tahun 2012
st.write("---")
st.header("Analisis Total Peminjaman Sepeda per Bulan pada Tahun 2012")
st.write("Grafik di bawah ini menampilkan jumlah total sepeda yang dipinjam per bulan pada tahun 2012.")

# Total Peminjaman Sepeda per Bulan
data_tahun_2012 = day_data[day_data["yr"] == 1]
plt.figure(figsize=(15, 5))
sns.lineplot(x="dteday", y="cnt", data=data_tahun_2012, linewidth=1, color='grey', marker='o', drawstyle='steps-post')
plt.xlabel("Bulan dan Tahun")
plt.ylabel("Jumlah Dipinjam")
plt.title("Jumlah Total Sepeda yang Dipinjam per Bulan pada Tahun 2012")
st.pyplot(plt)

# Ringkasan Analisis Total Peminjaman Sepeda per Bulan
st.write("Grafik menunjukkan tren jumlah sepeda yang dipinjam per bulan pada tahun 2012. Permintaan terus meningkat dari awal tahun hingga pertengahan tahun, mencapai puncaknya pada kuartal kedua, sebelum sedikit menurun menuju akhir tahun.")

# Analisis Total Peminjaman Sepeda per Bulan oleh Pengguna Terdaftar dan Tidak Terdaftar pada 2011-2012
st.write("---")
st.header("Analisis Total Peminjaman Sepeda per Bulan oleh Pengguna Terdaftar dan Tidak Terdaftar pada 2011-2012")
st.write("Grafik di bawah ini membandingkan jumlah total sepeda yang dipinjam per bulan oleh pengguna terdaftar dan tidak terdaftar pada tahun 2011-2012.")

# Total Peminjaman Sepeda per Bulan oleh Pengguna Terdaftar dan Tidak Terdaftar
data_per_bulan = day_data.set_index('dteday').resample(rule='M').mean()
plt.figure(figsize=(15, 5))
sns.lineplot(x=data_per_bulan.index, y="registered", data=data_per_bulan, color='blue', label='Terdaftar', marker='o', drawstyle='steps-post')
sns.lineplot(x=data_per_bulan.index, y="casual", data=data_per_bulan, color='orange', label='Tidak Terdaftar', linestyle='-', marker='o', drawstyle='steps-post')
plt.xlabel("Bulan dan Tahun")
plt.ylabel("Jumlah Dipinjam")
plt.title("Jumlah Total Sepeda yang Dipinjam per Bulan oleh Pengguna Terdaftar dan Tidak Terdaftar pada 2011-2012")
plt.legend(loc='upper left', fontsize=12)
st.pyplot(plt)

# Ringkasan Analisis Total Peminjaman Sepeda per Bulan oleh Pengguna
st.write("Grafik menunjukkan tren jumlah sepeda yang dipinjam per bulan oleh pengguna terdaftar dan tidak terdaftar pada tahun 2011-2012.")

# Analisis Perbandingan Peminjaman Sepeda antara Jam Teratas dan Jam Terbawah
st.write("---")
st.header("Analisis Perbandingan Peminjaman Sepeda antara Jam Teratas dan Jam Terbawah")
st.write("Grafik di bawah ini membandingkan jumlah peminjaman sepeda pada 5 jam teratas dan terbawah.")

# Perbandingan Peminjaman Sepeda antara Jam Teratas dan Jam Terbawah
jumlah_peminjaman_jam = hour_data.groupby("hr")["cnt"].sum().sort_values(ascending=False)
plt.figure(figsize=(15, 5))
barplot = sns.barplot(x=jumlah_peminjaman_jam.index, y=jumlah_peminjaman_jam.values, linewidth=1, edgecolor='black', facecolor='none')
plt.ylabel("Jumlah Dipinjam")
plt.xlabel("Jam")
plt.title("Perbandingan Jumlah Sepeda yang Dipinjam pada 5 Jam Teratas dan Terbawah")
plt.xticks(fontsize=12)
jam_teratas = jumlah_peminjaman_jam.head(5)
jam_terbawah = jumlah_peminjaman_jam.tail(5)
for bar in barplot.patches:
    if bar.get_height() in jam_teratas.values:
        bar.set_color('blue')
    elif bar.get_height() in jam_terbawah.values:
        bar.set_color('orange')
st.pyplot(plt)

# Ringkasan Analisis Perbandingan Peminjaman Sepeda antara Jam Teratas dan Jam Terbawah
st.write("Grafik menunjukkan perbedaan signifikan dalam jumlah peminjaman sepeda antara jam-jam teratas dan terbawah. Jam-jam dengan jumlah peminjaman tertinggi, terutama pada jam-jam menuju dan meninggalkan tempat kerja atau sekolah, menunjukkan tingkat penggunaan sepeda yang tinggi. Sementara itu, jam-jam dengan jumlah peminjaman terendah, terutama pada malam hari dan dini hari, menunjukkan tingkat penggunaan yang rendah.")

# Analisis Rata-Rata Frekuensi Peminjaman Sepeda pada Hari Kerja dan Hari Libur
st.write("---")
st.header("Analisis Rata-Rata Frekuensi Peminjaman Sepeda pada Hari Kerja dan Hari Libur")
st.write("Grafik di bawah ini menampilkan rata-rata frekuensi peminjaman sepeda pada hari kerja dan hari libur berdasarkan jam.")

# Rata-Rata Frekuensi Peminjaman Sepeda pada Hari Kerja dan Hari Libur
hour_data['hari_kerja'] = (hour_data['holiday'] == 0).astype(int)
plt.figure(figsize=(15, 5))
plot = sns.pointplot(data=hour_data, x='hr', y='cnt', hue='hari_kerja', palette={0: 'orange', 1: 'blue'}, markers=["o", "o"], linewidth=1.5, err_kws={'linewidth': 0}, drawstyle='steps-post')
plt.title('Rata-Rata Frekuensi Peminjaman Sepeda pada Hari Kerja dan Hari Libur berdasarkan Jam')
plt.ylabel('Frekuensi Dipinjam')
plt.xlabel('Jam')
handles, labels = plot.get_legend_handles_labels()
handles = handles[::-1]
labels = ['Hari Kerja', 'Hari Libur']
plt.legend(handles, labels, loc='upper left', fontsize=12)
st.pyplot(plt)

# Ringkasan Analisis Rata-Rata Frekuensi Peminjaman Sepeda pada Hari Kerja dan Hari Libur
st.write("Grafik menunjukkan pola peminjaman sepeda rata-rata pada hari kerja dan hari libur. Pada hari kerja, terjadi lonjakan peminjaman sepeda pada jam-jam menuju dan meninggalkan tempat kerja, sementara pada akhir pekan, terjadi peningkatan stabil tanpa lonjakan yang signifikan. Hal ini mungkin disebabkan oleh aktivitas rekreasi atau sosial selama akhir pekan.")

# Footer
st.write("---")
st.write("© 2024 PT. Dicoding Akademi Indonesia | Sumber data: [Kaggle - Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)")
