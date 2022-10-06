from django import forms

class CreateWishlist(forms.Form):
    nama_barang = forms.TextInput()
    harga_barang = forms.IntegerField()
    deskripsi = forms.TextInput()