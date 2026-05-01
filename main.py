from grades import *

def main():
    application = QApplication([])
    window = Grades()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()