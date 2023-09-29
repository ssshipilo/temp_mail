import requests
import time
import random
import uuid

class TempMail():

    def __init__(self):
        self.base_url = "https://api.internal.temp-mail.io/api/v2/email"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept-Language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,uk-UA;q=0.6,uk;q=0.5,kk-KZ;q=0.4,kk;q=0.3" 
            }
        self.email = ""


    def new_v1(self):
        """
        Create a new temporary mailbox
        """
        while True:
            try:
                time.sleep(1)
                response = requests.get(f"https://getnada.cc/api/domains/GwNvKEofrdyS7JTXCzHQ", headers=self.headers)
                response_data = response.json()

                domain_email = random.randint(0, len(response_data)-1)
                email = str(uuid.uuid1()).replace('-', '')
                new_email = email + "@" + response_data[domain_email]

                response = requests.get(f"https://getnada.cc/api/email/{new_email}/GwNvKEofrdyS7JTXCzHQ", headers=self.headers)
                if response.status_code == 200:
                    return new_email
                else:
                    continue
            except Exception as e:
                print(e)
                continue

    def messages_v1(self, new_email):
        link = f"https://getnada.cc/api/messages/{new_email}/GwNvKEofrdyS7JTXCzHQ"
        print(link)
        session = requests.Session()
        response = session.get(link, headers=self.headers)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)

            return response_data
    
    def new(self):
        """
        Create a new temporary mailbox
        """
        response = requests.post(f"{self.base_url}/new", headers=self.headers)
        response_data = response.json()
        email_address = response_data["email"]
        self.email = email_address

        return email_address

    def messages(self):
        """
        Get all messages
        """
        inbox_response = requests.get(f"{self.base_url}/{self.email}/messages", headers=self.headers)
        inbox_data = inbox_response.json()

        return inbox_data

    def delete(self):
        delete_response = requests.delete(f"{self.base_url}/{self.email}", headers=self.headers)
        if delete_response.status_code == 200:
            return True
        else:
            return False

if __name__ == "__main__":
    # temp_mail = TempMail()
    # new_email = temp_mail.new_v1()
    # print(new_email)

    # time.sleep(5)

    # while True:
    #     messages = temp_mail.messages_v1(new_email)
    #     # if messages and len(messages) > 0 and 'id' in messages[0]:
    #     #     print(f"[ID MESSAGE]: {messages[0]['id']}")
    #     #     print(messages[0]['body_html'])
    #     #     break
    #     time.sleep(5)

    temp_mail = TempMail()
    new_email = temp_mail.new()
    print(new_email)

    while True:
        messages = temp_mail.messages()
        if messages and len(messages) > 0 and 'id' in messages[0]:
            print(f"[ID MESSAGE]: {messages[0]['id']}")
            print(messages[0]['body_html'])
            break
        time.sleep(5)