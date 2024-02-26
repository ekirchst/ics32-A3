# Evan Kirchstter
# ekirchst@uci.edu
# 59946460
import socket
import json
server_adress = "168.235.86.101"
server_port =  "3021"



def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  try: 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
      server_conn.connect((server, port))
      stuff = {}
      if bio:
          stuff["token"] = "user_token"
          stuff["bio"] = {
            "entry": bio,
            "timestamp": ""
            }
      else:
          stuff["join"] = {
                    "username": username,
                    "password": password,
                    "token": ""
                }
          if message:
                    stuff["token"] = "user_token"
                    stuff["post"] = {
                        "entry": message,
                        "timestamp": ""
                    }
      data_str = json.dumps(stuff)
      server_conn.sendall(data_str.encode())

      response = server_conn.recv(4096).decode()
      response_json = json.loads(response)
      print(response_json)
      if "response" in response_json:
                if response_json["response"]["type"] == "ok":
                    return True
                else:
                    error_message = response_json["response"]["message"]
                    print("Error:", error_message)
                    return False
      else:
          print("Invalid response from server")
          return False
  except Exception as e:
    print(f"there was an error:  {e}")
  return 
