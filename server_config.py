import getpass

"""
The fabric module in python is used for connecting to
and configuring servers remotely.
To use it, it is required that the required packages from
the fabric module be imported and used.
"""

from fabric import Connection, Config

password = getpass.getpass("Enter the root password: \n")

config = Config(overrides={'sudo': {'password': password}})
conn = Connection("IP Address", user="username" config=config)


conn.run("ls -la", hide=True)

# Server config script