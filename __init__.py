from mycroft import MycroftSkill, intent_file_handler
import cv2
import os
from mycroft.util import LOG
import threading
from multiprocessing import Process
import time

#######
class Day2WorkshopSkill(MycroftSkill): 
    def __init__(self):
        MycroftSkill.__init__(self)
        self.log.info(LOGSTR + "_init_ Day2WorkshopSkill")

    '''def initialize(self):
        self.log.info(LOGSTR + "initialize Day2WorkshopSkill)
        #self.register_intent_file('definition.of.ESA.intent', self.handle_definition)
        #self.register_intent_file('objectives.of.ESA.intent', self.handle_objectives)'''

    ########################using Padatious intent parser###########################
    @intent_handler('definition.esa.intent')
    def handle_definition(self, message):
        #self.speak('This Easy Shopping Agent serves blind people as a personal shopping assistant to help them locate desired goods and make them enjoy shopping. To large extent, the can partly replace the eyes by voice perceptions.')
        self.speak_dialog('definition.dialog')

    @intent_handler('objectives.esa.intent')
    def handle_objectives(self, message):
        #self.speak('This ESA virtual assisstant leverages mycroft voice assistant platform and computer vision technology. ESA brings blind people a much easier shopping experience.')
        self.speak_dialog('objectives.dialog')

    '''def stop(self):
        pass'''
    
    #############################using Adapt intent parser#####################

def create_skill():
    return Day2WorkshopSkill()

'''def take_photo():
    LOG.error('========================>>>>>>>>>>>>> take photo process start')
    cap = cv2.VideoCapture(0)
    # time.sleep(0.5)
    # ret, frame = cap.read()
    # cv2.imshow("Capture",frame)
    # cv2.imwrite('/home/parallels/mycroft-core/skills/take-item-photo-skill.maoyuejingxian/photo/' +"1.jpg", frame)
    # cap.release()
    # cv2.destroyAllWindows()
    # os._exit(0)

    # while(1):
    #     #get a frame
    #     ret, frame = cap.read()
    #     #show a frame
    #     cv2.imshow('capture', frame)
    #     cv2.imwrite('/home/parallels/mycroft-core/skills/take-item-photo-skill.maoyuejingxian/photo/'+ str(i) +".jpg", frame)
    #     time.sleep(1.0)
    #     i+=1
    #     break

    # cap.release()
    # cv2.destroyAllWindows()
    # LOG.error('========================>>>>>>>>>>>>>>> take photo process end')
    # os._exit(0)

    flag = cap.isOpened()
    index = 1
    while(flag):
        ret, frame = cap.read()
        cv2.imshow("Capture",frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):    
            cv2.imwrite("/home/parallels/mycroft-core/skills/take-item-photo-skill.maoyuejingxian/photo/" + str(index) + ".jpg", frame)
            index += 1
        elif k == ord('q'):     #按下q键，程序退出
            break
    cap.release()
    cv2.destroyAllWindows()
    os._exit(0)

class TakeItemPhoto(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('photo.item.take.intent')
    def handle_photo_item_take(self, message):
     
        self.speak_dialog('photo.item.take')
        take_photo_process = Process(target=take_photo)
        take_photo_process.start()
        take_photo_process.join()

        # cap = cv2.VideoCapture(0)
        # # cap.isOpened()
        # i=0
        # while(1):
        #     ret,frame=cap.read()
        #     cv2.imshow('capture',frame)
        #     if cv2.waitKey(0)&0xFF==ord('q'):#按键盘q就停
        #         cv2.imwrite('/home/parallels/mycroft-core/skills/take-item-photo-skill.maoyuejingxian/photo/'+ str(i) + ".jpg", frame)
        #         i = i+1
        #         break
        
        # cap.release()
        # cv2.destroyAllWindows()
        # os._exit(0)

    def stop(self):
        pass


def create_skill():
    return TakeItemPhoto()'''

