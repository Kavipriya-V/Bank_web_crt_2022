# -------------------------------------- profile_detection ---------------------------------------
detect_frontal_face = r'C:\Users\admin\OneDrive\Desktop\Bank_Web_CRT_2021\face_liveness_detection_Anti_spoofing_master\profile_detection\haarcascades/haarcascade_frontalface_alt.xml'
detect_perfil_face = r'C:\Users\admin\OneDrive\Desktop\Bank_Web_CRT_2021\face_liveness_detection_Anti_spoofing_master\profile_detection\haarcascades/haarcascade_profileface.xml'

# -------------------------------------- emotion_detection ---------------------------------------
# modelo de deteccion de emociones
path_model = r'C:\Users\admin\OneDrive\Desktop\Bank_Web_CRT_2021\face_liveness_detection_Anti_spoofing_master\emotion_detection\Modelos/model_dropout.hdf5'
# Parametros del modelo, la imagen se debe convertir a una de tamaño 48x48 en escala de grises
w,h = 48,48
rgb = False
labels = ['angry','disgust','fear','happy','neutral','sad','surprise']


# definir la relacion de aspecto del ojo EAT
# definir el numero de frames consecutivos que debe estar por debajo del umbral
EYE_AR_THRESH = 0.23 #baseline
EYE_AR_CONSEC_FRAMES = 1

# eye landmarks
eye_landmarks = r"C:\Users\admin\OneDrive\Desktop\Bank_Web_CRT_2021\face_liveness_detection_Anti_spoofing_master\blink_detection\model_landmarks/shape_predictor_68_face_landmarks.dat"