print('''
██████╗ ████████╗     ██████╗██████╗  █████╗ ███████╗██╗  ██╗
██╔══██╗╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██████╔╝   ██║       ██║     ██████╔╝███████║███████╗███████║
██╔══██╗   ██║       ██║     ██╔══██╗██╔══██║╚════██║██╔══██║
██║  ██║   ██║       ╚██████╗██║  ██║██║  ██║███████║██║  ██║
╚═╝  ╚═╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                         MD5 SHA1 SHA224 SHA256 SHA384 SHA512                                    


[+] Diego Bernardes
[+]https://breaksec.wordpress.com/
''')
import hashlib
import argparse


argumentos = argparse.ArgumentParser()
argumentos.add_argument('--tipo', action = 'store', dest = 'tipo', required = True, help = '''
1 = MD5
2 = SHA1
3 = SHA224
4 = SHA256
5 = SHA384
6 = SHA512
''')
argumentos.add_argument('--hash', action = 'store', dest = 'hash', required = True, help = 'Hash que você deseja quebrar')
argumentos.add_argument('--wlist', action = 'store', dest = 'wordlist', required = True, help = 'Caminho da Wordlist (Ex.: C:\wordlist.txt )')
arg = argumentos.parse_args()


text = open(arg.wordlist).readlines()
busca = str(arg.hash).lower()
text = [str(x).rstrip() for x in text]
temp = ''


if arg.tipo == '1':
    for x in text:
        temp = hashlib.md5(x.encode('utf-8')).hexdigest()
        if busca == temp:
            print('[+]Valor encontrado\nHash: {hash}\nTexto Original: {text}\n{xD}' .format(
                hash = busca, text = x, xD = ('-'*30)))
            break
elif arg.tipo == '2':
    for x in text:
        temp = hashlib.sha1(x.encode('utf-8')).hexdigest()
        if busca == temp:
            print('[+]Valor encontrado\nHash: {hash}\nTexto Original: {text}\n{xD}' .format(
                hash = busca, text = x, xD = ('-'*30)))
            break
elif arg.tipo == '3':
    for x in text:
        temp = hashlib.sha224(x.encode('utf-8')).hexdigest()
        if busca == temp:
            print('[+]Valor encontrado\nHash: {hash}\nTexto Original: {text}\n{xD}' .format(
                hash = busca, text = x, xD = ('-'*30)))
            break
elif arg.tipo == '4':
    for x in text:
        temp = hashlib.sha256(x.encode('utf-8')).hexdigest()
        if busca == temp:
            print('[+]Valor encontrado\nHash: {hash}\nTexto Original: {text}\n{xD}' .format(
                hash = busca, text = x, xD = ('-'*30)))
            break
elif arg.tipo == '5':
    for x in text:
        temp = hashlib.sha384(x.encode('utf-8')).hexdigest()
        if busca == temp:
            print('[+]Valor encontrado\nHash: {hash}\nTexto Original: {text}\n{xD}' .format(
                hash = busca, text = x, xD = ('-'*30)))
            break
elif arg.tipo == '6':
    for x in text:
        temp = hashlib.sha512(x.encode('utf-8')).hexdigest()
        if busca == temp:
            print('[+]Valor encontrado\nHash: {hash}\nTexto Original: {text}\n{xD}' .format(
                hash = busca, text = x, xD = ('-'*30)))
            break
print('Finalizado')
