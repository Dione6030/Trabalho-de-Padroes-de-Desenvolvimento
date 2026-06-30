# Padrão de Desenvolvimento Flyweight
<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/8eb03f2a-42e8-4114-8bb2-fedde2d198f3" />

# Imagine a seguinte situação:

Você tem um projeto de jogo de sobrevivência em uma floresta no estilo "GreenHell", aí você está cuidando da ambientação e tem que colocar as árvores no jogo, você faz um sistema que irá criar a floresta conforme o jogador vai andando, gerando árvores proceduralmente.
<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/33ca189b-3ce1-4639-953d-65221a947b62" />

Você entra no jogo e ele está funcionando e gerando do jeito que você queria, aí você coloca na mão do seu colega para ele testar, mas ele mal sai andando e o jogo dele começa a travar e fechar.

Quando você percebe que é porque o note/pc dele não possui tanta VRAM e acaba não suportando a quantidade de objetos gerados na tela.
Sem Flyweight:
<img width="300" height="250" alt="image" src="https://github.com/user-attachments/assets/77e964a5-7495-4c68-86b8-464353c0892d" />
<img width="300" height="250" alt="image" src="https://github.com/user-attachments/assets/a0f1ba54-ca12-4651-b694-246cfb2985a3" />

Para contornar essa situação, você decide que, ao invés de criar vários objetos completos do zero e deixar no mapa, você decide guardar partes repetidas como textura, modelo, cor e espécie para usar em todas as árvores com o mesmo padrão e só chamar o mesmo objeto sem precisar criar outro.

Nesse caso, dividimos a árvore em duas partes, a parte imutável onde você vai armazenar a parte que será usada em diversos contextos (Flyweight), ficando com os dados "intrínsecos" do objeto;
<img width="786" height="215" alt="image" src="https://github.com/user-attachments/assets/91f20904-0459-4006-8209-55d127e00faf" />

E a parte que oscila e que sempre vai ser única para cada objeto (Contexto), que guarda o dado extrínseco.
<img width="642" height="338" alt="image" src="https://github.com/user-attachments/assets/42f27ce6-8e92-4b7e-8a32-5f7cf16a7858" />

Assim o cliente calcula ou armazena os dados extrínsecos dos Flyweight, com o Flyweight servindo de molde para os objetos.
<img width="846" height="298" alt="image" src="https://github.com/user-attachments/assets/e662b6bb-ba55-4b65-97d1-a51b2943da6f" />

Isso permite que o gasto seja consideravelmente reduzido da memória RAM da máquina, já que ele só precisa consumir o flyweight uma vez.
Com Flyweight:
<img width="300" height="220" alt="image" src="https://github.com/user-attachments/assets/c78e68e8-2fac-4375-b71f-79735de783fb" />
<img width="300" height="220" alt="image" src="https://github.com/user-attachments/assets/f54928a7-2aa7-4c7a-8b0a-fdd545866012" />

# Atenção
O flyweight deve ser usado somente em casos em que o programa deve rodar diversos objetos repetidos que talvez a VRAM não suporte, sendo recomendado em editores de texto, motores de renderização e interfaces gráficas (GUI) e, ironicamente, recursos nativos de linguagens de programação; podemos ver isso no String Interning do Java e C#.

# Prós e Contras
A única coisa boa dele é que ele poupa memória RAM, mas ele aumenta o código, fazendo com que quem chegue depois para fazer manutenção possa ficar em dúvida do porquê um objeto foi dividido do jeito como mostrado, e o gasto de memória RAM não some, vira gasto da CPU que transforma o Flyweight em cache e tem que calcular os dados de contexto repetidamente cada vez que o flyweight é chamado.

# Menção Honrosa
Pode ser usado com os padrões Composite, Facade, Singleton e, como no código apresentado, Factory Method, que, quando você tem em mente que talvez o cliente precise um novo padrão de objeto (tipo árvore com cor diferente), você manda para um objeto factory antes de chamar flyweight e armazenar o novo padrão.
<img width="798" height="375" alt="image" src="https://github.com/user-attachments/assets/4427afae-b73a-42d9-8c6c-446531614546" />
