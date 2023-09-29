# Temp mail

A small code to use temporary mail services. 

I'm sure you have occasions to automate processes to use mail, so I suggest not a bad alternative instead of resetting a new account in some mail service

## Example:
```python
from temp_mail import TempMail

mail = TempMail()
temp_mail = mail.new()

# you code ...

while True:
	messages = mail.messages()
	print("Wait message ...")
	if messages and len(messages) > 0 and 'id' in messages[0]:
		print(messages[0]['body_html'])
		break
	time.sleep(3)
```

