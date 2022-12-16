# Safe-Termux

Esse projeto não está em fase funcional, e esta momentaneamente descontinuado, o por conta de alguns bugs e mau-funcionamento, não por causa do código em si, e sim por causa do modo de funcionamento do Termux, que entra em conflinto com o modo de funcionamento do programa.

---

Esse projeto tem como objetivo criar um sistema de senha digitada + biometria, para a proteção do Termux contra acessos de terceiros, básicamente o programa deve ser indicado para ser iniciado como shell padrão, para isso o usuário deverar executa o instalador do programa pelo comando:

>./install.py

A parti desse momento, sempre que o usuário abrir uma shell ele deve ou colocar sua digital para desbloquear seu Termux, ou colocar sua senha de usuário.

Se o usuário errar a senha muitas vezes, tentar fechar o Termux e o abrir novamente, o programa ira ver os logs anteriores das tentativas de senhas falhas, e atráves de quantas tentativas o usuário fracassar, ou o programa ira travar permanentemente, deixando impossível se iniciar o Termux novamente sem que precise limpar o armazenamento do Termux.

Um tipo de acontecimento alternativo que poderia acontecer caso o usuário erre a senha demais, seria a possibilidade do Termux limpar todo armazenamento dele mesmo + o armazenamento do celular inteiro, e após tudo isso se executar um *fork bomb* para travar o aparelho por um tempo, mas, por causa de alguns bugs e pelo alto risco e perigo dessa função, ela fica desativada por padrão, e foi descontinuada.

~~Sim, eu sei que é irônico, uma função descontinuada dentro de um repositório descontinuado.~~

Observação, existe chance de haver brechas de segurança na função *fail*, além de não funcionar corretamente e ser perigoso, há chances de brechas, então, novamente, eu recomendo fortemente que mantenha essa função desativada.
