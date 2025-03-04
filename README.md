# Proyecto Urban Routes

## Comprobación de la funcionalidad de Urban Routes 


### 1. Nombre del proyecto: 
qa-project-Urban-Routes-es

### 2. Descripción del proyecto:
Lo que se pretende con estas pruebas automatizadas es validar todo el proceso de la solicitud de un taxi, desde la \
configuración de la ruta hasta pedir un taxi, teniendo en cuenta ciertos requisitos de pedido por parte del usuario.


### 3. Descripción de las tecnologías y técnicas utilizadas:

 - Python: Este es el lenguaje de programación usando para escribir y automatizar las pruebas.
 - Pytest: Usado para poder correr o ejecutar las pruebas automatizadas.
 - Selenium Webdriver: Permite interactuar con los elementos de la página web, como hacer clic \
en botones, llegar datos y navegar por la página.
 - Webdriver: Usado para controlar el navegador (Chrome).
 - By: Usado para encontrar los elementos de la página a través de localizadores como: ID, CLASS_NAME\
CSS_SELECTOR Y XPATH.
 - Expected Conditions (EC): Usado para esperar a que los elementos estén presentes y listos para que \
realicen una acción determinada.
 -  WebDriverWait: Usado para esperar a que los elementos estén presentes y listos antes de \
que realicen una acción determinada.
 - Chrome WebDriver: Usado para controlar una instancia del navegador Chrome a través de las clases \
service y options.
 - Assert: Usado para validar resultados.
 - Línea de comandos: Usado para cargar el código en GitHub.

### Pasos para ejecutar las pruebas:

- conectar tu GitHub.
- Clonar el repositorio en la computadora.
- Trabajar con el proyecto de forma local.
- Instalar en la libreria Pytest.
- Instalar Selenium.
- Instalar el Chrome Driver correcto.
- Verificar que hallan 2 archivos data.py, y main.py. 
- Almacenar todos los datos en el archivo data.py.
- En el archivo main.py se encontrarán los localizadores, clases, métodos y pruebas.
- Ejecutar las pruebas para ver la automatización en tiempo real.
- Los resultados aparecerán en la terminal donde te indicara si la prueba pasó o falló.

 
### Descripción de las pruebas:


1.	El método setup class :Inicializa el WebDriver.


2.	test_set_route: Configura las direcciones desde y hasta utilizándo la clase Urban Routes Page. El\
assert comprueba que los campos se hayan llenado correctamente. 

      
3. test_choose_comfort_option: Llama a la prueba anterior (test_set_route), luego se hace clic en \
el botón pedir un taxi, luego elegir la opción Comfort y finalmente se verifica con el assert que \
la opción se haya elegido correctamente. 


4.	test_fill_number: Llama a la prueba anterior (test_choose_comfort_option), luego se le da clic\
en el campo de número de teléfono, se introduce el número de teléfono, se comprueba que el número sea \
el correcto, luego se le da clic en el botón siguiente, luego se guarda el código en la variable \
código de confirmación, luego se introduce el código de confirmación en el campo, se comprueba que sea el\
código correcto y finalmente se da clic en el botón enviar. 


5.	test_payment_method: Llama a la prueba anterior(test_fill_number), luego se da clic en método de pago,\
luego clic en agregar tarjeta de crédito, luego enviar el número de la tarjeta de crédito, verificar \
que el número sea el correcto, enviar el código de verificación, comprobar que el código \
sea el correcto, luego hacer un TAB para cambiar el enfoque, luego un clic en agregar y finalmente cerrar\
la ventana. 


6.	test_message_for_driver: Llama a la prueba (test_payment_method), envia el mensaje para el conductor y se 
verifica que el mensaje sea el correcto.


7.	test_choose_blanket_and_tissue: Llama a la prueba (test_message_for_driver) y se le da clic al slider
para pedir una manta y pañuelos.


8.	test_order_ice_cream: Llama a la prueba (test_choose_blanket_and_tissue) y finalmente doble clic
en el signo + del botón.


9.  test_taxi_request: Llama a la función (test_order_ice_cream) y finalmente clic en pedir \
un taxi. 


10. Al finalizar las pruebas Chrome se cerrará automáticamente gracias al método teardown class.

