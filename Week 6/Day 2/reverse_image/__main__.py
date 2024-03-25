from modules.single_process import single_process
from modules.multi_process import multi_process

def main():
    single_process('./images/img1.jpg')
    multi_process('./images/img1.jpg')

if __name__ == "__main__":
    main()