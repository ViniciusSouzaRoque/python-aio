# Simple Factory

### O que é?
Simple Factory é um padrão de projeto criacional que permite criar objetos de diferentes classes sem expor a lógica de criação ao cliente. O cliente apenas fornece um parâmetro que indica o tipo de objeto que deseja e recebe uma instância da classe correspondente.

### Vantagens
Algumas vantagens da Simple Factory são:

- Encapsula a lógica de criação dos objetos, tornando o código mais simples e fácil de manter.
- Permite adicionar novos tipos de objetos sem alterar o código do cliente, bastando modificar a classe Factory.
- Permite ocultar os detalhes de implementação das classes concretas, expondo apenas uma interface comum.

### Desvantagens
- Viola o princípio da responsabilidade única, pois a classe Factory tem mais de uma razão para mudar: se a lógica de criação mudar ou se novos tipos de objetos forem adicionados.
- Pode gerar um acoplamento forte entre o cliente e a classe Factory, dificultando a substituição ou a extensão da Factory.
- Pode não ser adequada para cenários onde há muitos tipos de objetos diferentes ou onde a lógica de criação é complexa ou dinâmica.

### Meu exemplo
No meu exemplo, eu criei uma classe abstrata Pessoa que define duas operações abstratas: tipo_de_pessoa e documento. Essas operações devem ser implementadas pelas subclasses concretas PessoaFisica e PessoaJuridica, que representam os dois tipos de pessoa possíveis. Em seguida, eu criei uma classe PessoaFactory que possui um método estático get_pessoa que recebe um parâmetro tipo e retorna uma instância de PessoaFisica ou PessoaJuridica, dependendo do valor do parâmetro. Por fim, eu usei a PessoaFactory para criar duas pessoas de tipos diferentes e chamei as operações definidas na classe Pessoa.

### Quando usar?
Você pode usar a Simple Factory quando:

- Você precisa criar objetos de diferentes classes, mas não quer expor a lógica de criação ao cliente.
- Você quer simplificar o código do cliente, evitando o uso de construtores complexos ou operadores new.
- Você quer ter um ponto único de controle para a criação dos objetos, facilitando a manutenção e a extensão.