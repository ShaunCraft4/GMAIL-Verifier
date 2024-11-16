sc="!#$%^&*[]{}()"
dom=["com","edu","gov","net","org"]
Catch=0
mail=input("Enter mail address: ")
mail=mail.lower()
if mail.count("@")==1:
        masterlist=[]
        mailsplit=mail.split("@")
        mailsplit2=mailsplit[1]
        if mailsplit2.count(".")==1:
            mailsplit2=mailsplit2.split(".")
            masterlist.append(mailsplit[0])
            masterlist.extend(mailsplit2)
            print(masterlist)
            if len(masterlist[0])>6 and len(masterlist[0])<64 and len(masterlist[1])>2 and len(masterlist[1])<63 and " " not in mail and masterlist[2] in dom:
                if masterlist[0][0]!="'" and masterlist[0][-1]!="'":
                    Con=False
                    for i in sc:
                        if i in masterlist[0] or i in masterlist[1]:
                            Con=False
                            break
                    if Con==True and masterlist[0][0]!="." and masterlist[0][-1]!="." and ".." not in masterlist[0]:
                            Catch+=1
                else:
                    Catch+=1
if Catch==1:
    print("Valid email address")
else:
    print("Invalid email address")
                        




