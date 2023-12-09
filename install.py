import os, sys

# Linux stuff
UnixUser = os.environ["USER"]
UnixHome = os.path.expanduser("~")
UnitFile = "/etc/systemd/system/amogusmate.service"
amogusmate = "/usr/bin/amogusmate"

# check root permissions
if os.geteuid() != 0:
    print("Error: This script requires root permissions!")
    sys.exit(1)
elif not sys.platform.startswith("linux"):
    print("Error: This script is for Linux only!")
    sys.exit(1)
    
# check dependencies
Dependencies = ["tmate", "curl", "tmux"]
while True:
    for dependency in Dependencies:
        if os.system(f"which {dependency} > /dev/null 2>&1") != 0:
            print(f"Error: {dependency} is not installed!")
            sys.exit(1)
    break

# systemd unit template
SystemdUnit = f"""
[Unit]
Description=Send tmate session id over telegram
After=network.target

[Service]
User={UnixUser}
WorkingDirectory=/home/{UnixUser}/
ExecStart=/usr/bin/amogusmate
Restart=always

[Install]
WantedBy=multi-user.target
"""

# install

def install_amogusmate():
    if os.path.exists(f"{UnitFile}") and os.path.isfile(f"{UnitFile}"):
        os.remove(f"{UnitFile}")
    with open(f"{UnitFile}", "w") as f:
        f.write(SystemdUnit)
    os.system("systemctl daemon-reload")
    os.system("systemctl enable --now amogusmate")

def uninstall_amogusmate():
    if os.path.exists(f"{UnitFile}") and os.path.isfile(f"{UnitFile}"):
        os.system("systemctl daemon-reload")
        os.system("systemctl disable --now amogusmate")
        os.remove(f"{UnitFile}")
        os.remove(f"{amogusmate}")

def main():
    parser = argparse.ArgumentParser(description="amogusmate installer")
    parser.add_argument("--install", action="store_true", help="install amogusmate")
    parser.add_argument("--uninstall", action="store_true", help="uninstall amogusmate")
    args = parser.parse_args()
    if args.install:
        install_amogusmate()
    elif args.uninstall:
        uninstall_amogusmate()
    else:
        print("Error: No arguments given!")
        sys.exit(1)

if __name__ == "__main__":
    main()
