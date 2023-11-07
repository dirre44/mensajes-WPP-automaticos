import pywhatkit
from leer_mails import leer_mails

# id del grupo ECWo66rKJkN8pEAvoqxQwN

#pywhatkit.sendwhatmsg_instantly("+5491154193721", "chino gil", 7, False)


lista_mails = leer_mails()

codigo_wpp_prueba="ECWo66rKJkN8pEAvoqxQwN"
codigo_wpp_FOB="HScd4MqiFSJC1ujQymJFoW"

#for mail in lista_mails:
#    mail.replace(r'\r\n  VERIFICAR HABER PEDIDO ANTES PARA NO SUPERPONER EN FOB\r\n', '')
    #mail_limpio=mail.strip()
    #mail_limpio=mail_limpio.replace('VERIFICAR HABER PEDIDO ANTES PARA NO SUPERPONER EN FOB', '')
    #mail_final=f"comprar en FOB:\n{mail_limpio} (STOCK)"
    #print(f"comprar en FOB:\n{mail_limpio}(STOCK)")

for mail in lista_mails:

    mail_limpio=mail.strip()
    mail_limpio=mail_limpio.replace('VERIFICAR HABER PEDIDO ANTES PARA NO SUPERPONER EN FOB', '')
    #mail_final=f"comprar en FOB:\n{mail_limpio} (STOCK)"
    mail_final=f"comprar en FOB:\n{mail_limpio}(STOCK)"
    print(mail_final)

    seleccion = input("Desea enviar este mensaje de falta de stock?? Y/N: " )
    if seleccion.upper() == "Y":
        pywhatkit.sendwhatmsg_to_group_instantly(codigo_wpp_FOB,mail_final,8,True,3)
    elif seleccion.upper() == "N":
        continue
    else:
        # en realidad no se que deberia hacer en esta situacion, un continue??
        break