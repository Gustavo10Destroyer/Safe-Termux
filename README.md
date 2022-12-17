# Safe-Termux

Esse projeto cria um sistema de bloqueio para o seu Termux, que pode ser desbloqueado por impressão digital ou senha digitada, caso alguém pegue seu aparelho e tente logar até atingir o limite, o Termux ira se bloquear para sempre, e só será possível acessar o Termux caso o usuário limpe o armazenamento do app.

Existe uma função que é desativada por padrão, que serve para limpar todo armazenamento do aparelho e do Termux, mas por questão de segurança, deixamos desativado por padrão.

# Instalação rápida

```sh
bash -c "$(curl -s https://raw.githubusercontent.com/Imperador-RIC/Safe-Termux/main/install.sh)"
```

---

A parti do momento que o usuário executa o instalador pelo comando abaixo:

>./install.py

Ele terá que definir sua senha de usuário, lembre-se, a senha não é possível ser alterada, então, escolha com sabedoria.

Sempre que o usuário abrir uma shell ele deve ou colocar sua digital para desbloquear seu Termux, ou colocar sua senha de usuário.

Se o usuário errar a senha muitas vezes, tentar fechar o Termux e o abrir novamente, o programa ira ver os logs anteriores das tentativas de senhas falhas, e atráves de quantas tentativas o usuário fracassar, ou o usuário terá suas últimas chances para tentar desbloquear o Termux, ou o programa ira travar permanentemente o Termux, deixando impossível se iniciar o Termux novamente sem que precise limpar o armazenamento do app.

Um tipo de acontecimento alternativo que poderia acontecer caso o usuário erre a senha demais, seria a possibilidade do Termux limpar todo armazenamento dele mesmo, + o armazenamento do celular inteiro, e após tudo isso se executar um *fork bomb* para travar o aparelho por um tempo, mas, por causa de alto risco e perigo dessa função, ela fica desativada por padrão.

Bom, espero que gostem do meu repositório, o código não está perfeito nem de longe, da pra otimizar ele usando funções e outras coisas, mas no momento, é isso que posso lhe entregar a vocẽs.

## Observações:

### Detalhes

Da para se alterar a senha ou desinstalar o programa, mas para isso eu não irei ajudar vocẽs, façam esses procedimentos por vontade própria com seus métodos próprios.

É obrigatório se ter o Termux API instalado, caso contrário o programa não ira funcionar, é obrigatório para o funcionamento do programa.

## Créditos:
<p align="center">Responsáveis pelo projeto</p>
<p align="center">– <strong>d3str0yer</strong> • <strong>Imperador RIC</strong> • <strong>Dark Walker</strong> –</p>

Agradecimentos especiais a vocês que me ajudaram nesse projeto, agradeço ao [`d3str0yer](https://github.com/Gustavo10Destroyer) por todo apoio e suporte com as partes mais complexas do código, agradeço ao Dark Walker por me ajudar com todo o projeto do início ao fim, por me ajudar com a arte ASCII, variáveis, obrigado por literalmente tudo.
