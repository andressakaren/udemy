import 'package:flutter/material.dart';

class Questao extends StatelessWidget {
  
  final String texto;

  // criar contrutor
  const Questao(this.texto, {super.key});

  @override
  Widget build(BuildContext context) {
    return Text(texto);
  }
}

// como não tem mais acesso a pergunta, vou esperar receber o valor pelo construtor do meu conmponente. 