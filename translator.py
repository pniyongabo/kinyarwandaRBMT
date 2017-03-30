kin = open("kinya.txt").readlines()
eng = open("eng.txt").readlines()
adjs = [k.strip().lower() for k in open("adj.txt").readlines()]

#print(len(kin))
#print(len(eng))

engWordsToIgnore = []


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
    eng2Kin[engStr+"s"] = kinStr # plural forms of names and third person
                # a more accurate fix needs to be added to the data files
    kin2Eng[kinStr] = engStr
    
for w in engWordsToIgnore:
    eng2Kin[w] = ""
import re 
def addSpaces(str):
    str = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", str)    
    return str;
import string
def remove_punctuation(str):
 replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
 text = str.translate(replace_punctuation)
 return text
    
def translate(sentence, transdict):
    sent = addSpaces(sentence)
    #sent = remove_punctuation(sentence).lower()
    
    words = [clean(word) for word in sent.split(" ")]
    
    i = 0
    while i < len(words)-2:
        if words[i] in adjs:
            current = words[i]
            temp = words[i+1]
            words[i] = temp
            words[i+1] = current
            i = i+2
        else:
            i = i+1
    #print(words)
    
    trans = [transdict[w] if w in transdict.keys() else w for w in words]
    
    print(' '.join(trans))
    return (' '.join(trans))

translate("Hello, my name is Patrick. Good morning!", eng2Kin)
translate("cats and dogs are both mammals", eng2Kin)
translate("God spends the day elsewhere but spends the night in Rwanda.", eng2Kin)
translate("laws are heavier than stones", eng2Kin)

print("___________________________________________")
print("___________________________________________")

testSentences = open("test.en").readlines()
testOutput =  open("test.out", "w")
for k in testSentences:
    testOutput.write(translate(k, eng2Kin)+"\n")

testOutput.close()