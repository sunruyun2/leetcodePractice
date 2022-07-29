# 1.tuition

def numUniqueEmails(emails:list[str])->int:
    newList = []
    for email in emails:
        email = email.split("@")

        while "." in email[0]:
            email[0] = email[0].replace(".","")

        if "+" in email[0]:
            stopindex = email[0].index("+")
            email[0] = email[0][:stopindex]

        email = "@".join(email)

        if email not in newList:
            newList.append(email)

    return len(newList)

print(numUniqueEmails(["alice@2ife.com","whatev...r@inf.com","fioenf+fien@fjie.com","fioenf+fn@fjie.com"]))
print(numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))


# 2. use set and string functions
def numUniqueEmails(emails:list[str])->int:
    unique = set()
    for e in emails:
        local, domain = e.split("@")
        local = local.split("+")[0]
        local = local.replace(".","")
        unique.add((local,domain))
    return len(unique)


# 3.use set and iterate the string

def numUniqueEmails(emails:list[str]):
    unique = set()
    for e in emails:
        i , local = 0, ""
        while e[i] not in ["+" , "@"]:
            if e[i] != ".":
                local+=e[i]
            i+=1

        if e[i]!= "@":
            i+=1

        domain = e[i+1:]

        unique.add((local,domain))
    return len(unique)

print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))