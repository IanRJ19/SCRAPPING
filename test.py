from selenium import webdriver

# Inicializa el WebDriver sin especificar la ruta completa
driver = webdriver.Chrome()

# Abre una página web de prueba (por ejemplo, Google)
driver.get('https://www.google.com')

# Toma una captura de pantalla de la página
driver.save_screenshot('screenshot.png')

# Cierra el navegador
driver.quit()

print("El script se ejecutó correctamente y tomó una captura de pantalla.")
