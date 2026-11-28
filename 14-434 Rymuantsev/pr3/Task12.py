class Notification:
    def __init__(self, message):
        self.message = message
    def send(self):
        return self.message

class EmailNotification(Notification):
    def send(self):
        return self.message
    
class SmsNotification(Notification):
    def send(self):
        return self.message
    
class PushNotification(Notification):
    def send(self):
        return self.message

messages = [Notification("У вас просрочка по кредиту"), EmailNotification("Ваша почта скоро будет арестована0"),
            SmsNotification("Ваш телефон скоро конфискуют"), PushNotification("У ТЕБЯ СКОРО ХАТУ ЗАБЕРУТ")]

def broadcast(messages):
    for n in messages: 
        print(n.send())
# понятия не имею что тут коментировать, я просто добавил такой же дочерний подкласс 

input("Нажмите любую кнопку чтобы запустить колекторов")
broadcast(messages)