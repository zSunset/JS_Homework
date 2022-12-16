import os
def main():
    update = False
    name = input('Введите имя игрока: ')
    total = input('Введите количество балов: ')
    with open('str.html', 'w', encoding='UTF-8') as f:
        f.write('<html>\n'
                '<head>\n'
                '</head>\n'
                '<body>\n'
                '  <center>\n'
                f'   <h1>{name}</h1>\n'
                f' </center>\n'
                f' <hr />\n'
                f' {total}\n'
                f' <hr />\n'
                f'</body>\n'
                f'</html>\n')
if __name__ == '__main__':
    main()