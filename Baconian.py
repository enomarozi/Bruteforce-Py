import baconianlib

baconIJUV = baconianlib.baconianIJUV
baconDist = baconianlib.baconianDistric
def encrypt():
    text = "ENOMAROZI"
    result_allIJUV = " ".join([baconIJUV[i] for i in text if i in baconIJUV.keys()])
    result_allDistric = " ".join([baconDist[i] for i in text if i in baconDist.keys()]) 
    print("baconIJUV --> "+result_allIJUV)
    print("baconDistric --> "+result_allDistric)
def decrypt():
    text = "AABAAABBABABBBAABBAAAAAAABAAABABBBABBAABABAAA"
    result = [text[:i][-5:] for i in range(5,len(text)+5,5)]
    result_allIJUV = ""
    result_allDistric = ""
    for i in result:
        for j in baconIJUV.keys():
            if i == baconIJUV[j]:
                result_allIJUV += j
    for i in result:
        for j in baconDist.keys():
            if i == baconDist[j]:
                result_allDistric += j
    print("baconIJUV --> "+result_allIJUV)
    print("baconDistric --> "+result_allDistric)           
