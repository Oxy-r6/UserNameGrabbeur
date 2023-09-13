import os
import socket
import requests

# URL du webhook Discord
WEBHOOK_URL = "Link of your webhook"

# Récupérer le nom de l'hôte de l'ordinateur
hostname = socket.gethostname()

# Créer un message à envoyer au webhook Discord
message = f"L'hôte de l'ordinateur est : {hostname}"

# Créer un payload JSON pour le message
payload = {
    "content": message
}

# Envoyer le message au webhook Discord
response = requests.post(WEBHOOK_URL, json=payload)

# Vérifier si la requête a réussi
if response.status_code == 204:
    print(f"Message envoyé avec succès à {WEBHOOK_URL}")
else:
    print(f"Échec de l'envoi du message. Code de statut : {response.status_code}")