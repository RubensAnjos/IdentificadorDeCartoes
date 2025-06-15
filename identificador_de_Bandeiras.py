import re

def identificar_bandeira(card_number):
    card_number = str(card_number).replace(" ", "")

    patterns = {
        'Visa':        r'^4\d{12}(\d{3})?(\d{3})?$',
        'Mastercard':  r'^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$',
        'American Express': r'^3[47]\d{13}$',
        'Discover':    r'^(6011\d{12}|65\d{14}|64[4-9]\d{13})$',
        'Diners Club': r'^(3(0[0-5]|[68]\d)\d{11})$',
        'JCB':         r'^(35\d{14,17})$',
        'Elo':         r'^(4011(78|79)\d{10}|431274\d{10}|438935\d{10}|451416\d{10}|457393\d{10}|504175\d{10}|5067(0[0-9]|1[0-9]|20)\d{10}|509\d{13}|627780\d{10}|636297\d{10}|636368\d{10}|650\d{13}|6516\d{12}|6550\d{12})$',
        'Hipercard':   r'^(606282\d{10}(\d{3})?|3841\d{15})$',
        'EnRoute': r'^(2014|2149)[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{3}$',
        'Voyager': r'^8699[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{3}$',
        'Aura': r'^(50)\d{14}$'
    
    }

    for bandeira, pattern in patterns.items():
        if re.fullmatch(pattern, card_number):
            return bandeira
    return 'Bandeira desconhecida'