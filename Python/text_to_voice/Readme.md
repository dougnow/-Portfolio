Text to Speech Reader with Translation

Propósito del proyecto
Este proyecto es un lector automatizado de texto que combina varias tecnologías para extraer texto de imágenes y documentos PDF, convertirlo a voz y, si es necesario, traducir el texto automáticamente de inglés a español. El propósito es demostrar cómo se pueden integrar herramientas de procesamiento de lenguaje natural (NLP), reconocimiento óptico de caracteres (OCR), y generación de voz para resolver problemas cotidianos, como la lectura de documentos escaneados o PDFs.

Tecnologías utilizadas
Este proyecto hace uso de las siguientes tecnologías y bibliotecas:

Python: El lenguaje principal utilizado.
pytesseract: Para la extracción de texto de imágenes mediante OCR.
PyPDF2: Para la extracción de texto de PDFs.
gTTS: Para convertir el texto a voz en múltiples idiomas.
langdetect: Para detectar el idioma del texto de entrada.
googletrans: Para la traducción automática de inglés a español.
pdf2image: Para convertir páginas de un PDF a imágenes en caso de que el PDF no tenga texto embebido.


Instrucciones para ejecutarlo
Instalar las dependencias: Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes bibliotecas de Python. Puedes hacerlo ejecutando los siguientes comandos:

pip install pytesseract
pip install PyPDF2
pip install gTTS
pip install langdetect
pip install googletrans==4.0.0-rc1
pip install pdf2image


Instalar Tesseract OCR: Si no tienes Tesseract instalado en tu máquina, puedes descargarlo desde este enlace. 
Asegúrate de configurar la variable de entorno para que pytesseract pueda acceder al ejecutable.

Cómo ejecutar: Puedes clonar este repositorio en tu máquina local y ejecutar el archivo principal main.py. 
El programa te pedirá que elijas entre cargar un archivo o usar la cámara, y luego te guiará en función de si es una imagen o un PDF.

Entrada de archivos:

Para imágenes: Se puede cargar cualquier imagen que contenga texto, como fotos de libros o documentos escaneados.
Para PDFs: Puedes cargar cualquier archivo PDF con texto embebido o escaneado. El programa se encargará de extraer el texto o convertir las páginas a imágenes si es necesario.


-creado en gogle colab - revisor y ejecucion de codigo con revisor chatgpt 
