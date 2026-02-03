import re
import random


def create_emails(first_name: str, last_name: str, domain: str) -> str:
    """
    This function creates an email address by inserting a '.' between the
    first name and last name, and appending '@domain' at the end.

    :param first_name: First name of the user
    :type first_name: str
    :param last_name: Last name of the user
    :type last_name: str
    :param domain: The domain to be used in the email
    :type domain: str
    :return: The created email address
    :rtype: str
    """
    # Make names lowercase and remove non-alphanumeric characters
    first_name = re.sub(r"\W+", "", first_name.lower())
    last_name = re.sub(r"\W+", "", last_name.lower())

    local_part = ".".join([first_name, last_name])

    # Add a random 2-digit number to ensure uniqueness
    random_number = random.randint(10, 99)
    local_part += str(random_number)

    email = "@".join([local_part, domain.lower()])

    return email


if __name__ == "__main__":
    email_id = create_emails("KHUSHI", "SHARMA", "GMAIL.COM")
    print(email_id)
