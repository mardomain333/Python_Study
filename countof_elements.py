
n=[1,2,6,3,3,4,9,8,4,7,9,2,3,8,4,7]
hash_freq={}
hash_frequ={}
for a in n:
      if a not in hash_freq:
            hash_freq[a]=n.count(a)
print(hash_freq)

for i in n:
      if i not in hash_frequ:
            hash_frequ[i]=1
      else:
            hash_frequ[i]=hash_frequ[i]+1
print(hash_frequ)

st="agkjsdfkslfsj"
st2="dsflajdlaj"
dic={}
for a in st2:
      if a in st and a not in dic:
            dic[a]=st.count(a)
      elif a not in st:
            dic[a]=0
print(dic)