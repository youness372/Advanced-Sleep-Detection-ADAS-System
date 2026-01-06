##  $${\color{blue}Advanced \space Sleep \space Detection \space ADAS \space \space System } $$
A real-time Advanced Driver Assistance System (ADAS) that monitors driver fatigue and drowsiness using computer vision and machine learning. The system tracks facial landmarks, eye closure, yawning frequency, and head position to alert drivers when they show signs of fatigue.   

  
 ### $${\color{blue}Features \space :} $$   

* $${\color{lightgreen}Real-time \space Eye \space Monitoring \space :} $$  Detects eye closure using Eye Aspect Ratio (EAR)
* $${\color{lightgreen}Yawn \space Detection \space :} $$   Tracks yawning frequency using Mouth Aspect Ratio (MAR)
* $${\color{lightgreen}Head \space Position \space  Tracking \space :} $$  Monitors head tilt and downward movement
* $${\color{lightgreen}Fatigue \space Alerts  \space :} $$  Visual warnings when critical fatigue patterns are detected
* $${\color{lightgreen}Hand \space Gesture \space Controls \space :} $$  

  * 🖐🏻 Open hand (5 fingers) - Reset counters
  * ✌🏻 Peace sign (2 fingers) - Exit application

* $${\color{lightgreen}Live \space Dashboard\space :} $$   Real-time statistics display with transparent overlay
 ### $${\color{blue}Project  \space Structure :} $$  
  <img width="1354" height="458" alt="image" src="https://github.com/user-attachments/assets/4ae2c0b4-161b-414c-9909-c19a953b7af5" />

 ### $${\color{blue}Alert  \space System :} $$        

| Alert Type | Trigger Condition (Threshold) | Visual Indicator (UI) |
| :--- | :--- | :--- |
| **Sleep Alert** | Eye closure (EAR < 0.20) | Red border + "SLEEP ALERT" text | 
| **Head Down** | Head pitch low (< 0.12) | Orange "HEAD DOWN" warning |
| **Critical Fatigue** | 5+ yawns per minute | Orange "CRITICAL FATIGUE" warning |   

### *Requirements*      
```diff
- Python 3.7+ : (The Best version for Use OpenCV and MediaPipe is Python 3.11)
- Opencv : (Version 4.12.0.88)
- MediaPipe : (0.10.14)
```

## $${\color{blue}Installation } $$ 
###  $${\color{lightgreen}Clone  \space this \space repository  \space :} $$ 
```bash
git clone https://github.com/youness372/Advanced-Sleep-Detection-ADAS-System.git
cd Advanced-Sleep-Detection-ADAS-System
```
### $${\color{lightgreen}Install \space the \space required \space  dependencies \space  :} $$  
```bash
pip install opencv-python mediapipe
```
### $${\color{lightgreen}Usage\space :} $$ 
  * Run the application:   
```bsh
python Advanced-Sleep-Detection-ADAS-System.py
```
#### $${\color{lightgreen}Controls \space :} $$   
```diff
- Press "q" to quit the application
```

### $${\color{blue}Code \space Structure } $$ 

```mermaid
graph TB
    A([Start ADAS System]) --> B[Initialize MediaPipe<br/>Face Mesh & Hands]
    B --> C[Set Parameters<br/>Max Faces: 1<br/>Max Hands: 1<br/>Confidence: 0.7]
    C --> D[Start Video Capture]
    D --> E[Capture & Flip Frame]
    E --> F[Convert BGR to RGB]
    F --> G[Process Face Mesh]
    F --> H[Process Hand Detection]
    
    G --> I{Face<br/>Detected?}
    H --> J{Hand<br/>Detected?}
    
    I -- Yes --> K[Extract Facial<br/>Landmarks]
    I -- No --> M[Skip Face Processing]
    
    K --> L[Calculate Metrics:<br/>EAR, MAR, Head Pitch]
    L --> N{MAR > 0.5?}
    N -- Yes --> O[Increment Yawn Count<br/>Record Timestamp]
    N -- No --> P[Reset Yawn Flag]
    O --> Q[Clean Old Timestamps<br/>Keep Last 60s]
    P --> Q
    
    Q --> R{EAR < 0.20?}
    R -- Yes --> S[SLEEP ALERT<br/>Red Border]
    R -- No --> T{Head Pitch<br/>< 0.12?}
    
    T -- Yes --> U[HEAD DOWN<br/>Warning]
    T -- No --> V{Yawns/Min<br/>>= 5?}
    
    V -- Yes --> W[CRITICAL FATIGUE<br/>Warning]
    V -- No --> X[Continue Monitoring]
    
    S --> X
    U --> X
    W --> X
    M --> X
    
    J -- Yes --> Y[Count Raised Fingers]
    J -- No --> Z[Skip Hand Control]
    
    Y --> AA{5 Fingers<br/>Raised?}
    AA -- Yes --> AB[Reset Counter<br/>Clear Timestamps]
    AA -- No --> AC{2 Fingers<br/>Peace Sign?}
    
    AC -- Yes --> AD([Exit Application])
    AC -- No --> Z
    
    AB --> Z
    Z --> X
    
    X --> AE[Render Dashboard<br/>Display Stats]
    AE --> AF[Show Frame]
    AF --> AG{Press 'Q'<br/>or Exit?}
    
    AG -- No --> E
    AG -- Yes --> AD
    
    style A fill:#4CAF50,stroke:#2E7D32,stroke-width:3px,color:#fff
    style B fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff
    style C fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff
    style D fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff
    style E fill:#00BCD4,stroke:#00838F,stroke-width:2px,color:#fff
    style F fill:#00BCD4,stroke:#00838F,stroke-width:2px,color:#fff
    style G fill:#FF9800,stroke:#E65100,stroke-width:2px,color:#fff
    style H fill:#FF9800,stroke:#E65100,stroke-width:2px,color:#fff
    style I fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style J fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style L fill:#FFD54F,stroke:#F57F17,stroke-width:2px,color:#000
    style N fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style R fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style T fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style V fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style S fill:#F44336,stroke:#C62828,stroke-width:3px,color:#fff
    style U fill:#FF5722,stroke:#D84315,stroke-width:2px,color:#fff
    style W fill:#FF5722,stroke:#D84315,stroke-width:2px,color:#fff
    style AA fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style AC fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    style AB fill:#8BC34A,stroke:#558B2F,stroke-width:2px,color:#fff
    style AD fill:#F44336,stroke:#C62828,stroke-width:3px,color:#fff
    style AE fill:#00BCD4,stroke:#00838F,stroke-width:2px,color:#fff
    style AG fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
```


