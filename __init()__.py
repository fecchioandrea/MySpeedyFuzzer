"""
Invia 'num' richieste HTTP di tipo GET/POST su altrettanti threads,
avendo sempre a disposizione un massimo numero di thread pari a '-t'.

Il tipo della richiesta è determinato dalla presenza o meno dell'argomento
--data, tra quelli passati da linea di comando. Se presente è un POST,
se assente allora viene riempito il payload indicato direttamente nell'url.

La prova (per il POST) utilizza una Web App su Virtual Machine, indirizzo:
http://192.168.56.101/index.php/, in cui ad un payload viene sostituito
di volta in volta un diverso codice di intrusione, tra quelli nel file
'Auth_Bypass.txt', nella repository: https://github.com/swisskyrepo/PayloadsAllTheThings.

Nel caso particolare, usiamo 'Administrator' come 'uname',
mentre 'psw' corrisponde al campo il cui valore va ricercato.

"""


__title__ = 'fuzzer'
__version__ = '0.1.0'
__author__ = 'Andrea Fecchio'

__all__ = ()
