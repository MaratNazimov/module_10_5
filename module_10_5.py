import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            x = file.readline()
            if not x:
                break
        all_data.append(x)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()

for i in filenames:
    read_info(i)

end = datetime.datetime.now()

print(f'Линейный вызов: {end - start}')

if __name__ == '__main__':
    start = datetime.datetime.now()

    with multiprocessing.Pool(processes=6) as pool:
        pool.map(read_info, filenames)

    end = datetime.datetime.now()

    print(f'Многопроцессорный: {end - start}')
