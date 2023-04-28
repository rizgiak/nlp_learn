import MeCab
wakati = MeCab.Tagger("-Owakati")
text = wakati.parse("圧力中心情報を用いて手内回転を行うに指ロボットの開発").split()
print(text)