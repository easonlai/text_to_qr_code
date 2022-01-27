import segno

text_to_qr = 'Meeting Room F'
qrcode = segno.make(text_to_qr, micro=False)
qrcode.save('text_to_qr.png', scale=5)