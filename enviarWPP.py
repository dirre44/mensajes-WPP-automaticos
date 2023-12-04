import pywhatkit
from leer_mails import leer_mails

def limpiar_mail(lista_mail):
    mails_limpios=[]
    for mail in lista_mail:
        mail_limpio=mail.strip()
        mail_limpio=mail_limpio.replace('VERIFICAR HABER PEDIDO ANTES PARA NO SUPERPONER EN FOB', '')
        mail_final=f"comprar en FOB:\n{mail_limpio}(STOCK)"
        mails_limpios.append(mail_final)    
    return mails_limpios

codigo_wpp_prueba="ECWo66rKJkN8pEAvoqxQwN"
codigo_wpp_FOB="HScd4MqiFSJC1ujQymJFoW"

lista_mails = leer_mails()
lista_mensajes=limpiar_mail(lista_mails)

division_mensajes={"enviar":[],"no_enviar":[]}

for mail in lista_mensajes:

    print(mail)
    seleccion = input("Desea enviar este mensaje de falta de stock?? Y/N: " )
    if seleccion.upper() == "Y":
        division_mensajes["enviar"].append(mail)
    elif seleccion.upper() == "N":
        division_mensajes["no_enviar"].append(mail)
    else:
        # en realidad no se que deberia hacer en esta situacion, un continue??54545454
        break

for mail in division_mensajes["enviar"]:

    pywhatkit.sendwhatmsg_to_group_instantly(codigo_wpp_FOB,mail,8,True,3)
