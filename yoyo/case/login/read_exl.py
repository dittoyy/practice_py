# coding:utf-8
import xlrd

class read_excel():
    def __init__(self, path="testdata.xlsx", sheetName=u'login'):
        data = xlrd.open_workbook(path)
        self.table = data.sheet_by_name(sheetName)
        # 读取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols


    def read_dict(self):
        r = []
        j =1
        for i in range(self.rowNum-1):
            s = {}
            # 从第二行取对应values值
            values = self.table.row_values(j)
            for x in range(self.colNum):
                s[self.keys[x]] = values[x]
            r.append(s)
            j+=1
        return r



if __name__ == "__main__":
    d = read_excel()
    print d.read_dict()







