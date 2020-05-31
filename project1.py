import numpy as np
import cv2
import pyautogui




capt = cv2.VideoCapture(0)
count=0

while(1):
    
    # image reading
    r, shape = capt.read()
    
    #processing
    shape = cv2.flip(shape,1)
    
    
    global gx
    global gy
    global prevArea,newArea
    prevArea,newArea=0,0
    
    #identification of yellow color in frame.
    hsv = cv2.cvtColor(shape, cv2.COLOR_BGR2HSV)
    lowYellow = np.array([15,140,142])#changes hsv values as per light condition.
    upYellow = np.array([83,250,250])  
    
    masking = cv2.inRange(hsv, lowYellow, upYellow)
    blur = cv2.medianBlur(masking, 15)
    blur = cv2.GaussianBlur(blur , (5,5), 0)
    thres = cv2.threshold(blur, 0, 275, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    
    cv2.imshow("masking",masking)
    #find contours in frame
    contours, hierarchy = cv2.findContours(masking,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
            
    #function to determine which key is pressed based on the center of the contour(yellow paper)
    def key(gx,gy):
        if gy>50 and gy<100:
            if gx>50 and gx<100:
                print("1")
                pyautogui.press("1")
            elif gx>100 and gx<150:
                print("2")
                pyautogui.press("2")
            elif gx>150 and gx<200:
                print("3")
                pyautogui.press("3")
            elif gx>200 and gx<250:
                print("4")
                pyautogui.press("4")
            elif gx>250 and gx<300:
                print("5")
                pyautogui.press("5")
            elif gx>300 and gx<350:
                print("6")
                pyautogui.press("6")
            elif gx>350 and gx<400:
                print("7")
                pyautogui.press("7")
            elif gx>400 and gx<450:
                print("8")
                pyautogui.press("8")
            elif gx>450 and gx<500:
                print("9")
                pyautogui.press("9")
            elif gx>500 and gx<550:
                print("0")
                pyautogui.press("0")
        elif gy>100 and gy<150:
            if gx>50 and gx<100:
                print("q")
                pyautogui.press("q")
            elif gx>100 and gx<150:
                print("w")
                pyautogui.press("w")
            elif gx>150 and gx<200:
                print("e")
                pyautogui.press("e")
            elif gx>200 and gx<250:
                print("r")
                pyautogui.press("r")
            elif gx>250 and gx<300:
                print("t")
                pyautogui.press("t")
            elif gx>300 and gx<350:
                print("y")
                pyautogui.press("y")
            elif gx>350 and gx<400:
                print("u")
                pyautogui.press("u")
            elif gx>400 and gx<450:
                print("i")
                pyautogui.press("i")
            elif gx>450 and gx<500:
                print("o")
                pyautogui.press("o")
            elif gx>500 and gx<550:
                print("p")
                pyautogui.press("p")
        elif gy>150 and gy<200:
            if gx>50 and gx<100:
                print("a")
                pyautogui.press("a")
            elif gx>100 and gx<150:
                print("s")
                pyautogui.press("s")
            elif gx>150 and gx<200:
                print("d")
                pyautogui.press("d")
            elif gx>200 and gx<250:
                print("f")
                pyautogui.press("f")
            elif gx>250 and gx<300:
                print("g")
                pyautogui.press("g")
            elif gx>300 and gx<350:
                print("h")
                pyautogui.press("h")
            elif gx>350 and gx<400:
                print("j")
                pyautogui.press("j")
            elif gx>400 and gx<450:
                print("k")
                pyautogui.press("k")
            elif gx>450 and gx<500:
                print("l")
                pyautogui.press("l")
        elif gy>200 and gy<250:
            if gx>50 and gx<100:
                print("z")
                pyautogui.press("z")
            elif gx>100 and gx<150:
                print("x")
                pyautogui.press("x")
            elif gx>150 and gx<200:
                print("c")
                pyautogui.press("c")
            elif gx>200 and gx<250:
                print("v")
                pyautogui.press("v")
            elif gx>250 and gx<300:
                print("b")
                pyautogui.press("b")
            elif gx>300 and gx<350:
                print("n")
                pyautogui.press("n")
            elif gx>350 and gx<400:
                print("m")
                pyautogui.press("m")
        elif gy>250 and gy<300:
            if gx>100 and gx<450:
                print("space")
                pyautogui.press("space")
            elif gx>450 and gx<550:
                print("Backspace")
                pyautogui.press("backspace")
    
    cv2.drawContours(shape,contours,-1,(0,255,0),2)
    
    
    

    
    if len(contours)>0:
        cnt=max(contours,key=cv2.contourArea)
        if cv2.contourArea(cnt)>600 and cv2.contourArea(cnt)<1200:
             M = cv2.moments(cnt)
             gx = int(M['m10']/M['m00'])
             gy = int(M['m01']/M['m00'])
             #print ("Centroid = ", cx, ", ", cy)
             newArea=cv2.contourArea(cnt)
             #print("new area ",new_area)
             cv2.circle(shape,(gx,gy),1,(0,0,255),2)
             if count==0:
                 prevArea=newArea
                 #print("in count==0   ",count)
                 
             count=count+1
             #print(count)
             if count==20:
                 count=0
                 diffArea=newArea-prevArea
                 if diffArea>500 and diffArea<1200:
                    print("diff- ",diffArea)
                    key(gx,gy)
                
        
        
    #display the keyboard in the screen        
    def key_layout():   
        m=50
        n=50
        
        for i in range(1,10):
            cv2.rectangle(shape,(m,n),(m+50,100),(0,255,0),2)
            cv2.putText(shape,str(i),(m+7,90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=m+50
        cv2.rectangle(shape,(500,50),(500+50,100),(0,255,0),2)
        cv2.putText(shape,'0',(m+7,90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        first_line="q w e r t y u i o p" #list of first line
        first_line=first_line.split(" ")
        m=50
        for i in first_line:
            n=150
            cv2.rectangle(shape,(m,n),(m+50,100),(0,255,0),2)
            cv2.putText(shape,str(i),(m+7,90+40),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            m=m+50
        second_line='a s d f g h j k l '
        second_line=second_line.split(" ")
        m=50
        for i in second_line:
            n=200
            cv2.rectangle(shape,(m,n),(m+50,150),(0,255,0),2)
            cv2.putText(shape,str(i),(m+7,90+90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            m=m+50
        
        
        third_line='z x c v b n m   '
        third_line=third_line.split(" ")
        m=50
        for i in third_line:
            n=250
            cv2.rectangle(shape,(m,n),(m+50,200),(0,255,0),2)
            cv2.putText(shape,str(i),(m+7,90+140),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            m=m+50
        
        
        
        m=100
        n=300
        cv2.rectangle(shape,(m-50,n),(m+350,250),(0,255,0),2)
        
        cv2.rectangle(shape,(m+350,250),(m+450,300),(0,255,0),2)
        cv2.putText(shape,"<--",(m+357,285),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
    key_layout()
    cv2.imshow('image',shape)
    if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
        break
############################################

############################################
## Close and exit
capt.release()
cv2.destroyAllWindows()
############################################
