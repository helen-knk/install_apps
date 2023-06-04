import subprocess

# Lista de aplicativos a serem instalados
list_apps = \
    ["discord", "notion", "rectangle", "postman", "slack",
     "db-browser-for-sqlite", "dbeaver-community", "firefox",
     "visual-studio-code", "krisp", "logi-options-plus", "gather"]
# note: pycharm and demopro aren't here

# Iterar sobre a lista de aplicativos e executar o comando de instalação com o Homebrew
for app in list_apps:
    comando = f"brew install --cask {app}"
    subprocess.call(comando, shell=True)
