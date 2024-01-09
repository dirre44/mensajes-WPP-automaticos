import pywhatkit
from armar_mensaje import armar_lista

codigo_wpp_prueba="ECWo66rKJkN8pEAvoqxQwN"
codigo_wpp_FOB="HScd4MqiFSJC1ujQymJFoW"

lista_mensajes = armar_lista()


for mail in lista_mensajes:
    pywhatkit.sendwhatmsg_to_group_instantly(codigo_wpp_FOB,mail,8,True,3)