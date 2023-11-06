import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

def leer_mails():
    # Configura el alcance y el archivo de credenciales
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    CREDENTIALS_FILE = 'client_secret_761641041079-b991g5has3pul09ajl9eh7gled0gb04s.apps.googleusercontent.com.json'

    # Inicializa las credenciales de OAuth
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Guarda las credenciales para futuros usos
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Inicializa la API de Gmail
    service = build('gmail', 'v1', credentials=creds)

    #asunto_especifico='info'

    # Lee los correos electrónicos
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q=f'is:unread').execute()
    messages = results.get('messages', [])
    lista_mails=[]

    if not messages:
        print('No se encontraron correos electrónicos no leídos.')
    else:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            message_content = ""

            if 'parts' in msg['payload']:
                for part in msg['payload']['parts']:
                    if part['mimeType'] == 'text/plain':
                        message_body = part['body']['data']
                        message_data = base64.urlsafe_b64decode(message_body.encode('UTF-8'))
                        message_content += message_data.decode('UTF-8')
            else:
                message_body = msg['payload']['body']['data']
                message_data = base64.urlsafe_b64decode(message_body.encode('UTF-8'))
                message_content += message_data.decode('UTF-8')

            # Ahora tienes el contenido del correo electrónico en la variable message_content
            # Puedes trabajar con él como desees, por ejemplo, imprimirlo o procesarlo más.
            lista_mails.append(message_content)
    
    return lista_mails
