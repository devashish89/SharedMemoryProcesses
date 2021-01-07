import time
import multiprocessing



lst_numbers = []

def square_nums(numbers, arr, val):
    global lst_numbers
    for idx, num in enumerate(numbers):
        print(num*num)
        lst_numbers.append(num*num)
        arr[idx] = num*num

    val = 2.71


if __name__=='__main__':
    numbers = [1,2,3,4,5]
    arr = multiprocessing.Array('i',len(numbers)) # i:integer and d:double #Shared memory
    val = multiprocessing.Value('d',3.14) #shared memory
    p1 = multiprocessing.Process(target=square_nums, args=(numbers,arr,val))
    p1.start()
    p1.join()

    print(lst_numbers, arr[:], val)





