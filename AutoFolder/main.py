import os

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
NEGRITO = "\033[1m"
BLUE = "\033[94m"
YELLOW = "\033[93m"


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def sair():
    print("Saindo.....")
    exit()


def mostrar_figlet():
    print(f'''{RED}{NEGRITO}                 
    _         _        _____     _     _                 _            
   / \  _   _| |_ ___ |  ___|__ | | __| | ___ _ __    __| | _____   __
  / _ \| | | | __/ _ \| |_ / _ \| |/ _` |/ _ \ '__|  / _` |/ _ \ \ / /
 / ___ \ |_| | || (_) |  _| (_) | | (_| |  __/ |    | (_| |  __/\ V / 
/_/   \_\__,_|\__\___/|_|  \___/|_|\__,_|\___|_|     \__,_|\___| \_/  
                                                                      
                     {YELLOW}{NEGRITO}[Select Option To Continue]   {RESET}                                                          
    
                                               
    {RESET}''')


limpar_tela()

while True:
    mostrar_figlet()
    print(f"  {RED}{NEGRITO}[{RESET}{GREEN}{NEGRITO}1{RED}{NEGRITO}]{RESET} {GREEN}{NEGRITO}FRONT END")
    print(f"  {RED}{NEGRITO}[{RESET}{GREEN}{NEGRITO}0{RED}{NEGRITO}]{RESET} {GREEN}{NEGRITO}SAIR")

    opcao = int(input(f"  {BLUE}{NEGRITO}[Auto{RED}{NEGRITO}@{RED}{NEGRITO}{BLUE}{NEGRITO}Folder]${RESET} "))
    if opcao == 0:
         sair()


    if opcao == 1:

        limpar_tela()

        

        nome_pasta = input(f"  {YELLOW}{NEGRITO}Qual nome da pasta?:{RESET} ")

        caminho_pasta = os.path.join(nome_pasta)
        os.makedirs(caminho_pasta, exist_ok=True)

        caminho_page = os.path.join(caminho_pasta, "page")
        os.makedirs(caminho_page, exist_ok=True)

        caminho_assets = os.path.join(caminho_pasta, "assets")
        os.makedirs(caminho_assets, exist_ok=True)

        caminho_subpasta = os.path.join(caminho_pasta, "scr")
        os.makedirs(caminho_subpasta, exist_ok=True)

        caminho_img = os.path.join(caminho_assets, "img")
        os.makedirs(caminho_img, exist_ok=True)

        caminho_fonts = os.path.join(caminho_assets, "fonts")
        os.makedirs(caminho_fonts, exist_ok=True)

        caminho_icons = os.path.join(caminho_assets, "icons")
        os.makedirs(caminho_icons, exist_ok=True)

        caminho_css = os.path.join(caminho_subpasta, "css")
        os.makedirs(caminho_css, exist_ok=True)

        caminho_js = os.path.join(caminho_subpasta, "js")
        os.makedirs(caminho_js, exist_ok=True)

        arquivo = os.path.join(caminho_pasta, "index.html")
        with open(arquivo, 'w') as arquivo:
            arquivo.write('''   
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="scr/css/style.css">
  <title>Document</title>
</head>
<body>


  <script src="scr/js/application.js" type="text/javascript" charset="utf-8" async defer></script>
</body>
</html>
            ''')

        arquivo = os.path.join(caminho_css, "style.css")
        with open(arquivo, 'w') as arquivo:
            arquivo.write('''   
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
            ''')

        arquivo = os.path.join(caminho_js, "app.js")
        with open(arquivo, 'w') as arquivo:
            arquivo.write('''   
           ''')
            print(caminho_pasta, caminho_assets)
        limpar_tela()