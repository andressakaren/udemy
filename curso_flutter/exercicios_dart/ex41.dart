class Pessoa {
  late String nome;
  late String _cpf;
}

main () {

  var p1 = Pessoa();
  p1.nome = 'Joao';
  p1._cpf = '123.456.789-00';

  print('O ${p1.nome} tem cpf ${p1._cpf}');
}