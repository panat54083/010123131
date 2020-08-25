# 6201012610052 Assingment สำหรับ Calculator โดยใช้ PyQT5

from PyQt5 import QtWidgets

from Main import Ui_MainWindow
from InfixConverter import Infix

class CalculatorWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.approve_decimal = True
        self.reset = False

        self.b_0.clicked.connect(self.digit_press)
        self.b_1.clicked.connect(self.digit_press)
        self.b_2.clicked.connect(self.digit_press)
        self.b_3.clicked.connect(self.digit_press)
        self.b_4.clicked.connect(self.digit_press)
        self.b_5.clicked.connect(self.digit_press)
        self.b_6.clicked.connect(self.digit_press)
        self.b_7.clicked.connect(self.digit_press)
        self.b_8.clicked.connect(self.digit_press)
        self.b_9.clicked.connect(self.digit_press)

        self.b_point.clicked.connect(self.decimal_press)

        self.b_del.clicked.connect(self.deleteAndClear_press)
        self.b_clear.clicked.connect(self.deleteAndClear_press)

        self.b_openBrac.clicked.connect(self.bracket_press)
        self.b_closeBrac.clicked.connect(self.bracket_press)

        self.b_add.clicked.connect(self.operator_press)
        self.b_sub.clicked.connect(self.operator_press)
        self.b_mul.clicked.connect(self.operator_press)
        self.b_div.clicked.connect(self.operator_press)

        self.b_perc.clicked.connect(self.percent_press)
        self.b_equal.clicked.connect(self.equal_press)

    def isNumber(self, c):
        if c in '0123456789':
            return True

    def digit_press(self):
        button = self.sender()
        text = self.l_display.text()
        if self.reset == True: # เริ่มต้นใหม่
            text = ''
            self.reset = False
        if text == '0':
            text = ''
        if ('.' in text and button.text() == '0') or ('('or'+'or'-'or'x'or'÷' in text):
            new_text = format(text + button.text(),'.15')
            
        if len(text) > 0:
            if text[-1] == ')' or text[-1] == '%': # ถ้าตัวก่อนหน้าเป็น ) หรือ % จะไม่ให้เติมตัวเลข
                new_text = format(text,'.15')
        self.l_display.setText(new_text)

    def decimal_press(self):

        self.reset = False
        text = self.l_display.text()
        if len(text) > 0:
            if text[-1] != '%' and self.approve_decimal == True: # ถ้ามีการอนุญาตให้เติมจุด / ยังไม่มีจุด
                new_text = text + '.'
                self.approve_decimal = False

            else: # There is decimal more than one
                new_text = text
        else:
            new_text = '0'+'.'
            self.approve_decimal = False

        self.l_display.setText(new_text)

    def deleteAndClear_press(self):

        self.reset = False
        text = self.l_display.text()
        button = self.sender()

        if button.text() == 'Delete':
            if len(text) > 0:
                if text[-1] == '.': # ถ้าเราลบจุดออก ก็จะสามารถเติมจุดได้อีก
                    self.approve_decimal = True
                self.l_display.setText(text[:-1])

        else: # button.text() == 'Clear'
            self.l_display.setText('0')
            self.approve_decimal = True
    
    def bracket_press(self):

        text = self.l_display.text()
        button = self.sender()
        
        if button.text() == '(':
            if text == '0': #ถ้าข้อความใน label เป็น 0
                text = ''

            if len(text) > 0 :
                if self.isNumber(text[-1]) or text[-1] in '.': # ถ้าตัวก่อนหน้า ( เป็นตัวเลข และเป็นเครื่องหมาย .
                    new_text = text
                else:
                    new_text = text + '('
            else:
                new_text = text+'('

        else: #button.text() == ')'
            if '(' in text: #ถ้ามี ( อยู่ใน label
                new_text = text + ')'
            else:
                new_text = text

            if len(text) > 0 :
                if text[-1] == '(':
                    new_text = text
        
        self.l_display.setText(new_text)

    def operator_press(self):

        self.reset = False
        text = self.l_display.text()
        button = self.sender()
        if len(text) > 0:
            if text[-1] not in '(+-x÷': # ถ้าข้างหน้า operator ที่จะเติมเป็น oper อีกตัวจะเติมไม่ได้
                if button.text() == '+':
                    new_text = text + '+'

                elif button.text() == 'x':
                    new_text = text + 'x'

                elif button.text() == '÷':
                    new_text = text + '÷'
            else:
                new_text = text
            if button.text() == '-':
                new_text = text + '-'
        else:
            new_text = text

        self.l_display.setText(new_text)

    def percent_press(self):

        self.reset = False
        text = self.l_display.text()
        if len(text) > 0:
            if self.isNumber(text[-1]):
                new_text = text + '%'
            else:
                new_text = text
        else:
            new_text = text
        self.l_display.setText(new_text)

    def equal_press(self):

        
        text = self.l_display.text()

        new_text = text.replace('x', '*')
        new_text = new_text.replace('÷', '/')
        new_text = new_text.replace('%', '*1/100')

        text_postfix = Infix(new_text)
        result = text_postfix.calculatePostfix()
        # print(text_postfix.convertPostfix())
        # print(result)
        self.reset = True
        self.l_display.setText(result)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CalculatorWin()
    sys.exit(app.exec_())
    
