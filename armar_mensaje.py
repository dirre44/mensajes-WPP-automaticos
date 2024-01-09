from leer_mails import leer_mails

def limpiar_mail(lista_mail):
    mails_limpios=[]
    for mail in lista_mail:
        mail_limpio=mail.strip()
        mail_limpio=mail_limpio.replace('VERIFICAR HABER PEDIDO ANTES PARA NO SUPERPONER EN FOB', '')
        mail_final=f"comprar en FOB:\n{mail_limpio}(STOCK)"
        mails_limpios.append(mail_final)    
    return mails_limpios

def armar_lista():
    lista_mails = leer_mails()
    lista_mensajes=limpiar_mail(lista_mails)
    return lista_mensajes