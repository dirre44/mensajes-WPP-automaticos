import pywhatkit
from leer_mails import leer_mails

# id del grupo ECWo66rKJkN8pEAvoqxQwN

#pywhatkit.sendwhatmsg_instantly("+5491154193721", "chino gil", 7, False)


lista_mails = leer_mails()

#for mail in lista_mails:
#    mail.replace(r'\r\n  VERIFICAR HABER PEDIDO ANTES PARA NO SUPERPONER EN FOB\r\n', '')
#    print(mail)

for mail in lista_mails:

    pywhatkit.sendwhatmsg_to_group_instantly("ECWo66rKJkN8pEAvoqxQwN",mail,15,True,3)