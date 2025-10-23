import cv2
import mediapipe as mp
import time


camera = cv2.VideoCapture(0) # (0) - camera index

#попадания точки(пальца) в прямоугольник
def point_in_rect(cx, cy, x1, y1, x2, y2):
    return x1 <= cx <= x2 and y1 <= cy <= y2

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils  # для рисования линий

#styles for lines
line_color = (0, 0, 255)   # красные линии (BGR)
line_thickness = 2          # толщина линий
circle_color = (0, 255, 0) # зелёные кружки на суставах
circle_radius = 3    

firstNum = None
secondNum = None
waitingForSecond = False
res = 0

if not camera.isOpened():
    print("cant find camera")
    exit()

# create new window for cams
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)



try:
    while True:
        success, img = camera.read()

      


        # mirror cam
        img = cv2.flip(img, 1)



       


    


    
        h, w, c = img.shape 

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if results.multi_hand_landmarks:
            text_y = 20  # стартовая позиция текста сверху
            for hand_idx, handLms in enumerate(results.multi_hand_landmarks):
                cv2.putText(img, f"Hand {hand_idx+1}:", (10, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                text_y += 15
                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.putText(img, f"{id}: ({cx},{cy})", (10, text_y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                    text_y += 15
                text_y += 10  # небольшой отступ между руками

                #draw lines
                mpDraw.draw_landmarks(
                    img, 
                    handLms, 
                    mpHands.HAND_CONNECTIONS,
                    mpDraw.DrawingSpec(color=circle_color, thickness=circle_radius, circle_radius=circle_radius),
                    mpDraw.DrawingSpec(color=line_color, thickness=line_thickness)
)
       
        #проверка пападания 
        if results.multi_hand_landmarks:

         


            for hand_idx, handLms in enumerate(results.multi_hand_landmarks):
                #left or right hand
                hand_label = results.multi_handedness[hand_idx].classification[0].label
                lm = handLms.landmark[8]  # указательныц палец [8]
                cx, cy = int(lm.x * w), int(lm.y * h)

                #left hand
                if hand_label == "Left" and not waitingForSecond:
             
                   
                    if point_in_rect(cx, cy, 100, 100, 200, 200): 
                        firstNum = 1
                    elif point_in_rect(cx, cy, 210, 100, 310, 200):
                        firstNum = 2
                    elif point_in_rect(cx, cy, 320, 100, 420, 200):
                        firstNum = 3
                    elif point_in_rect(cx, cy, 430, 100, 530, 200):
                        firstNum = 4
                    elif point_in_rect(cx, cy, 540, 100, 640, 200):
                        firstNum = 5
                    elif point_in_rect(cx, cy, 650, 100, 750, 200):
                        firstNum = 6
                    elif point_in_rect(cx, cy, 760, 100, 860, 200):
                        firstNum = 7
                    elif point_in_rect(cx, cy, 870, 100, 970, 200):
                        firstNum = 8
                    elif point_in_rect(cx, cy, 980, 100, 1080, 200):
                        firstNum = 9
                    
                    
                    if firstNum is not None:
                        print("firstNum", firstNum)
                       

  
                
                #right hand
                if hand_label == "Right" and firstNum is not None:
               
                    if point_in_rect(cx, cy, 100, 100, 200, 200): 
                        secondNum = 1
                    elif point_in_rect(cx, cy, 210, 100, 310, 200):
                        secondNum = 2
                    elif point_in_rect(cx, cy, 320, 100, 420, 200):
                        secondNum = 3
                    elif point_in_rect(cx, cy, 430, 100, 530, 200):
                        secondNum = 4
                    elif point_in_rect(cx, cy, 540, 100, 640, 200):
                        secondNum = 5
                    elif point_in_rect(cx, cy, 650, 100, 750, 200):
                        secondNum = 6
                    elif point_in_rect(cx, cy, 760, 100, 860, 200):
                        secondNum = 7
                    elif point_in_rect(cx, cy, 870, 100, 970, 200):
                        secondNum = 8
                    elif point_in_rect(cx, cy, 980, 100, 1080, 200):
                        secondNum = 9

                    if secondNum is not None:
                        res = firstNum + secondNum
                        print("Сумма:", res)
                        # сброс
                        firstNum = None
                        secondNum = None
                        waitingForSecond = False
                
                       
          

           
                



                


       



                        
                       

                      
                   

          

         
        #numbers
        cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 2)
        cv2.putText(img, "1", (140, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.rectangle(img, (210, 100), (310, 200), (255, 0, 0), 2)
        cv2.putText(img, "2", (250, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.rectangle(img, (320, 100), (420, 200), (255, 0, 0), 2)
        cv2.putText(img, "3", (360, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.rectangle(img, (430, 100), (530, 200), (255, 0, 0), 2)
        cv2.putText(img, "4", (470, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.rectangle(img, (540, 100), (640, 200), (255, 0, 0), 2)
        cv2.putText(img, "5", (580, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.rectangle(img, (650, 100), (750, 200), (255, 0, 0), 2)
        cv2.putText(img, "6", (690, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.rectangle(img, (760, 100), (860, 200), (255, 0, 0), 2)
        cv2.putText(img, "7", (800, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.rectangle(img, (870, 100), (970, 200), (255, 0, 0), 2)
        cv2.putText(img, "8", (910, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.rectangle(img, (980, 100), (1080, 200), (255, 0, 0), 2)
        cv2.putText(img, "9", (1020, 170), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

      



        #+++++++++

        # рисуем прямоугольник
        cv2.rectangle(img, (1130, 300), (1230, 400), (255, 0, 0), 2)  # прямоугольник
        cv2.putText(img, str(res), (1150, 370), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)  # текс





       
        

        cv2.imshow("Image", img)

        # press q to leave
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # exit
    camera.release()
    cv2.destroyAllWindows()
    cv2.waitKey(100)  
