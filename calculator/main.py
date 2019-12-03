import sys
from PyQt5 import QtWidgets
from calculator import Ui_Form
import re


def find_all(sub, s):
    index_list = []
    index = s.find(sub)
    while index != -1:
        index_list.append(index)
        index = s.find(sub, index + 1)

    if len(index_list) > 0:
        return index_list
    else:
        return -1


class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    #实现pushButton_clicked()函数
    def pushButton1_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"1")
    def pushButton2_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"2")
    def pushButton3_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"3")
    def pushButton4_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"4")
    def pushButton5_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"5")
    def pushButton6_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"6")
    def pushButton7_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"7")
    def pushButton8_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"8")
    def pushButton9_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"9")
    def pushButton0_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"0")
    def pushButton_point_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+".")
    # %
    def pushButton_per_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"%")
    def pushButton_back_clicked(self):
        str = self.textEdit.toPlainText()
        str = str[0:-1]
        self.textEdit.setText(str)

    def pushButton_n_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"**")

    def pushButton_clear_clicked(self):
        self.textEdit.setText("")

    def pushButton_plus_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"+")
    def pushButton_minus_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"-")
    def pushButton_multiply_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"*")
    def pushButton_divide_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"/")

    def pushButton_square_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"**2")
    def pushButton_tri_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"**3")
    def pushButton_sqrt_clicked(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"**0.5")

    def pushButton_equal_clicked(self):
        content = self.textEdit.toPlainText()
        if "%" not in content:
            rst = eval(content)
            print(rst)
            self.textEdit.setText(str(rst))
        else:
            pattern = re.compile(r'[\*+-/%]')
            m = pattern.findall(content)
            print(m)
            x = re.finditer(pattern,content)
            positions = [i.start() for i in x]
            print(positions)
            positions = [i for i in positions if content[i]!="."]
            m = [s for s in m if s != "."]
            # print(positions)
            # print(m)
            rep_index = []
            rep = []
            for i,p in enumerate(m):
                if p=='%':
                    if i == 0:
                        st = 0
                        se = positions[i]
                    else:
                        st = positions[i-1]+1
                        se = positions[i]
                    rep.append(str(float(content[st:se])/100))
                    rep_index.append([st,se])
            # print(rep)
            # print(rep_index)

            # generate new content without %
            new = ''
            N = len(content)
            if rep_index[0][0] == 0:
                if rep_index[-1][-1] < N-1:
                    p = len(rep_index)
                    for i in range(p):
                        new = new+rep[i]
                        if i != p-1:
                            new = new+content[rep_index[i][-1]+1:rep_index[i+1][0]]
                        else:
                            new = new+content[rep_index[i][-1]+1:]
                else:
                    p = len(rep_index)
                    for i in range(p):
                        new = new+rep[i]
                        if i != p-1:
                            new = new+content[rep_index[i][-1]+1:rep_index[i+1][0]]
            else:
                if rep_index[-1][-1] < N-1:
                    p = len(rep_index)
                    new = new + content[0:rep_index[0][0]]
                    for i in range(p):
                        new = new + rep[i]
                        if i != p-1:
                            new = new + content[rep_index[i][-1]+1:rep_index[i+1][0]]
                        else:
                            new = new + content[rep_index[i][-1]:]
                else:
                    p = len(rep)
                    new = new + content[0:rep_index[0][0]]
                    for i in range(p):
                        new = new + rep[i]
                        if i != p-1:
                            new = new + content[rep_index[i][-1] + 1:rep_index[i + 1][0]]

            print("original expression: ",content)
            print("transformed expression: ",new)
            rst = eval(new)
            print("Answer: ",rst)
            self.textEdit.setText(str(rst))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    app.exec_()
    # sys.exit(app.exec_())