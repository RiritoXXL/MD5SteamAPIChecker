import hashlib as hash

def Main():
    steam_x64 = open("steam_api64.dll", "rb").read() #Steam_API X64 DLL Read
    md5_hash_steamapi64 = hash.md5(steam_x64).hexdigest()
    print(md5_hash_steamapi64)

if __name__ == "__main__":
    Main()