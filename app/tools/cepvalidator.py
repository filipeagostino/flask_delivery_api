import requests
from colorama import Fore, init
init(autoreset=True)

def cepValidator(cep):
    url = 'https://cdn.apicep.com/file/apicep/'

    cep_formated = cep[:5]+'-'+cep[5:]
    print(Fore.YELLOW + f'CEP FORMATED: {cep_formated}')

    result = requests.get(f'{url}{cep_formated}.json')
    
    if result.status_code == 200:
        print(Fore.GREEN + f'Status Code: {result.status_code}')
        print(f'Json:\n{result.json()}')
        return True
    else:
        print(Fore.RED + 'Invalid CEP!')
        return False