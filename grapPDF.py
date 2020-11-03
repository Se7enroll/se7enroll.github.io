from selenium import webdriver

def grapPdf(pdf_url):
	download_dir = "C:\\Users\\tobias\\downloads\\GradProb" # for linux/*nix, download_dir="/usr/Public"
	options = webdriver.ChromeOptions()

	profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
	options.add_experimental_option("prefs", profile)
	driver = webdriver.Chrome(r"C:\Users\Tobias\Documents\chromedriver.exe", chrome_options=options)  # Optional argument, if not specified will search path.

	driver.get(pdf_url)


def findPdf(url):
	#Setup
	download_dir = "C:\\Users\\tobias\\downloads\\gradProb" # for linux/*nix, download_dir="/usr/Public"
	options = webdriver.ChromeOptions()
	profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
	options.add_experimental_option("prefs", profile)
	driver = webdriver.Chrome(r"C:\Users\Tobias\Documents\chromedriver.exe", chrome_options=options)  # Optional argument, if not specified will search path.

	#Find links
	driver.get(url)
	links = []
	elements = driver.find_elements_by_xpath(r"//a[contains(@href,'.pdf')]")
	for element in elements:
		links.append(element.get_attribute('href'))

	print(links)

	for i in links:
		driver.get(i)

	print("succes?")
	

findPdf(r"http://math.wisc.edu/~roch/grad-prob/index.html")