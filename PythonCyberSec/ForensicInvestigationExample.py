import hashlib
# et python hash library

file1=open('oldfile.txt', 'r').read().strip().strip('-').encode('utf-8')#strip fjerner her ting, foerst lnje afsnit i den uden noget, efter bindestreg
file2=open('newfile.txt', 'r').read().strip().strip('-').encode('utf-8')#dette kan til dels, sammenlignes med hvad en it-sikkerheds efterforsker her ville goere
#da vi her snakker om et skadet system, og der skal tjekkes filer for at finde ud af hvad der er sket, og findes et spor, 
#finde ud af hvad der er aendret og om dataen muligvis stadig ligger i system, i form af ram eller lignende saa den kan rekonstrueres

#Vi vil med hash her tjekker om de filer er de samme.
hash1 = hashlib.md5(file1).hexdigest()#en mindre hex decimal repraesentation af hashen
hash2 = hashlib.md5(file2).hexdigest()

if(hash1==hash2):
    print('Duplicate.')
else:
    print('files dont match')

print(hash2)
print(hash1)