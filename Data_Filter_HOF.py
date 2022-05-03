from data_list import DATA

def run():
    all_oldman_workers=[worker["name"] for worker in DATA if worker["age"]>=21]

    for worker in all_oldman_workers:
        print(worker)




if __name__=='__main__':
    run()