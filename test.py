def test_greet():
    from utils import greet
    assert greet('Ani') == 'Barev, Ani!'
    print('Тест пройден')


if __name__ == '__main__':
    test_greet()
