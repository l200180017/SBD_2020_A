from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
query = ("SELECT id_nasabahFK,jenis_transaksi,tanggal,jumlah FROM transaksi WHERE YEAR(tanggal)=2020")
cursor.execute(query)
for (id_nasabahFK,jenis_transaksi,tanggal,jumlah)in cursor:
    print("nasabah dengan ID {} melakukan transaksi {} pada {:%d %b %Y} sejumlah {}".format(id_nasabahFK,jenis_transaksi,tanggal,jumlah))     
cursor.close()
cnx.close()

##from datetime import date, datetime, timedelta
##import mysql.connector
##
##cnx = mysql.connector.connect(user='root', database='perbankan')
##cursor = cnx.cursor()
##tanggal = datetime.now().date()
##tambah_transaksi=("INSERT INTO transaksi(id_nasabahFK,no_rekeningFK,jenis_transaksi,tanggal,jumlah) VALUES(%s,%s,%s,%s,%s)")
##data_transaksi = ('9','110','kredit',tanggal,'50000')
##cursor.execute(tambah_transaksi,data_transaksi)
##
##cnx.commit()
##cursor.close()
##cnx.close()
