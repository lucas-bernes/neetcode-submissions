class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_receivers = set()
        for email in emails:

            split_email = email.split("@")
            local_name = split_email[0]
            domain = split_email[1]

            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".","")

            info = {}
            formatted_email = local_name + "@" + domain
            email_receivers.add(formatted_email)
        return len(email_receivers)

            