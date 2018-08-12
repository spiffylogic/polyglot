// To run: dart helloworld.dart

import 'dart:io';

void main(List<String> args) {
  print("Hello world!");

  for (var arg in args) {
    stdout.writeln(arg);
  }
}

