#!/bin/bash

# Adiciona as configurações de histórico ao arquivo .bashrc
echo 'HISTTIMEFORMAT="%d/%m/%y %T "' >> ~/.bashrc
echo 'HISTFILESIZE=100000' >> ~/.bashrc
echo 'HISTTIMEFORMAT="%d/%m/%y %T "' >> ~/.bashrc
echo 'HISTFILESIZE=100000' >> ~/.bashrc
echo 'HISTSIZE=100000' >> ~/.bashrc

# Adiciona a personalização do prompt ao arquivo .bashrc
echo 'PS1="\[\033[32m\]pentesters-thiago.alvarenga-\$(date +%d-%m-%Y-%T) # \[\033[0m\]"' >> ~/.bashrc

# Recarrega o arquivo .bashrc para que as alterações entrem em vigor
source ~/.bashrc
