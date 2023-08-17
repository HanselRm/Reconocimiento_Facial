# Reconocimiento_Facial

Prerrequisitos

    Python 3.11.4
    pip 23.1.2

Ejecutar el proyecto

    Entrar en el cmd, luego al direcctorio Reconocimiento_Facial-master\envs\tincode\Scripts desde el cmd
    y escribimos activate.bat para ejecutar el entorno virtual, luego retrodecemos a la carpeta raiz del 
    proyecto y escribimos pip install opencv-python y ejecutamos el proyecto con app.py. (todo en el cmd)

Explicación

    El proyecto es una aplicacion de reconocimiento facial el cual reconoce a las personas por medio de 
    las caracteristicas de las caras de las personas. 
    
    El proyecto toma un xml que es el modelo ya entrenado que  define un clasificador de cascada Haar, que 
    es una estructura jerárquica de múltiples etapas, cada una compuesta por varios árboles de decisión que 
    se entrenan mediante AdaBoost. Cada etapa de la cascada se enfoca en una tarea específica, como la 
    detección de una característica particular en una imagen. Dentro de cada etapa, los árboles de decisión 
    utilizan características de tipo Haar para evaluar si se encuentra o no la característica deseada en la 
    imagen. Estas características de Haar son patrones rectangulares que se aplican a diferentes regiones de 
    la imagen para medir ciertas propiedades visuales. AdaBoost se utiliza para ajustar los pesos de las 
    muestras de entrenamiento y combinar múltiples árboles de decisión en cada etapa, de manera que se 
    enfoquen en las regiones de la imagen donde se espera que se encuentre la característica buscada.

Explicacion del codigo

    El programa Define el nombre del archivo XML que contiene el clasificador de cascada Haar 
    preentrenado para la detección de caras. Carga el clasificador de cascada Haar utilizando 
    cv2.CascadeClassifier(file), inicializa la cámara web, inicia un bucle infinito (while True) 
    para capturar y procesar continuamente los cuadros de video desde la cámara, convierte la 
    imagen a escala de grises ya que el clasificador Haar generalmente funciona mejor en imágenes en 
    grises luego itera a través de las caras detectadas y dibuja rectángulos verdes alrededor de ellas y 
    se va ejecutando hasta que se precione la tecla Esc.
