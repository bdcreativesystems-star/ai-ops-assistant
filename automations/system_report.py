import platform

def generate_report():
    print("System:", platform.system())
    print("Node:", platform.node())
    print("Release:", platform.release())
    print("Version:", platform.version())
