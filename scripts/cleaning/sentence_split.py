# import nltk

# nltk.download("punkt")

from nltk import sent_tokenize

test_sentence = "Syllad | The Rising Meghalaya June 22, 2022 Tang namar ka jingduh u transformer, ki paid nongthang bording ka shnong Syndai Mission bad ka Syndai Kmaishnong kila hap ban mad iaka jingeh da kaba shong haka jingdum khlem bording. “Ka jingsniew u transformer mynta la lai taiew ka la buh jingeh ia ka shnong ka thaw baroh kawei khamtam ki khynnah skul ki ba dei ki lawei jong ka ri bad ka shnong ka thaw namar ba kim ioh lad shuh ban pule kot ha ka por mynmiet,” la ong ki nongialam ka JSU Syndai Unit kiba la ujor sha u Executive Engineer Meghalaya Energy Corporation Ltd Jowai. Ki nongialam ka  JSU kiba kynthup ia u vice-president Bankerlang Lamurong bad u general secretary ka seng  u samla Heiplanmiki Tariang kila ai da ka dorkhat sha u EE ka MeECL haka sngi ba ar ban kyntu ia u ban maramot mardor ia u transformer ba pynioh bording ia kitei ki shnong ban myntoi ki paid nongthang bording. Ka JSU kala dawa ruh ban maramot iaki lain bad ki post elektrik kiba la kdor kiba buh jingma iaka leit ka wan ki nongshong shnong bad ki iing kiba don marjan uba pynpoi ding na ka shnong Syndai sha shnong Muktapur. Shuh shuh ka JSU Mihmyntdu kala ujor sha u Asst. Executive Engineer (MeECL), Jowai Distributor Sub-Division ban bujli ia u post ding elektrik ha Mihmyntdu Moowamon (Lum Phareng ). Une u post ulah ban khyllem ha kano kano ka por bad u lah ban wanrah jingma jingmynsaw ong ka JSU."

sentences = sent_tokenize(text=test_sentence)
for sentence in sentences:
    print(sentence, end="\n\n")
