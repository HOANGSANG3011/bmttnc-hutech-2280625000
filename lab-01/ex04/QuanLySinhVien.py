from SinhVien import SinhVien

class QuanlySinhVien:
    listSinhvien = []
    
    def generateID(self): 
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id 
            for sv in self.listSinhvien: 
                if (maxId< sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien._len_()
    
    def nhapsinhvien(self):
        svId= self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh của sinh vien: ") 
        diemTB = float(input("Nhap diem cua sinh vien: ")) 
        sv = SinhVien (svId, name, sex, major, diemTB) 
        self.xepLoaiHocLuc(sv) 
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh viên: ")
            major = int(input("Nhap chuyen6 ngành của sinh vien: "))
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID - {} khong ton tai." .format(ID))
    def sortByID(self):
        self.listSinhvien.sort(key=lambda x: x._id, reverse=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
    def sortByDiemTB (self):
        self.listSinhvien.sort(key=lambda x: x._diemTB, reverse=False)
        
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhvien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword): 
        listSV = []
        if (self.soLuongSinhVien() > 0): 
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()): 
                    listSV.append(sv)
        return listSV
    
    def deleteById(self, ID): 
        isDeleted = False
        sv= self.findByID(ID) 
        if (sv != None):
            self.listSinhvien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocluc = "Gioi"
        elif (sv. diemTB >= 6.5):
            sv. hocLuc = "Kha"
        elif (sv. diemTB >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yeu"
            
    def showSinhvien (self, listSV):
        print("{8} {:<18} {:<8} {:<8}{:<8} {:<8}"
            .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if (listSV._len_() > 0):
            for sv in listSV:
                print("{8} {:<18} {:<8} {:<8}{:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv. diemTB, sv. hocLuc))
        print("\n")
        
    def getListSinhVien(self):
        return self.listSinhVien