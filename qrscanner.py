import qrcode
from pyzbar.pyzbar import decode
from PIL  import Image

myqr=qrcode.make("https://www.youtube.com/watch?v=IUQVO97zcE0")
myqr1=qrcode.make("https://www.simplilearn.com/?utm_source=bing&utm_medium=cpc&utm_term=simplilearn&utm_content=392503905-1320514564874663-&utm_device=c&utm_campaign=B-Search-Brand-Exact-IN-AllDevice-adgroup-Brand-Simplilearn&msclkid=21828d79cccc1d9ebfb6eb26ce36ee1c")
myqr.save("myqr.png",scale=19)
b=decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))