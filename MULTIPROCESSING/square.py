import multiprocessing
def square(n):
    return n**2
if __name__ == '__main__':
    with multiprocessing.Pool(processes=5) as pool :
        out =pool.map(square , [3,4,5,6,6,7,87,8,8])
        print(out)