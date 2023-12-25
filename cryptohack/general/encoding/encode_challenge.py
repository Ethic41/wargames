#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-02 21:13:34
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from pwn import *
from Crypto.Util.number import long_to_bytes
from json import dumps as json_encode
from json import loads as json_decode
from binascii import unhexlify
from base64 import b64decode
import codecs

def main():
    cnx = remote("socket.cryptohack.org", 13377)
    while True:
        remote_input = json_decode(cnx.recvline().decode().strip("\n"))
        if "flag" in remote_input:
            print(remote_input["flag"])
            break

        if "type" in remote_input:
            print(remote_input)
            
            if remote_input["type"] == "base64":
                cnx.send(get_response(b64decode(remote_input["encoded"]).decode()))
            
            if remote_input["type"] == "hex":
                cnx.send(get_response(unhexlify(remote_input["encoded"]).decode()))
            
            if remote_input["type"] == "bigint":
                cnx.send(get_response(long_to_bytes(int(remote_input["encoded"], base=16)).decode()))
            
            if remote_input["type"] == "rot13":
                cnx.send(get_response(codecs.decode(remote_input["encoded"], "rot_13")))
            
            if remote_input["type"] == "utf-8":
                cnx.send(get_response("".join([chr(i) for i in remote_input["encoded"]])))
            

def get_response(payload):
    return json_encode({"decoded": payload}).encode()
if __name__ == "__main__":
    main()

