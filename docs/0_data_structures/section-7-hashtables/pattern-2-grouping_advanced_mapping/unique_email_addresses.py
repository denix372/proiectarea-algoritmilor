from collections import defaultdict

class Solution:
    def num_unique_emails(self, emails: list[str]) -> int:
        d = defaultdict(set)
        for address in emails:
            name, email = address.split('@')
            parsed_name = name.replace('.', '').split('+')[0]

            d[email].add(parsed_name)
        return sum(len(x) for x in d.values())
emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails))