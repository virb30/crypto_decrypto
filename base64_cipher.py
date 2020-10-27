from base64 import b64encode, b64decode


def enc_base64(text_in=''):
    message_bytes = text_in.encode('ascii')
    base64_bytes = b64encode(message_bytes)
    return base64_bytes.decode('ascii')


def dec_base64(text_in=''):
    base64_bytes = text_in.encode('ascii')
    message_bytes = b64decode(base64_bytes)
    return message_bytes.decode('ascii')