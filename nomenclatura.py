import random

bruh = ["litio Li 1 Li2O ossido di dilitio ossido di litio",
"sodio Na 1 Na2O ossido di disodio ossido di sodio",
"potassio K 1 K2O ossido di dipotassio ossido di potassio",
"argento Ag 1 Ag2O ossido di diargento ossido di argento",
"magnesio Mg 2 MgO ossido di magnesio ossido di magnesio",
"calcio Ca 2 CaO ossido di calcio ossido di calcio",
"stronzio Sr 2 SrO ossido di stronzio ossido di stronzio",
"bario Ba 2 BaO ossido di bario ossido di bario",
"zinco Zn 2 ZnO ossido di zinco osiido di zinco",
"cadmio Cd 2 CdO ossido di cadmio ossido di cadmio",
"alluminio Al 3 Al2O3 triossido di dialluminio ossido di alluminio",
"bismuto Bi 3 Bi2O3 triossido di dibismuto ossido bismutoso",
"bismuto Bi 5 Bi2O5 pentaossido di dibismuto ossido bismutico",
"stagno Sn 2 SnO ossido di stagno ossido stannoso",
"stagno Sn 4 Sn2O4 tetraossido di distagno ossido stannico",
"piombo Pb 2 PbO ossido di piombo ossido plomboso",
"piombo Pb 4 Pb2O4 tetraossido di dipiombo ossido plumbico",
"mercurio Hg 1 Hg2O ossido di dimenrcurio ossido mercurioso",
"mercurio Hg 2 HgO ossido di mercurio ossido mercurico",
"rame Cu 1 Cu2O ossido di dirame ossido rameoso",
"rame Cu 2 CuO ossido di rame ossido rameico",
"cromo Cr 2 CrO ossido di cromo ossido cromoso",
"cromo Cr 3 Cr2O3 triossido di dicromo ossido cromico",
"cromo Cr 6 Cr2O6 esaossido di dicromo anidride cromica",
"manganese Mn 2 MnO ossido di manganese ossido manganoso",
"manganese Mn 3 Mn2O3 triossido di dimanganese ossido manganico",
"manganese Mn 4 Mn2O4 tetraossido di dimanganese biossido di manganese",
"manganese Mn 6 Mn2O6 esaossido di dimanganese anidride manganica",
"manganese Mn 7 Mn2O7 eptaossido di dimanganese anidride permanganica",
"ferro Fe 2 FeO ossido di ferro ossido ferroso",
"ferro Fe 3 Fe2O3 triossido diferro ossido ferrico",
"cobalto Co 3 Co2O3 triossido di dicobalto ossido cobaltico",
"nichel Ni 2 NiO ossido di nichel ossido nicheloso",
"nichel Ni 3 Ni2O3 triossido di dinichel ossido nichelico",
"oro Au 1 Au2O ossido di dioro ossido auroso",
"oro Au 3 Au2O3 triossido di dioro ossido aurico",
"platino Pt 2 PtO ossido di platino ossido platinoso",
"platino Pt 4 Pt2O4 tetraossido di platino ossido platinico",
"fluoro F 1 F2O ossido di difloro anidride fluorica",
"cloro Cl 1 Cl2O ossido di dicloro anidride ipoclorosa",
"cloro Cl 3 Cl2O3 triossido di dicloro anidride clorosa",
"cloro Cl 5 Cl2O5 pentaossido di dicloro anidride clorica",
"cloro Cl 7 Cl2O7 eptaossido di dicloro anidride perclorica",
"bromo Br 1 Br2O ossido di dibromo anidride ipobromosa",
"bromo Br 3 Br2O3 triossido di dibromo anidride bromosa",
"bromo Br 5 Br2O5 pentaossido di dibromo anidride bromica",
"bromo Br 7 Br2O7 eptaossido di dibromo anidride perbromica",
"iodio I 1 I2O ossido di diiodio anidride ipoiodosa",
"iodio I 3 I2O3 triossido diiodio anidride iodosa",
"iodio I 5 I2O5 pentaossido di diiodio anidride iodica",
"iodio I 7 I2O7 eptaossido di diiodio anidride periodica",
"zolfo S 4 S2O4 tetraossido di dizolfo anidride solforosa",
"zolfo S 6 S2O6 esaossido di dizolfo anidride solforica",
"azoto N 3 N2O3 triossido di diazoto anidride nitrosa",
"azoto N 5 N2O5 pentaossido di diazoto anidride nitrica",
"fosforo P 3 P2O3 triossido di difosforo anidride fosforosa",
"fosforo P 5 P2O5 pentaossido di difosforo anidride fosforica",
"arsenico As 3 As2O3 triossido di diarsenico anidride arseniosa",
"arsenico As 5 As2O5 pentaossido di diarsenico anidride arsenica",
"antimonio Sb 3 Sb2O3 triossido di diantimonio anidride antimoniosa",
"antimonio Sb 5 Sb2O5 penta ossido di diantimonio anidride antimonica",
"carbonio C 4 C2O4 ossido di di carbono ossido di carbonio",
"silicio Si 4 Si2O4 tetraossido di disilicio anidride silicica",
"boro B 3 B2O3 triossido di diboro anidride borica",
"ossigeno O 2 O2 biossido ossigeno"]
"idrogeno H 1 H2O ossido diidrogeno ossido di idrogeno",
resto = ["a) NH3 idruro covalente triidruro di azoto ammoniaca",
"b) KCl sale binario cloruro di potassio cloruro di potassio",
"c) AsH3 idruro covalente triidruro di arsenico arsina",
"d) BaH2 idruro metallico diidruro di bario idruro di bario",
"e) HCl idracido cloruro di idrogeno acido cloridrico",
"f) BF3 sale binario trifluoruro di boro fluoruro di boro",
"g) LiH idruro metallico idruro di litio idruro di litio",
"h) FeBr3 sale binario tribromuro di ferro bromuro ferrico",
"i) SiH4 idruro covalente tetraidruro di silicio idruro di silicio",
"j) HBr idracido bromuro di idrogeno acido bromidrico",
"k) HI idracido ioduro di idrogeno acido iodidrico",
"l) CuH idruro metallico monoidruro di rame idruro rameoso",
"m) PH3 idruro covalente triidruro di fosforo fosfina",
"n) ZnH2 idruro metallico diidruro di zinco idruro di zinco",
"o) NaF sale binario fluoruro di sodio fluoruro di sodio",
"p) CaH2 idruro metallico diidruro di calcio idruro di calcio",
"q) PbI2 sale binario diioduro di piombo ioduro piomboso",
"r) K2S sale binario solfuro di dipotassio solfuro di potassio",
"s) CH4 idruro covalente tetraidruro di carbonio idruro di carbonio",
"t) H2S idracido solfuro di diidrogeno acido solfidrico",
"u) HF idracido fluoruro di idrogeno acido fluoridrico",
"v) SiCl4 sale binario tetracloruro di silicio cloruro di silicio",
"w) NiO ossido basico monossido di nichel ossido nicheloso",
"x) CS2 sale binario disolfuro di carbonio solfuro di carbonio",
"/ H2SO3 acido solforoso acido triossosolforico",
"/ H2S acido solfidrico solfuro di diidrogeno",
"/ HClO acido ipocloroso acido monossoclorico",
"/ H3PO4 acido fosforico acido tetrossofosforico",
"/ H2CrO4 acido cromico acido tetrossocromico",
"/ HNO3 acido nitrico acido triossonitrico",
"/ HF acido fluoridrico fluoruro di idrogeno",
"/ H2O2 acqua ossigenata perossido di idrogeno",
"/ NH3 ammoniaca triidruro di azoto",
"/ BaH2 idruro di bario diidruro di bario",
"/ K2O2 perossido di potassio perossido di potassio",
"/ Cl2O5 anidride clorica pentossido di dicloro",
"/ Mn2O7 anidride permanganica eptossido di dimanganese",
"/ PH3 fosfina triidruro di fosforo",
"a) CO2 ossido acido diossido di carbonio anidride carbonica",
"b) CuO ossido basico monossido di rame ossido rameico",
"c) SrO ossido basico ossido di stronzio ossido di stronzio",
"d) SO2 ossido acido diossido di zolfo anidride solforosa",
"e) P2O5 ossido acido pentaossido di difosforo anidride fosforica",
"f) H2O2 perossido perossido di idrogeno acqua ossigenata",
"g) Ni2O3 ossido basico triossido di dinichel ossido nichelico",
"h) Na2O2 perossido perossido di sodio perossido di sodio",
"i) Cl2O ossido acido monossido di dicloro anidride ipoclorosa",
"a) NaCl cloruro di sodio cloruro di sodio",
"b) H2O ossido di diidrogeno acqua",
"c) Na2O2 perossido di sodio perossido di sodio",
"d) SiO2 diossido di silicio anidride silicica",
"e) XeF6 esafluoruro di xenon fluoruro di xenon",
"f) AsH3 triidruro di arsenico arsina",
"g) H2S solfuro di diidrogeno acido solfidrico",
"h) CH4 tetraidruro di carbonio metano",
"i) N2O3 triossido di diazoto anidride nitrosa",
"l) KCN cianuro di potassio cianuro di potassio",
"m) LiH idruro di litio idruro di litio",
"n) NH3 triidruro di azoto ammoniaca",
"o) PH3 triidruro di fosforo fosfina",
"p) Cu2O monossido di dirame ossido rameoso",
"q) HgS monosolfuro di mercurio solfuro mercurico",
"r) H2O2 perossido di idrogeno acqua ossigenata",
"s) CS2 disolfuro di carbonio solfuro carbonico",
"t) CaO ossido di calcio ossido di calcio",
"a) H2CO3 acido carbonico acido triossocarbonico",
"b) HNO2 acido nitroso acido diossonitrico",
"c) HNO3 acido nitrico acido triossonitrico",
"d) H2SO3 acido solforoso acido triossosolforico",
"e) H2SO4 acido solforico acido tetrossosolforico",
"f) HClO acido ipocloroso acido monossoclorico",
"g) HClO2 acido cloroso acido diossoclorico",
"h) HClO3 acido clorico acido triossoclorico",
"i) HClO4 acido perclorico acido tetrossoclorico"]


bruta = []
iupaac = []
trad = []

for frase in bruh:
    pezzi = frase.split()
    bruta.append(pezzi[3])
    if "di" in pezzi:
        iupaac.append(pezzi[4]+" di "+pezzi[6])
        pezzi.remove("di")
        if  "di" in pezzi:
            
            trad.append(pezzi[6]+" di "+pezzi[8])
        else:
            trad.append(pezzi[6]+" " +pezzi[7])
    else:
        trad.append(pezzi[len(pezzi)-2]+" " +pezzi[len(pezzi)-1])
        iupaac.append(pezzi[len(pezzi)-4]+" " +pezzi[len(pezzi)-3])
        
for frase in resto:
    pezzi = frase.split()
    bruta.append(pezzi[1])
    if "di" in pezzi:
        iupaac.append(pezzi[pezzi.index("di")-1]+" di "+pezzi[pezzi.index("di")+1])
        pezzi.remove("di")
        if  "di" in pezzi:
            trad.append(pezzi[len(pezzi)-3]+" di "+pezzi[len(pezzi)-1])
        else:
            trad.append(pezzi[len(pezzi)-2]+" " +pezzi[len(pezzi)-1])
    else:
        trad.append(pezzi[len(pezzi)-2]+" " +pezzi[len(pezzi)-1])
        iupaac.append(pezzi[len(pezzi)-4]+" " +pezzi[len(pezzi)-3])

punteggio = 0

while True:
    domanda = random.randint(0,len(bruta))
    quale = random.randint(0,3)
    if quale == 0:
        print(bruta[domanda])
        risposta1= input("dimmi la nom iupac\n")
        risposta2 = input("dimmi la nom tradizionale\n")
        if risposta1 == iupaac[domanda]:
            print("nom iupac giusta!")
            punteggio +=1
        else:
            print("sbagliata! quella giusta era: " + iupaac[domanda])
            break
        if risposta2 == trad[domanda]:
            print("nom trad giusta!")
            punteggio +=1
        else:
            print("sbagliata! quella giusta era: " + trad[domanda])
            break
    
    if quale == 1:
        print(iupaac[domanda])
        risposta1= input("dimmi la bruta\n")
        risposta2 = input("dimmi la nom tradizionale\n")
        if risposta1 == bruta[domanda]:
            print("bruta giusta!")
            punteggio +=1
        else:
            print("sbagliata! quella giusta era: " + bruta[domanda])
            break
        if risposta2 == trad[domanda]:
            print("nom trad giusta!")
            punteggio +=1
        else:
            print("sbagliata! quella giusta era: " + trad[domanda])
            break

    if quale == 2:
        print(trad[domanda])
        risposta1= input("dimmi la nom iupac\n")
        risposta2 = input("dimmi la bruta\n")
        if risposta1 == iupaac[domanda]:
            print("nom iupac giusta!")
            punteggio +=1
        else:
            print("sbagliata! quella giusta era: " + iupaac[domanda])
            break
        if risposta2 == bruta[domanda]:
            print("bruta giusta!")
            punteggio +=1
        else:
            print("sbagliata! quella giusta era: " + bruta[domanda])
            break
    
    print("\n")

print("punteggio: " + str(punteggio))
x = input()

    