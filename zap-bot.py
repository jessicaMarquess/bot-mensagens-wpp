from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Me manda umas músicas legais ai, parça!"
        self.grupos = ["Pessoa ou grupo"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            # é preciso ter o chromedriver para rodar 
            executable_path=r'./chromedriver.exe', chrome_options=options 
        )

    def EnviarMensagens(self):
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(30)
        for grupo in self.grupos:
            # bot procura quem irá mandar a mensagem 
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            # entrando no chat
            chatBox = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chatBox.click()
            # para o bot reproduzir a mensagem
            chatBox.send_keys(self.mensagem)
            # enviando a mensagem
            bottomSend = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            bottomSend.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()