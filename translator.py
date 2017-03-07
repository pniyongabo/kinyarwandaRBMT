kin = open("kinya.txt").readlines()
eng = open("eng.txt").readlines()

#print(len(kin))
#print(len(eng))

def clean(str):
    str = str.lower()
    str = str.strip()
    if "::" in str:
        temp = str.split("::")[0]
        return clean(temp)
    if "//" in str:
        temp = str.split("//")[0]
        return clean(temp)
    if "()" in str:
        temp = str.split("()")[0]
        return clean(temp)
    return str

eng2Kin = {}
kin2Eng= {}
for i in range(len(kin)):
    engStr, kinStr = clean(eng[i]), clean(kin[i])
    eng2Kin[engStr] = kinStr
    kin2Eng[kinStr] = engStr
    
import string
def remove_punctuation(str):
 replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
 text = str.translate(replace_punctuation)
 return text
    
def translate(sentence, transdict):
    sent = remove_punctuation(sentence)
    #print(sent)
    words = sent.split()
    #print(words)
    trans = [transdict[w] if w in transdict.keys() else w for w in words]
    #print(trans)
    print(' '.join(trans))

translate("hello, my name is patrick. good morning, let us go eat", eng2Kin)
translate("cats and dogs are both mammals", eng2Kin)
translate("God spends the day elsewhere but spends the night in Rwanda.", eng2Kin)
translate("laws are heavier than stones", eng2Kin)

print("___________________________________________")
print("___________________________________________")

testSentences = open("test.en").readlines()
for k in testSentences:
    translate(k, eng2Kin)