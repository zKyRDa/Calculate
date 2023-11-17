import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import (
    QPropertyAnimation, QSequentialAnimationGroup, QPoint, QSize)
from desing import Ui_MainWindow
import math

mathexpression = ''
ActionConvertions = {'√': 'isqrt( ', 'ln': 'log( 2.71828182846, ', 'lg': 'log10( '}
special_action = ['^', '!', ')', '(']
deleteIndex = {}  # input : mathexpression

class CalcWindow(QMainWindow):
    def __init__(self):
        super(CalcWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # main calculator
        # digit buttons
        self.ui.Button_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.Button_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.Button_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.Button_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.Button_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.Button_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.Button_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.Button_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.Button_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.Button_9.clicked.connect(lambda: self.add_digit('9'))
        # action buttons
        self.ui.Button_C.clicked.connect(self.clear)
        self.ui.Button_comma.clicked.connect(self.add_point)
        self.ui.Button_plus.clicked.connect(lambda: self.add_action('+'))
        self.ui.Button_minus.clicked.connect(lambda: self.add_action('-'))
        self.ui.Button_multiply.clicked.connect(lambda: self.add_action('*'))
        self.ui.Button_split.clicked.connect(lambda: self.add_action('/'))
        self.ui.Button_BACKSPACE.clicked.connect(self.deleteBack)
        self.ui.Button_v.clicked.connect(lambda: self.add_special_action('^'))
        self.ui.Button_x1.clicked.connect(lambda: self.add_special_action('!'))
        self.ui.Button_scobs.clicked.connect(self.add_scobs)
        self.ui.Button_asin.clicked.connect(lambda: self.add_ready_function('asin'))
        self.ui.Button_sin.clicked.connect(lambda: self.add_ready_function('sin'))
        self.ui.Button_acos.clicked.connect(lambda: self.add_ready_function('acos'))
        self.ui.Button_cos.clicked.connect(lambda: self.add_ready_function('cos'))
        self.ui.Button_root.clicked.connect(lambda: self.add_ready_function('√'))
        self.ui.Button_atan.clicked.connect(lambda: self.add_ready_function('atan'))
        self.ui.Button_tan.clicked.connect(lambda: self.add_ready_function('tan'))
        self.ui.Button_ln.clicked.connect(lambda: self.add_ready_function('ln'))
        self.ui.Button_lg.clicked.connect(lambda: self.add_ready_function('lg'))
        self.ui.Button_plusminus.clicked.connect(lambda: self.add_bracketed_ready_function(' -'))
        self.ui.Button_1x.clicked.connect(lambda: self.add_bracketed_ready_function('1/'))
        self.ui.Button_Pi.clicked.connect(lambda: self.add_special_symbol('3,14159265359'))
        self.ui.Button_e.clicked.connect(lambda: self.add_special_symbol('2,71828182846'))
        self.ui.Button_equally.clicked.connect(lambda: self.equelly())  # result
        # other button
        self.ui.pushButton.clicked.connect(self.animMenu)

    def equelly(self):
        self.ui.input.setText(str(eval(mathexpression)))

    def deleteBack(self):
        global mathexpression
        self.ui.input.setText(self.ui.input.text()[:-1])

        mathexpression = mathexpression.replace(mathexpression.split()[-1][-1], '')
        self.processing()

    def processing(self):
        global mathexpression
        if self.ui.input.text()[0] == '0':
            self.ui.input.setText(self.ui.input.text()[1:])
        self.ui.input.setStyleSheet('''color: white;
                                    font-size: 30pt;
                                    border: none;''')
        print(mathexpression)
        print(deleteIndex)
        try:
            self.ui.label.setText(f'{self.ui.input.text()} = {str(eval(mathexpression))}')
        except SyntaxError:
            self.ui.label.setText('')

    def add_digit(self, btn_text: str):
        global mathexpression
        if self.ui.input.text() == '0':
            deleteIndex.update({len(self.ui.input.text()) - 1: len(mathexpression)})
        else:
            deleteIndex.update({len(self.ui.input.text()): len(mathexpression)})
        self.ui.input.setText(self.ui.input.text() + btn_text)
        mathexpression += btn_text

        self.processing()

    def add_point(self):
        global mathexpression
        if '.' not in mathexpression.split()[-1]:
            mathexpression += '.'
            self.ui.input.setText(self.ui.input.text() + ',')
            deleteIndex.update({len(self.ui.input.text()) - 1: len(mathexpression) - 1})
        self.processing()

    def add_action(self, math_act: str):
        global mathexpression
        if mathexpression[-1] in special_action or self.ui.input.text()[-1].isdigit():
            self.ui.input.setText(self.ui.input.text() + math_act)
            mathexpression += f' {math_act} '
            deleteIndex.update({len(self.ui.input.text()) - 1: f'{len(mathexpression) - 3} {len(mathexpression) - 1}'})
        else:
            self.ui.input.setText(self.ui.input.text()[:-1] + math_act)
            mathexpression = mathexpression.replace(mathexpression.split()[-1][-1], f'{math_act} ')
            deleteIndex.update({len(self.ui.input.text()) - 1: f'{len(mathexpression) - 4} {len(mathexpression) - 2}'})
        self.processing()

    def add_special_action(self, symbol: str):
        global mathexpression
        if not self.ui.input.text()[-1] == symbol:
            self.ui.input.setText(self.ui.input.text() + symbol)
            if symbol == '^':
                mathexpression += ' ** '
                deleteIndex.update({len(self.ui.input.text()) - 1: f'{len(mathexpression) - 4} {len(mathexpression) - 1}'})
            elif symbol == '!':
                if mathexpression.split()[-1] == ')':  # for expression in scobs
                    temp = ''
                    i = 0
                    for el in mathexpression[::-1]:
                        temp += el
                        if el == ')':
                            i += 1
                        elif el == '(':
                            i -= 1
                        if i == 0 and el != ' ':
                            symbol = temp[::-1]
                            break
                else:
                    symbol = mathexpression.split()[-1]
                mathexpression = mathexpression.replace(symbol, f'math.factorial({eval(symbol)})')
                deleteIndex.update({len(self.ui.input.text()) - 1: f'{len(mathexpression) - len(f'math.factorial({eval(symbol)})')} {len(mathexpression) - 1}'}) # ХЕРЬ
        self.processing()

    def add_ready_function(self, function: str):
        global mathexpression
        self.ui.input.setText(self.ui.input.text() + f'{function}(')
        functionincycle = False
        for el in ActionConvertions:
            if function == el:
                mathexpression += f'math.{ActionConvertions[el]}'
                functionincycle = True
                break
        if not functionincycle:
            mathexpression += f'math.{function}( '
        deleteIndex.update({f'{len(self.ui.input.text()) - len(f'{function}') - 1} {len(self.ui.input.text()) - 1}': f'{len(mathexpression) - len(f'math.{function}( ')} {len(mathexpression) - 2}'})
        self.processing()

    def add_bracketed_ready_function(self, function: str):
        global mathexpression
        if self.ui.input.text()[0:3] == f'{function}(':
            mathexpression = mathexpression[3:-1]
            self.ui.input.setText(self.ui.input.text()[3:-1])
        else:
            mathexpression = f'{function}( {mathexpression} )'
            self.ui.input.setText(f'{function}({self.ui.input.text()})')
        deleteIndex.update({f'0 2, {len(self.ui.input.text() - 1)}': f'0 3, {len(mathexpression) - 1}'})
        self.processing()

    def add_scobs(self):
        global mathexpression
        if self.ui.input.text()[-1] != '(' and self.ui.input.text()[-1] != ')':
            scob = '(' if self.ui.input.text().count('(') == self.ui.input.text().count(')') else ')'
            mathexpression += f' {scob} '
            self.ui.input.setText(self.ui.input.text() + scob)
            deleteIndex.update({f'{len(self.ui.input.text()) - 1}': f'{len(mathexpression) - 1}'})
        self.processing()

    def add_special_symbol(self, symbol: str):
        global mathexpression
        self.ui.input.setText(self.ui.input.text() + symbol)
        mathexpression += f'{symbol[0]}.{symbol[2:]}'
        deleteIndex.update({f'{len(self.ui.input.text()) - len(symbol)} {len(self.ui.input.text()) - 1}': f'{len(mathexpression) - len(symbol)} {len(mathexpression) - 1}'})
        self.processing()

    def clear(self):
        self.ui.input.setText('0')
        global mathexpression
        mathexpression = ''
        deleteIndex.clear()
        self.ui.input.setStyleSheet('''color: #757576;
                                    font-size: 30pt;
                                    border: none;''')
        self.ui.label.clear()
    # Other

    def animMenu(self):
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim_2 = QPropertyAnimation(self.child, b"size")
        self.anim_2.setEndValue(QSize(250, 150))
        self.anim_2.setDuration(2000)
        self.anim_2.start() 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalcWindow()
    window.show()
    sys.exit(app.exec())
