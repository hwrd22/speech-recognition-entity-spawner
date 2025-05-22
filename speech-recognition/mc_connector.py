import socket
import json
import os


class MCConnector:
  host = 'localhost'
  port = 0
  clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def __init__(self, port):
    self.port = port
    try:
      self.clientSocket.connect((self.host, self.port))
    except ConnectionRefusedError:
      print("Could not connect to Minecraft. Please make sure Minecraft is running (with the mod) first.")
      exit(1)
  
  def stream(self, cmdList):
    for cmd in cmdList:
      try:
        self.clientSocket.send((cmd + '\r\n').encode('utf-8'))
      except ConnectionResetError:
        print("Minecraft instance is no longer running. Please restart Minecraft to use this script.")
        exit(0)
      except Exception as e:
        print(cmd)
        raise e