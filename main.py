import requests

import backup

def proc_data(d):
    if d is not None:
        resultado = None
        datos = d.split('|')
        operador = datos[0]
        comando1 = datos[1]
        comando2 = datos[2]
        comando3 = datos[3]
        resultado = operador, comando1, comando2, comando3
        return resultado

if __name__ == "__main__":
    var1 = requests.get('https://github.com/a21rubenpv/pps/raw/main/flow.txt')
    datos = proc_data(var1.text)
    isBackup = datos[1].split(':')[1]
    isSent = datos[2].split(':')[1]
    isAuth = datos[3].split(':')[1]
    print("backup: ", isBackup)
    print("sent: ", isSent)
    print("Autorizado", isAuth)

    if int(isBackup) == 1 & int(isAuth) == 1:
        # Carpeta da que queres facer backup
        backup.backuptoZip('aaa')
    else:
        print('Non se vai facer backup')
