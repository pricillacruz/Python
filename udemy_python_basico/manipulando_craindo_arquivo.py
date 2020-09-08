#cuidando da acentuação correte:
# -*- coding: utf-8 -*-

#criando um novo arquivo
w = open("meu_arquivo2.txt", "w")

#o "a" acrescenta conteudo novo no arquivo
w = open("meu_arquivo2.txt", "a")

#colocando conteudo dentro do arquivo
w.write("Esse é o novo conteudo colocado no arquivo! Ass: Pri \n")

#fechando o arquivo depois de aberto
w.close()

