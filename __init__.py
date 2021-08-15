from mycroft import MycroftSkill, intent_file_handler


class TakeItemPhoto(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('photo.item.take.intent')
    def handle_photo_item_take(self, message):
        self.speak_dialog('photo.item.take')


def create_skill():
    return TakeItemPhoto()

