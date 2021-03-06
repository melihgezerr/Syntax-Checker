import re
f = open("calc.in")
ff = open("calc.out", "w")
bbool = True
list_of_lines = f.read().splitlines()
for seq in list_of_lines.copy():
    if seq == "\n":
        list_of_lines.remove(seq)
for seq in list_of_lines.copy():
    if seq == "":
        list_of_lines.remove(seq)
for i in list_of_lines:
    list_of_lines[list_of_lines.index(i)] = i.strip()
init_var = []
mid_var = []
init_value = []
mid_value = []
sonuc_term = []
my_text = "\n".join(list_of_lines)
my_text_replaced = "\n".join(list_of_lines)
try:
    init_lines = list_of_lines[list_of_lines.index("AnaDegiskenler")+1 : list_of_lines.index("YeniDegiskenler")]
    mid_lines = list_of_lines[list_of_lines.index("YeniDegiskenler")+1 : list_of_lines.index("Sonuc")]
    sonuc_line = list_of_lines[list_of_lines.index("Sonuc")+1:]
    all_stmt_lines = init_lines + mid_lines
except:
    pass

keywords = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti',
            'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis', '+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')',
            'ac-parantez', 'kapa-parantez', 'AnaDegiskenler', 'YeniDegiskenler', 'Sonuc', 'degeri', 'olsun', 'nokta'}
sayilar = ["sifir", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]
rakamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dictt = {"ac-parantez": "(", "kapa-parantez": ")",
         "sifir": "0", "bir": "1", "iki": "2", "uc": "3", "dort": "4",
         "bes": "5", "alti": "6", "yedi": "7", "sekiz": "8", "dokuz": "9",
         "arti": "+", "eksi": "-", "carpi": "*", "nokta": "."}
remove_list = ['+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')',
            'ac-parantez', 'kapa-parantez',"nokta"]

for i, j in dictt.items():
    if i in my_text_replaced.split():
        my_text_replaced = my_text_replaced.replace(i, j)
try:
    for i in list_of_lines:
        anad_yenid = list_of_lines[list_of_lines.index("AnaDegiskenler")+1:list_of_lines.index("YeniDegiskenler")]
        yenid_sonuc = list_of_lines[list_of_lines.index("YeniDegiskenler") + 1:list_of_lines.index("Sonuc")]
        sonuc_term = list_of_lines[list_of_lines.index("Sonuc")+1:]
    for i in anad_yenid:
        x = re.findall("(.*\S)\s+degeri",i)
        init_var += x
    for i in yenid_sonuc:
        x = re.findall("(.*\S)\s+degeri",i)
        mid_var += x
    for i in anad_yenid:
        x = re.findall("degeri\s+(.*\S)\s+olsun",i)
        init_value += x
    for i in yenid_sonuc:
        x = re.findall("degeri\s+(.*\S)\s+olsun",i)
        mid_value += x
except:
    pass

########################################BURAYA KADAR HER SEY TANIMLANMALI###########################

########################################KONTROLLER BASLADI##########################################

if not list_of_lines[0] == "AnaDegiskenler":  #### AnaDegiskenler ile baslamal??
    bbool = False
#print(bbool)

try:
    if len(all_stmt_lines) != 0:
        for line in all_stmt_lines:
            if not re.search(".+olsun", line):     #### t??m statementlar single line olmal??
                bbool = False
except:
    pass
#print(bbool)

try:
    if len(init_var) == len(anad_yenid) and len(mid_var) == len(yenid_sonuc):       ####YAZIM YANLI??I VARSA BAZEN BULUYOR
        pass                                                                    ## REGEX YAKALAYAMADIGI ??C??N BULUYOR
    else:
        bbool=False
except:
    pass
#print(bbool)

if re.search("ve\s*ve",my_text) or re.search("veya\s*ve",my_text) or re.search("ve\s*veya",my_text) or re.search("veya\s*veya",my_text):              ####YAZIM YANLI??I VARSA BAZEN BULUYOR
    bbool = False                                                                     ## REGEX YAKALAYAMADIGI ??C??N BULUYOR
#print(bbool)

try:
    if not (list_of_lines[-1] == "Sonuc" or list_of_lines[-2] == "Sonuc"):   ##### Sonuctan sonra tek sat??r olmal??.
        bbool = False
    #print(bbool)
except:
    pass

if not re.findall("AnaDegiskenler|YeniDegiskenler|Sonuc", my_text) == ["AnaDegiskenler", "YeniDegiskenler", "Sonuc"] :  ##### 3 ana parcay?? var m???
    bbool = False
#print(bbool)

for i in init_var+mid_var:
    if i in keywords or not i.isalnum() or len(i) > 10:
        bbool = False                                         #### variablelar keyword olmamal??, 10 birim olmal?? ve alphanumeric olmal??
#print(bbool)

if len(init_var) != len(set(init_var)) or len(mid_var) != len(set(mid_var)):   #### variablelar sadece bir kez kullan??lmal??
    bbool = False
#print(bbool)

if re.search("\d+\s*\.\s*[a-z]+|[a-z]+\s*\.\s*\d+|[a-z]+\s*\.\s*[a-z]+",my_text):   #### 3 . dort veya   uc . dort  veya  uc . 4 olmaml??.
    bbool = False
#print(bbool)

for line in list_of_lines:
    words = line.split()
    try:
        if "nokta" in words:
            if words[words.index("nokta")-1] in sayilar and words[words.index("nokta")+1] in sayilar:   ### bir nokta 5 , 9 nokta alt??, gibi anlams??z ??eyleri buluyor
                pass
            else:
                bbool = False
    except:
        pass
    try:
        for i in range(len(words)):
            if i > 0 and i < (len(words)) :
                if words[i] in sayilar and (words[i-1] in sayilar or words[i+1] in sayilar):                  ### dokuz dokuz gibi seyleri buluyor
                    bbool = False
    except:
        pass

#print(bbool)

if re.search("\d+\s+\.\s+\d+|\d+\.\s+\d+|\d+\s+\.\d+", my_text):     ##### 3 . 4 gibi bo??luklar?? buluyor.
    bbool = False
#print(bbool)


for i in init_value:                    #### baslang??c degerlerini kontrol etti.
    splitted = i.split()
    if len(splitted) > 1:                    #### baslang??c degerlerini kontrol etti.
        if "nokta" in splitted:
            if splitted[splitted.index("nokta")-1] in sayilar and splitted[splitted.index("nokta")+1] in sayilar:
                pass
            else:                                                       #### baslang??c degerlerini kontrol etti.
                bbool = False
        else:
            bbool = False
    if len(splitted) == 1:
        if re.search("^\d$|^\d\.\d$|^sifir$|^bir$|^iki$|^uc$|^dort$|^bes$|^alti$|^yedi$|^sekiz$|^dokuz$|^dogru$|^yanlis$",i):  #### baslang??c degerlerini kontrol etti.
            pass
        else:
            bbool = False
#print(bbool)

for i in mid_value:                                             #### PARANTEZ KONTROL
    splitted = i.split()
    stack = []
    for prtnez in splitted:
        if prtnez == "(" or prtnez == "ac-parantez":
            stack.append(prtnez)
        elif prtnez == ")" or prtnez == "kapa-parantez":                #### PARANTEZ KONTROL
            if (len(stack) > 0) :
                stack.pop()
            else:
                bbool =False
    if len(stack) == 0:                                 #### PARANTEZ KONTROL
        pass
    else:
        bbool = False
#print(bbool)

if re.search("\(\s*\)",my_text):
    bbool = False                                   #### PARANTEZ KONTROL
#print(bbool)

for i in sonuc_term:
    splitted = i.split()                                #### PARANTEZ KONTROL
    stack = []
    for prtnez in splitted:
        if prtnez == "(" or prtnez == "ac-parantez":
            stack.append(prtnez)
        elif prtnez == ")" or prtnez == "kapa-parantez":
            if (len(stack) > 0) :
                stack.pop()
            else:
                bbool =False                                #### PARANTEZ KONTROL
    if len(stack) == 0:
        pass
    else:
        bbool = False
#print(bbool)

###############################B??N LOOP VE AR??TMET??K LOOP AYIRICI###################################

bool_dict_initvar = {}
bool_dict_midvar = {}

try:
    for a in init_var:
        if init_value[init_var.index(a)] == "dogru" or init_value[init_var.index(a)] == "yanlis":
            bool_dict_initvar[a] = init_value[init_var.index(a)]                                         #### booldict??N??T VAR A LOG??CAL OLANLARI EKL??YOR
except:
    pass

for a in mid_var:
    bool_dict_midvar[a] = 1             ### M??D VALUELARIN LOG??CAL OLUP OLMADI??INI KONTROL ED??YOR
for i in range(len(mid_value)):                                   ####BOOL D??CT M??DVAR DA  1 LER LOG??CAL   0 LAR AR??TMET??C
    x = mid_value[i].split()
    if '+' in x or '-' in x or '*' in x or 'arti' in x or 'eksi' in x or 'carpi' in x:
        bool_dict_midvar[mid_var[i]] = 0
    else:
        for a in x.copy():
            if a in remove_list:
                x.remove(a)
        for aa in x:                                        ### M??D VALUELARIN LOG??CAL OLUP OLMADI??INI KONTROL ED??YOR
            if aa in bool_dict_initvar:                             ####BOOL D??CT M??DVAR DA  1 LER LOG??CAL   0 LAR AR??TMET??C
                pass
            elif aa == "dogru" or aa == "yanlis":
                pass
            elif aa in sayilar or aa in rakamlar:
                bool_dict_midvar[mid_var[i]] = 0
                break
            elif re.search("^\d\.\d$",aa):
                bool_dict_midvar[mid_var[i]] = 0
                break
            else:
                bool_dict_midvar[mid_var[i]] = 0           ### M??D VALUELARIN LOG??CAL OLUP OLMADI??INI KONTROL ED??YOR
            if aa in mid_var and bool_dict_midvar[aa] == 1:                     ###BOOL D??CT M??DVAR DA 1 LER LOG??CAL  0 LAR AR??TMET??C
                bool_dict_midvar[mid_var[i]] = 1

###############################B??N LOOP VE AR??TMET??K LOOP AYIRICI###################################
aritmetic_midvalue = {}
for i in bool_dict_midvar:
    if bool_dict_midvar[i] == 0:
        aritmetic_midvalue[i] = mid_value[mid_var.index(i)]

remove_list = ['+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')',
            'ac-parantez', 'kapa-parantez',"nokta"]

for j, i in aritmetic_midvalue.items():
    xx = i.split()
    if "ve" in xx or "veya" in xx:
        bbool = False
    else:
        for a in xx.copy():
            if a in remove_list:
                xx.remove(a)
        for x in xx:
            if x in init_var and x not in bool_dict_initvar:
                pass
            elif x in mid_var and mid_var.index(j)>mid_var.index(x) and bool_dict_midvar[x] == 0:       #### BOOLD??CTM??DVAR DA ZATEN 1 OLUNCA LOG??CLER??N SYNTAXI
                pass                                                                                    #### DOGRU OLUYOR.
            elif x in sayilar:                                                                          #### B??Z BURADA AR??TMET??C EXPRESS??ONLARI TEST ETT??K
                pass                                                                                    #### YAN?? LOG??C AR??TMET??C KARISIKSA VEYA DEF??NED PREV??OUS L??NES DEG??LSE HATA VER??YOR.
            elif re.search("^\d\.\d$|^\d$",x):
                pass
            else:
                bbool = False
#print(bbool)

sonuc_bool = 0
for i in sonuc_term:
    xx = i.split()
    if '+' in xx or '-' in xx or '*' in xx or 'arti' in xx or 'eksi' in xx or 'carpi' in xx:        ####SONUC LOG??C M?? AR??TMET??C M?? KONTROL??
        pass
    else:
        for a in xx.copy():
            if a in remove_list:                                    ####SONUC LOG??C M?? AR??TMET??C M?? KONTROL??
                xx.remove(a)
        for i in xx:                                                            ####SONUC LOG??C M?? AR??TMET??C M?? KONTROL??
            if i in bool_dict_initvar:
                sonuc_bool = 1
            elif i == "dogru" or i == "yanlis":
                sonuc_bool = 1                                                          ####SONUC LOG??C M?? AR??TMET??C M?? KONTROL??
            elif i in bool_dict_midvar and bool_dict_midvar[i] == 1:
                sonuc_bool = 1                                                          ####SONUC LOG??C M?? AR??TMET??C M?? KONTROL??

if sonuc_bool == 0:
    for i in sonuc_term:
        xx = i.split()
        for a in xx.copy():
            if a in remove_list:
                xx.remove(a)
        for x in xx:
            if x in init_var and x not in bool_dict_initvar:
                pass
            elif x in bool_dict_midvar and bool_dict_midvar[x] ==0:
                pass
            elif x in sayilar:                                            #### B??Z BURADA AR??TMET??C EXPRESS??ONLARI TEST ETT??K
                pass
            elif re.search("^\d\.\d$|^\d$",x):
                pass
            elif x.isnumeric():
                pass
            else:
                bbool = False
#print(bbool)

try:
    for a in mid_lines:
        for i in a.split():
            if i in keywords:
                pass
            elif i in mid_var or i in init_var:       ####YAZIM YANLISLARINI BULUYO
                pass
            elif re.search("^\d\.\d$",i):
                pass
            else:
                bbool = False
    #print(bbool)
except:
    pass
try:
    for a in sonuc_term:                                ####YAZIM YANLISLARINI BULUYO
        for i in a.split():
            if i in keywords:
                pass
            elif i in mid_var or i in init_var:
                pass                                       ####YAZIM YANLISLARINI BULUYO
            elif re.search("^\d\.\d$", i):
                pass
            else:
                bbool = False
    #print(bbool)                                    ####YAZIM YANLISLARINI BULUYO
except:
    pass
if bbool == True:
    ff.write("Here Comes the Sun")
else:
    ff.write("Dont Let Me Down")
f.close()
ff.close()





