# BIO  

Genetik bilimi açısından önemli veritabanlarından toplu veri alma ve işleme yazılımı. 

Desteklenen veritabanları:
* MutationTaster
* Polyphen-2
* ...

Program kendisine verilen büyük veri dosyasındaki bilgilere göre uzak veritabanlarından bilgilere erişir ve okunabilir yapıda kullanıcıya sunar.

## Kaynak koddan derlemek için gereksinimler 

- Python v3.0 ve üstü
- tkinter v8.0 ve üstü
- requests kütüphanesi (python3 için)

## Çalıştırılabilir dosya için gereksinimler

- Yalnızca çalıştırılabilir dosyaya çift tıklamanız yeterli. 

## Örnek girdi dosyası
Proje içerisinde ./input/input dosyası örnek girdi olarak kullanılabilir.

## Girdi dosya yapısı
Her bir kişi için bir satır boşluk bırakılmalı. 

```
name: isim
site: mutationtaster
özellik1: veri
özellik2: veri
... 
...

name: isim
site: polyphen
özellik1: veri
özellik2: veri
özellik3: veri
...

...
...

```

Eklenebiilecek özellikler

```
mutationtaster : 
	-> "gene", 
	-> "transcript",
	-> "snippets refers to",
	-> "alteration",
	-> "position",
	-> "new base",
	-> "first wild type base",
	-> "last wild type base",
	-> "inserted bases",
	-> "name of alteration"
	
---------------------------------

polyphen : 
	-> 'protein',
	-> 'sequence',
	-> 'position',
	-> 'AA1', 
	-> 'AA2'
```

Örnek Girdi dosyası:
```
to: mutationtaster
name: Hakan Keleş
transcript: ENST00000379370
snippets refers to: gDNA
first wild type base: 28669
last wild type base: 28672

to: polyphen
name: Emre Horsanalı
protein: P41567
position: 59
AA1: L
AA2: P

to: mutationtaster
name: Yetiş Yılmaz
transcript: ENST00000270142
snippets refers to: CDS
alteration: C[A/G]TGTTCATGAGTTTGGAGATAATACAGCAGGCTGT
name of alteration: CHRND_L63P

to: polyphen
name: Hasan Kot
protein: P41567
position: 59
AA1: L
AA2: P

to: polyphen
name: Ahmet Sonuç
protein: P41567
position: 59
AA1: L
AA2: P

to: mutationtaster
name: Berkay Dedeoglu
transcript: ENST00000379370
snippets refers to: gDNA
first wild type base: 28669
last wild type base: 28672

to: polyphen
name: Ismail Can
protein: P41567
position: 59
AA1: L
AA2: P

to: mutationtaster
name: Necla Kayagencer
transcript: ENST00000270142
snippets refers to: CDS
alteration: C[A/G]TGTTCATGAGTTTGGAGATAATACAGCAGGCTGT
name of alteration: CHRND_L63P

to: polyphen
name: Suat Kama
protein: P41567
position: 59
AA1: L
AA2: P

to: polyphen
name: Ahmet Sonuç
protein: P41567
position: 59
AA1: L
AA2: P

to: mutationtaster
name: Ayşegül Yılmaz
gene: KlMn3
transcript: EN2365535896
last wild type base: 12 
inserted bases: 26

to: mutationtaster
name: Ayşegül Yılmaz 
gene: pljh
transcript: EN256321458200
new base: 45
position: 23

to: polyphen
name: İsmail Candaş
protein: EN8965424562
position: 20
AA1: A
AA2: B

```

### Danışman
**Gıyasettin Özcan**

---

### Geliştiriciler

**Emre Horsanalı**
**Berkay Dedeoğlu**




