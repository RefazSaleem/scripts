#!/usr/bin/env python3
import sys
import subprocess

def register_user(username, server, password):
    command = [
        "/home/refazsaleem/synapse/bin/register_new_matrix_user",
        server,
        "-c", "homeserver.yaml",
        "--user", username,
        "--password", password,
        "--admin"
    ]
    subprocess.run(command)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: synapse-register <username> <server_url> <password>")
        sys.exit(1)

    username = sys.argv[1]
    server = sys.argv[2]
    password = sys.argv[3]

    register_user(username, server, password)
    print(f"User {username} created successfully!")
