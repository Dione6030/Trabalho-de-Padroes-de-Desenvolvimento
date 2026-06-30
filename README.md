# Composite

O objetivo do composite é permitir tratar objetos individuais e grupos de objetos de uma maneira uniforme, com o intuito de resolver um problema clássico que seria representar estruturas hierárquicas que podem conter elementos dentro de outros elementos. Com isso, ele permite que as partes e conjunto de partes sejam manipulados através da mesma interface, elminando verificações de tipo e tornando o sistema extensível.

Nos exemplos (usei como base o visual do refactoring guru) em Python, temos o nosso sistema de encomendas, basicamente simulando um sistema de logística. Nossa encomenda simples é indivisível, pois tem peso, descrição e valor, já o nosso pacote (onde entra o Composite) pode conter várias encomendas simples mas também pode conter outros pacotes (contendo outras encomendas simples por exemplo), com o Composite, ele permite que ambos sejam tratados como "encomendas", sem distinção.

## :no_entry_sign: Sistema sem Composite

- Cada classe tem sua própria interface

- Não há como saber se o código está lidando com uma encomenda simples ou um pacote

- Lógica de cálculo fica espalhada e duplicada

- Fica difícil expandir a estrutura hierárquica


## :white_check_mark: Sistema com Composite

- Define operações que todos elementos devem implementar

- Implementa a interface sem conter outros elementos contendo uma coleção de (Component)

- Reduz a complexidade a aumenta a extensibilidade do programa

- Facilita testes e manutenção do código

## Pontos Fortes e Fracos (Comparativo)

- Pode se tornar difícil implementar a interface se não houver muita semelhança
  
- Para sistemas simples mais pode se tornar difícil a compreensão


| Forte        | Fraco           |
| ------------- |:-------------:|
| Permite introduzir novos elementos sem que o código inteiro quebre     | Permite que objectos sejam adicionados em lugares errados sem validação |
| Esturtura em "árvore" (polimorfismo) ótima para sistemas hierárquicos     | Desvantajoso para sistemas simples devido a abstração      |
| Facilita a implementação a partir de classes | Difícil implementar interface comum de classes dependendo do sistema      |

## Conclusão

O sistema em Composite é uma ótima escolha quando o programador precisa fazer um sistema que possui várias classes que dependem uma da outra, criando um código que o permite implementar várias funções a partir de uma sem ter que se preocupar se a implementação irá quebrar parte do código já existente.
