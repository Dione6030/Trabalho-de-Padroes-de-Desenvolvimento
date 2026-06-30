# Padrão de Desenvolvimento Flyweight

    Imagine a seguinte situação:

    Você tem um projeto de jogo de sobrevivência em uma floresta no estilo "GreenHell", aí você está cuidando da ambientação e tem que colocar as árvores no jogo, você faz um sistema que irá criar a floresta conforme o jogador vai andando, gerando árvores proceduralmente.

    Você entra no jogo e ele está funcionando e gerando do jeito que você queria, aí você coloca na mão do seu colega para ele testar, mas ele mal sai andando e o jogo dele começa a travar e fechar.

    Quando você percebe que é porque o note/pc dele não possui tanta VRAM e acaba não suportando a quantidade de objetos gerados na tela.

    Para contornar essa situação, você decide que, ao invés de criar um objeto completo do zero e deixar no mapa, você decide guardar partes repetidas como textura, modelo, cor e espécie para usar em todas as árvores com o mesmo padrão e só chamar o mesmo objeto sem precisar criar outro.

    Nesse caso, dividimos a árvore em duas partes, a parte imutável onde você vai armazenar a parte que será usada em diversos contextos (Flyweight), ficando com os dados "intrínsecos" do objeto;

    E a parte que oscila e que sempre vai ser única para cada objeto (Contexto), que guarda o dado extrínseco.

    Assim o cliente calcula ou armazena os dados extrínsecos dos Flyweight, com o Flyweight servindo de molde para os objetos.

    Isso permite que o gasto seja consideravelmente reduzido da memória RAM da máquina.

# Atenção
    O flyweight deve ser usado somente em casos em que o programa deve rodar diversos objetos repetidos que talvez a VRAM não suporte, sendo recomendado em editores de texto, motores de renderização e interfaces gráficas (GUI) e, ironicamente, recursos nativos de linguagens de programação; podemos ver isso no String Interning do Java e C#.

# Prós e Contras
    A única coisa boa dele é que ele poupa memória RAM, mas ele aumenta o código, fazendo com que quem chegue depois para fazer manutenção possa ficar em dúvida do porquê um objeto foi dividido do jeito como mostrado, e o gasto de memória RAM não some, vira gasto da CPU que transforma o Flyweight em cache e tem que calcular os dados de contexto repetidamente cada vez que o flyweight é chamado.

# Menção Honrosa
    Pode ser usado com os padrões Composite, Facade, Singleton e, como no código apresentado, Factory Method, que, quando você tem em mente que talvez o cliente queira um novo padrão de objeto (tipo árvore com cor diferente), você manda para um objeto factory antes de chamar flyweight.