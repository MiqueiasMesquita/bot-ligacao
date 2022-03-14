from twilio.rest import Client

account_sid = "AC044c3223194d7dbca165155209833755"
auth_token = "0ad10899872a1343cd75264c12097bd9"
meu_numero = "xxxxxxxxx"
numero_twilio = "xxxxxxx"
mensagem = """
<Response>
<Say language="pt-BR">
Sua mensagenm aqui.
</Say>
</Response>
"""

cliente = Client(account_sid, auth_token)

ligacao = cliente.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)
