import cv2
import mediapipe as mp
import numpy as np
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

yawn_count = 0
is_yawning = False
yawn_timestamps = []

def get_distance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def count_fingers(hand_landmarks):
    fingers = []
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x: fingers.append(1)
    else: fingers.append(0)
    for tip in [8, 12, 16, 20]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y: fingers.append(1)
        else: fingers.append(0)
    return fingers

while cap.isOpened():
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1) 
    ih, iw, _ = img.shape
    current_time = time.time()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    face_results = face_mesh.process(img_rgb)
    hand_results = hands.process(img_rgb)

    if hand_results.multi_hand_landmarks:
        for hand_lms in hand_results.multi_hand_landmarks:
            f = count_fingers(hand_lms)
            if f == [1, 1, 1, 1, 1]: 
                yawn_count = 0
                yawn_timestamps = []
            elif f == [0, 1, 1, 0, 0]:
                cap.release()
                cv2.destroyAllWindows()
                exit()

   
    if face_results.multi_face_landmarks:
        for face_lms in face_results.multi_face_landmarks:
            lms = face_lms.landmark
            
            ear = get_distance(lms[159], lms[145]) / get_distance(lms[33], lms[133]) 
            mar = get_distance(lms[13], lms[14]) / get_distance(lms[78], lms[308])   
            head_pitch = lms[152].y - lms[1].y 

            if mar > 0.5:
                if not is_yawning:
                    yawn_count += 1
                    yawn_timestamps.append(current_time)
                    is_yawning = True
            else: is_yawning = False

            yawn_timestamps = [t for t in yawn_timestamps if current_time - t <= 60]

            if ear < 0.20: 
                cv2.putText(img, "!!! SLEEP ALERT !!!", (iw//2-150, ih//2), 2, 1.2, (0,0,255), 3)
                cv2.rectangle(img, (0,0), (iw,ih), (0,0,255), 10)
            
            if head_pitch < 0.12: 
                cv2.putText(img, "HEAD DOWN!", (iw//2-100, ih//2+50), 2, 1, (0,165,255), 2)

            if len(yawn_timestamps) >= 5: 
                cv2.putText(img, "CRITICAL FATIGUE", (iw//2-150, ih-100), 2, 1, (0,165,255), 2)

    overlay = img.copy()
    cv2.rectangle(overlay, (20, 20), (350, 180), (80, 0, 80), -1)
    img = cv2.addWeighted(overlay, 0.7, img, 0.3, 0)

    cv2.putText(img, "DRIVER ADAS SYSTEM", (40, 50), 2, 0.6, (255,255,255), 1)
    cv2.line(img, (40, 60), (330, 60), (255,255,255), 1)
    cv2.putText(img, f"Total Yawns: {yawn_count}", (50, 95), 2, 0.7, (255,255,255), 1)
    cv2.putText(img, f"Yawns/Min: {len(yawn_timestamps)}", (50, 135), 2, 0.7, (0,255,0), 2)
    cv2.putText(img, "🤚🏻: Reset  ✌🏻: Exit", (50, 165), 2, 0.5, (200,200,200), 1)

    cv2.imshow("ADAS Full Suite", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()