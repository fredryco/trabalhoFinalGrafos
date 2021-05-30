#!/usr/bin/python
import subprocess
from signal import SIGTERM, SIGKILL
import time
import sys
import os

def main(argumento, segundos):
  pilha = subprocess.Popen(argumento)
  time.sleep(segundos)
  pilha.poll()
  if pilha.returncode == None:
    sys.stderr.write("[%s] parar\n" % pilha.pid)

    #segundos para recarregar os arquivos
    os.kill(pilha.pid, SIGTERM)
    time.sleep(10)
    pilha.poll()
    if pilha.returncode == None:
      sys.stderr.write("[%s] kill\n" % pilha.pid)
      os.kill(pilha.pid, SIGKILL)

main(sys.argv[1:], 5*60)

# utilização:
#   ./pcvObserver.py <programa> <argumentos>
#   exemplo
#   ./pcvObserver.py primes.py

