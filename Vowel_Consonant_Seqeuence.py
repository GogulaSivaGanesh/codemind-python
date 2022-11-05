a=input()
vo='aeiou'
ou=''
for i in a:
    if i in vo:
        if len(ou)==0 or ou[len(ou)-1]=='C' :
            ou+='V'
    else:
        if len(ou)==0 or ou[len(ou)-1]=='V':
            ou+='C'
print(ou)
        