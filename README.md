# Composite

O objetivo do composite é permitir tratar objetos individuais e grupos de objetos de uma maneira uniforme, com o intuito de resolver um problema clássico que seria representar estruturas hierárquicas que podem conter elementos dentro de outros elementos. Com isso, ele permite que as partes e conjunto de partes sejam manipulados através da mesma interface, elminando verificações de tipo e tornando o sistema extensível.

Nos exemplos (usei como base o visual do refactoring guru) em Python, temos o nosso sistema de encomendas, basicamente simulando um sistema de logística. Nossa encomenda simples é indivisível, pois tem peso, descrição e valor, já o nosso pacote (onde entra o Composite) pode conter várias encomendas simples mas também pode conter outros pacotes (contendo outras encomendas simples por exemplo), com o Composite, ele permite que ambos sejam tratados como "encomendas", sem distinção.

## :no_entry_sign: Sistema sem Composite

- Cada classe tem sua própria interface

- O código não tem como saber está lidando com uma encomenda simples ou um pacote

- Lógica de cálculo fica espalhada e duplicada

- Fica difícil expandir a estrutura hierárquica


## :white_check_mark: Sistema com Composite
