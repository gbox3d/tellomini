#%%
#기본모듈로만 사용한예제 
import socket
from time import sleep
import curses

# 상태정보를 받는 포트 지정 
local_ip = ''
local_port = 8889
cmd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
cmd_socket.bind((local_ip, local_port))

status_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
status_socket.bind((local_ip, 8890))


tello_ip = '192.168.10.1'
tello_port = 8889
tello_adderss = (tello_ip, tello_port)

# # 상태 출력
sleep(1)
print('ready')
# response, ip = status_socket.recvfrom(1024)
# print(response.decode())
# sleep(1)

while True:
    cmd_socket.settimeout(3)
    cmd_socket.sendto('command'.encode('utf-8'), tello_adderss)

    try:
        response, ip = cmd_socket.recvfrom(1024)
        print(f"{response} , {ip}")
        if response == b'ok':
            break;
    except socket.timeout:
        print('time out')
        # pass
    
cmd_socket.settimeout(None)
    

#%%
#이륙시키기 
sleep(3)
print('take off')
cmd_socket.sendto('takeoff'.encode('utf-8'), tello_adderss)

response, ip = cmd_socket.recvfrom(1024)
print(f"{response} , {ip}")


# sleep(3)
print('cw')
cmd_socket.sendto('cw 90'.encode('utf-8'), tello_adderss)

response, ip = cmd_socket.recvfrom(1024)
print(f"{response} , {ip}")

print('up')
cmd_socket.sendto('up 50'.encode('utf-8'), tello_adderss)

response, ip = cmd_socket.recvfrom(1024)
print(f"{response} , {ip}")

print('cw')
cmd_socket.sendto('cw 90'.encode('utf-8'), tello_adderss)

response, ip = cmd_socket.recvfrom(1024)
print(f"{response} , {ip}")

#%%
print('land')
cmd_socket.sendto('land'.encode('utf-8'), tello_adderss)
response, ip = cmd_socket.recvfrom(1024)
print(f"{response} , {ip}")

response, ip = status_socket.recvfrom(1024)
print(f"{response} , {ip}")

print('done')


# %%
