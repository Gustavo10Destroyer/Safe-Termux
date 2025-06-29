# Safe-Termux

Esse projeto cria um sistema de bloqueio para o seu Termux, que pode ser desbloqueado por impressão digital ou senha digitada, caso alguém pegue seu aparelho e tente logar até atingir o limite, o Termux ira se bloquear para sempre, e só será possível acessar o Termux caso o usuário limpe o armazenamento do app.

Existe uma função que é desativada por padrão, que serve para limpar todo armazenamento do aparelho e do Termux, mas por questão de segurança, deixamos desativado por padrão.

---

# Instalação

A partir do momento que o usuário clona o repositório e executa o instalador pelo comando abaixo:
```bash
python ./install.py
```

Ou executa o comando abaixo de instalação rápida:
```bash
bash -c "$(curl -s https://raw.githubusercontent.com/Gustavo10Destroyer/Safe-Termux/master/install.sh)"
```

## Nota
O comando de [`instalação`](#instalação) rápida apaga o Safe-Termux, caso já esteja instalado, e baixa novamente a versão mais atual

Ele terá que definir sua senha de usuário, lembre-se, a senha não é possível ser alterada, então, escolha com sabedoria.
Sempre que o usuário abrir uma shell ele deve ou colocar sua digital para desbloquear seu Termux, ou colocar sua senha de usuário.

Se o usuário falhar com a biometria e 3 vezes consecultivas com a senha, o Termux será bloqueado, apagando todo o armazenamento do app

Um tipo de acontecimento alternativo que poderia acontecer caso o usuário erre a senha demais, seria a possibilidade do Termux limpar todo armazenamento dele mesmo, + o armazenamento do celular inteiro, e após tudo isso se executar um *fork bomb* para travar o aparelho por um tempo, mas, por causa de alto risco e perigo dessa função, ela fica desativada por padrão.

Bom, espero que gostem do meu repositório, o código não está perfeito nem de longe, da pra otimizar ele usando funções e outras coisas, mas no momento, é isso que posso lhe entregar a vocẽs.

## Observações:

Da para se alterar a senha ou desinstalar o programa, mas para isso eu não irei ajudar vocẽs, façam esses procedimentos por vontade própria com seus métodos próprios.

É obrigatório se ter o Termux API instalado, caso contrário o programa não ira funcionar, é obrigatório para o funcionamento do programa.

## Aviso de Segurança:

Apesar da alta segurança do nosso código, ele é possível de ser burlado, princípalmente por conta do *root*, de certos modelos de celulares no mercado, por conta do funcionamento do Termux e seu modo de segurança, entre outras coisas, nosso código é seguro, mas não absoluto.

## Créditos:

<p align="center">Responsáveis pelo projeto</p>
<p align="center">– <strong>Gustavo</strong> • <strong>Imperador RIC</strong> • <strong>Dark Walker</strong> –</p>

<strong>Obrigado [`Silver`](https://github.com/VantzBlackz) por fazer testes de penetração e descobrir 2 falhas importantes de segurança!</strong>
Agradecimentos especiais a vocês que me ajudaram nesse projeto, agradeço ao [`Gustavo`](https://github.com/Gustavo10Destroyer) por todo apoio e suporte com as partes mais complexas do código, agradeço ao [`Dark Walker`](https://github.com/ReiDarkWalker) por me ajudar com todo o projeto do início ao fim, por me ajudar com a arte ASCII, variáveis, obrigado por literalmente tudo.
