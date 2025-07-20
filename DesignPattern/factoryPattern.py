from abc import ABC, abstractmethod


class Notification(ABC):
    
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(f"Sending Email: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Sending Push: {message}")



class NotificationFactory:

    _registry = {}

    @classmethod
    def register_notification(cls, notify_type, notification_class):
        cls._registry[notify_type] = notification_class


    @classmethod
    def create_notification(cls, notify_type):
        if notify_type not in cls._registry:
            raise ValueError(f"Notification type: '{notify_type}' is not registered.")
        
        return cls._registry[notify_type]()
    
NotificationFactory.register_notification("email", EmailNotification)
NotificationFactory.register_notification("sms", SMSNotification)
NotificationFactory.register_notification("push", PushNotification)


if __name__ == "__main__":
    notify_type = "email"
    notifier = NotificationFactory.create_notification(notify_type)
    notifier.send(f"Your order is notified at {notify_type}")
    
