import cv2
cap = cv2.VideoCapture(0)
# cap.isOpened()
i=0
while(1):
    ret,frame=cap.read()
    cv2.imshow('capture',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):#按键盘q就停止拍照
        cv2.imwrite('/home/mao/mycroft-core/skills/take-item-photo-skill.maoyuejingxian/photo/' + str(i) + ".jpg", frame)
        i=i+1
        break

cap.release()
cv2.destroyAllWindows()

from mycroft import MycroftSkill, intent_file_handler
import cv2

class TakeItemPhoto(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('photo.item.take.intent')
    def handle_photo_item_take(self, message):
        self.speak_dialog('photo.item.take')
        cap = cv2.VideoCapture(0)
        # cap.isOpened()
        i=0
        while(1):
            ret,frame=cap.read()
            cv2.imshow('capture',frame)
            if cv2.waitKey(1)&0xFF==ord('q'):#按键盘q就停
                cv2.imwrite('/home/mao/mycroft-core/skills/take-item-photo-skill.maoyuejingxian/photo/+ str(i)' + ".jpg", frame)
                i = i+1
                break
        cap.release()
        cv2.destroyAllWindows()

def create_skill():
    return TakeItemPhoto()

