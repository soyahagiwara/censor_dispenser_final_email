import copy  # This will be later used to copy a list.
email_four = open("C:/Users/soyah/Desktop/python_codes/censor_dispenser/email_four.txt", "r").read()
proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset",
                  "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# This is the function for the final email.


def censor(email, proprietary_terms, negative_words):
    words = proprietary_terms + negative_words
    for word in words:
        email = email.replace(word, 'X'*len(word))
    # Now the email is censored. But we still need to blur words next to the censored ones.
    split_email = email.split('\n')
    for i in range(len(split_email)):
        split_email[i] = split_email[i].split(' ')
    # Now, if the email is "This is an example. \n This might make it easier to understand." and if we censor ["is", "understand"],
    # the split_email would be [['This', 'XX', 'an', 'exmaple'], ['This', 'XXXXX', 'make', 'it', 'easier', 'to', 'XXXXXXXXXX']].
    # Let's create a new list called new_split_email which will be modified to blur the words next to the already censored ones.
    # It is necessary to use copy.deepcopy to completely 'copy' split_mail. Using just '=' or copy() will result in referrencing split_mail.
    new_split_email = copy.deepcopy(split_email)
    for i in range(len(split_email)):
        for j in range(len(split_email[i])):
            if 'X' in split_email[i][j]:
                # The following indented codes are rather messy. But necessary to prevent IndexError.
                # For example, if we wanted to blur words next to 'XXXXXXXXXX' in the previous example, we would get an IndesError since that's the last word.
                if 0 <= j-1 and j+1 <= len(split_email[i])-1:
                    new_split_email[i][j-1] = 'X'*len(split_email[i][j-1])
                    new_split_email[i][j+1] = 'X'*len(split_email[i][j+1])
                elif 0 <= j-1:
                    new_split_email[i][j-1] = 'X'*len(split_email[i][j-1])
                elif j+1 <= len(split_email[i]) - 1:
                    new_split_email[i][j+1] = 'X'*len(split_email[i][j+1])
    # Now all we have to do is join new_split_email appropriately.
    for i in range(len(new_split_email)):  # First, lists within new_split_email will be joined by spaces
        new_split_email[i] = ' '.join(new_split_email[i])
    return '\n'.join(new_split_email)  # Then, join new_split_email with \n, and return it.


print(email_four)
print(censor(email_four, proprietary_terms, negative_words))
