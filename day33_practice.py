def dec(f):
    def w():
        print("Before")
        f()
    return w
