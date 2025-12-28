import time
phrase="python is the best coding language"

word_count=len(phrase.split())
choice=input("Can we start")
if choice == "":
    start=time.time()
    action=input("start typing ...")
    end=time.time()

total_time=(end-start)/60
wpm=round(word_count/total_time,2)
if action==phrase:
    print(f"u done it wpm={wpm}")
else:
    print("wrong sentance..")
