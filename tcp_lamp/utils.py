import codecs


def int_from_bytes(bytes_in):
    return int(codecs.encode(bytes_in, 'hex'), 16)

