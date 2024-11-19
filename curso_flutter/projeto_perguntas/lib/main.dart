import 'package:flutter/material.dart';
// import 'package:logging/logging.dart';

void main() => runApp(const PerguntaApp());
// runapp() é uma função do flutter que recebe um widget e coloca na tela
// const PerguntaApp() cria uma instancia do widget perguntarapp(). Se usa const antes da classe pra indicar que a classe pode ser otimizada pelo compilador para ser uma instancia constante. ou seja, ela permite que o flutter crie e reutilize a mesma instancia sempre q necessário, melhorando a performance do app.

// final Logger _logger = Logger('PerguntaApp');

/// essa classe gerencia o estado
class PerguntaAppState extends State<PerguntaApp> {
  var perguntaSelecionada = 0;

  void responder() {
    setState(() {
      perguntaSelecionada++;
    });
    print(perguntaSelecionada);
    print('Pergunta respondida!'); // é ideal usar o logger ao inves do print. Log de nível 'info'
  }

// implementar um método buid que é obrigatório pela classe statelesswidget (ou statefulwidget)
  @override
  Widget build(BuildContext context) {
    final perguntas = [
      'Qual é a sua cor favorita?',
      'Qual é o seu animal favorito?',
    ];

    // retorna criando uma instancia
    return MaterialApp(
      // atributos nomeados
      // home: Text('Olá mundo'),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Perguntas'),
        ),
        body: Column(
          children: <Widget>[
            Text(perguntas[perguntaSelecionada]),
            ElevatedButton(
              onPressed: () {
                responder();
              },
              child: const Text('Resposta 1'),
            ),
            ElevatedButton(
              onPressed: () {
                responder();
              },
              child: const Text('Resposta 2'),
            ),
            ElevatedButton(
              onPressed: () {
                responder();
              },
              child: const Text('Resposta 3'),
            ),
          ],
        ),
      ),
    );
  }
}

// esse extend é para tornar o perguntaApp um widget, nesse caso, imutável (não tem estado que muda durante a execução)
class PerguntaApp extends StatefulWidget {
  const PerguntaApp({super.key});

  @override
  PerguntaAppState createState() {
    return PerguntaAppState();
  }
}
