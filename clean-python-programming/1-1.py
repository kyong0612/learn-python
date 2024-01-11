def a():
    print("aを開始")
    b()

def b():
    print("bを開始")
    c()

def c():
    print('cを開始')
    42/0 # この部分でエラーを起こす

a()
