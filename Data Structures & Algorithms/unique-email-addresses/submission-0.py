class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique = set()

        for email in emails:
            email.strip() #trim leading and trailing whitespace
            parts = email.split("@") #break into parts by '@'
            domainName = parts[1]

            remPeriod = parts[0].replace('.', "")
            localName = remPeriod.split("+")[0]

            unique.add(localName + "@" + domainName)
        
        print(str(unique))
        return len(unique)