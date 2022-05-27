# simplified_real_estate_banking

Projeto desenvolvido em Python, com o objetivo de simular partidas de banco imobiliário e gerar estatísticas sobre as mesmas. Para tanto, foram consideradas as regras a seguir:

## Tabuleiro e Início
- Numa partida desse jogo, os jogadores se alteram em rodadas, numa ordem definida aleatoriamente no começo da partida. Cada jogador sempre começa uma partida com saldo de 300.
- O tabuleiro é composto por 20 **propriedades** em sequência.
- Cada propriedade tem um custo de venda, um valor de aluguel, um proprietário, caso já estejam compradas, e seguem uma determinada ordem no tabuleiro.
- Não é possível construir nenhuma melhoria sobre as propriedades.

## Partidas

No começo da sua vez, o jogador joga um dado equiprovável de 6 faces, o qual determina quantas espaços no tabuleiro o jogador vai andar, sendo que:

- Ao cair em uma propriedade sem proprietário, o jogador pode escolher entre comprar ou não a propriedade. Esse é a única forma pela qual uma propriedade pode ser comprada.
- Ao cair em uma propriedade que tem proprietário, ele deve pagar ao proprietário o valor do aluguel da propriedade.
- Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo.

Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda. Ao comprá-la, ganha sua posse e perde a quantia da venda. Além disso, um jogador que fica com saldo negativo perde a partida e é eliminado, de modo que perde suas propriedades, as quais podem ser compradas por qualquer outro jogador.

## Condições de vitória

A partida termina nos casos em que:

- Restar somente um jogador com saldo positivo, a qualquer momento da partida, o qual é declarado o vencedor.
- O jogo estiver demorando muito, terminando  na milésima rodada, com a vitória do jogador com maior saldo. O critério de desempate é a ordem de turno dos jogadores nesta partida.

## Jogadores

Há 4 diferentes tipos de possíveis jogadores, cujo comportamento dita suas ações durante o jogo:

- **Impulsivo**: compra qualquer propriedade sobre a qual ele parar.
- **Exigente**: compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
- **Cauteloso**: compra qualquer propriedade, desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
- **Aleatório**: compra a propriedade em que ele parar em cima com probabilidade de 50%.

## Objetivo

A ideia é rodar uma simulação de várias partidas, para decidir qual a melhor estratégia dentre as 4 citadas. Assim sendo, a saida de uma execução do **script principal** serão os dados referntes ao conjunto de simulações executadas (*default* 300), sendo:

- Quantas partidas terminam por *time out* (1000 rodadas).
- Quantos turnos, em média, demora uma partida.
- Qual a porcentagem de vitórias por comportamento dos jogadores.
- Qual o comportamento mais vitorioso.

## Estrutura e execução

O projeto foi implementado seguindo princípios de Orientação a Objetos e *Clean Code*, de modo que foram definidas Classes para representação das entidades **Jogador**, **Propriedade**, **Tabuleiro** e **Jogo**, as quais possuem os métodos responsáveis pela execução de suas ações, construindo o fluxo do jogo.

O script **simulation.py** é respnsável por iniciar um conjunto de simulações e gerar as estatísticas de saída. Por default, são executadas 300 simulações, bastando alterar esse valor na chamada do método de simulação, no __main__. Para cada partida, será definido, aleatoriamente, a quantidade de jogadores de cada tipo, de modo que sempre haverá no mínimo 1 jogador de cada tipo, e no máximo 3. Assim sendo, a partida poderá ter de 4 a 12 jogadores.

Não há necessidade de instalação de nenhuma dependência para execução do projeto, bastando utilizar alguma versão recente do Python.

Devido à simplicidade, não há necessidade de um banco de dados para obter os valores de venda e aluguel de cada propriedade. Ao invés disso, esses valores s]ao gerados em tempo de execução, na inicialização da classe do Tabuleiro. Foi definido um padrão, segundo o qual cada grupo de 5 propriedades terá o mesmo valor de aluguel e venda, os quais irão variar, respectivamente, de 25 a 100, e de 100 a 400, sendo o aluguel sempre 4 vezes maior do que o valor de compra. 

Dessa forma, uma propriedade poderá ter o aluguel de 25 e valor de compra de 100, o aluguel de 50 e valor de compra de 200, e assim pro diante. Essa decisão foi para que os valores ficassem proporcionais ao saldo dos jogadores e seu crescimento durante a partida, possibilitando maior poder de compra e consistência nos resultados das simulações.
