import Tkinter, tkFileDialog, Tkconstants, tkMessageBox
from Tkinter import *
from tkFileDialog   import askopenfilename
from tkFileDialog import *
from PIL import Image
import os
## get image dir
def chooseImg():
	name = askopenfilename()
	#status = "gambar dikonversi menjadi" + lokasi.get()
	#labelText.set(name)
	lokasi.delete(0,END)
	lokasi.insert(0,name)
	return
## get new dir
def toNewDir():
	location = asksaveasfilename()
	lokasiNewDir.delete(0,END)
	lokasiNewDir.insert(0,location)
## convert to JPEG
def toJPG():
	im_dir= lokasi.get()
	im_new_dir = lokasiNewDir.get()+".jpg"
	im_before = Image.open(im_dir)
	before = os.path.getsize(im_dir)
	im_after =im_before.save(im_new_dir, "JPEG", quality=80, optimize=True, progressive=True)
	after = os.path.getsize(im_new_dir)
	rate = compressionRate(before,after)
	labelinfo= StringVar()
	tkMessageBox.showinfo("Compression Rate",'Uncompressed Size: '+ str(before)+'\nCompresed Size'+str(after)+'\nCompression Rate:'+str(rate))
## convert to PNG
def toPNG():
	im_dir= lokasi.get()
	im_new_dir = lokasiNewDir.get()+".png"
	im_before = Image.open(im_dir)
	before = os.path.getsize(im_dir)
	im_after =im_before.save(im_new_dir, "PNG")
	after = os.path.getsize(im_new_dir)
	rate = compressionRate(before,after)
	labelinfo= StringVar()
	tkMessageBox.showinfo("Compression Rate",'Uncompressed Size: '+ str(before)+'\nCompresed Size'+str(after)+'\nCompression Rate:'+str(rate))
## convert to GIF
def toGIF():
	im_dir= lokasi.get()
	im_new_dir = lokasiNewDir.get()+".gif"
	im_before = Image.open(im_dir)
	before = os.path.getsize(im_dir)
	im_after =im_before.save(im_new_dir,"GIF")
	after = os.path.getsize(im_new_dir)
	rate = compressionRate(before,after)
	labelinfo= StringVar()
	tkMessageBox.showinfo("Compression Rate",'Uncompressed Size: '+ str(before)+'\nCompresed Size'+str(after)+'\nCompression Rate:'+str(rate))
## Count Compression rate
def compressionRate(before,after):
	compressed_size = after
	uncompressed_size = before
	compression_rate = ((uncompressed_size/compressed_size)*100)/100
	return compression_rate
app = Tk()
app.title("Image Converter")
app.geometry('550x400+200+200')
### buat Judul Aplikasi ####
judul_app= StringVar()
judul_app.set("Konverter Gambar (Jaringan Multimedia 2015)\nDibuat Oleh")
label1 = Label(app,textvariable=judul_app, height=3)
label1.pack()
### buat menampilkan NRP ####
labelText= StringVar()
labelText.set("Faris Makarim:\t 5112100154\nNarendra Hanif:\t 5112100160\nAditya Putra Ferza:\t5112100108")
label1 = Label(app,textvariable=labelText, height=4)
label1.pack()
## tombol pilih nama gambar##
button_pilih_gambar = Button(app, text="Pilih gambar", width=12,command=chooseImg)
button_pilih_gambar.pack()
## text box lokasi gambar ##
lokasiGambar = StringVar(None)
lokasi = Entry(app, textvariable=lokasiGambar,width=40)
lokasi.pack()
### teks lokasi gambar ####
text_app= StringVar()
text_app.set("Lokasi file")
label2 = Label(app,textvariable=text_app, height=3)
label2.pack()
###### button simpan file baru####
button_newFileDir = Button(app, text="Lokasi Penyimpanan", width=15,command=toNewDir)
button_newFileDir.pack()

###### teks box lokasi file baru####
lokasiGambarBaru = StringVar(None)
lokasiNewDir = Entry(app, textvariable=lokasiGambarBaru,width=40)
lokasiNewDir.pack()


### convert to JPG button###
button_JPG = Button(app, text="Ubah menjadi JPG", width=12,command=toJPG)
button_JPG.pack(side=LEFT)
#### CONVERT TO PNG ####
button_png = Button(app, text="Ubah menjadi PNG", width=12,command=toPNG)
button_png.pack(side=LEFT)
#### CONVERT TO GIF ####
button_png = Button(app, text="Ubah menjadi GIF", width=12,command=toGIF)
button_png.pack(side=LEFT)

app.mainloop()