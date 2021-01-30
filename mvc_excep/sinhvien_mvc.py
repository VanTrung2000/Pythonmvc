import db_exceptions
import sinhvien_db
import sinhvien_model, sinhvien_view, sinhvien_controller

def start():
    try:
        # Khởi tạo đối tượng model
        model = sinhvien_model.SinhVienModel("localhost", "root", "123456", "demo")
        #model = sinhvien_model.SinhVienModel("localhost", "root", "1234567", "demo")
        # Khởi tạo đối tượng view
        view = sinhvien_view.SinhVienView()
        # Khởi tạo controller
        controller = sinhvien_controller.SinhvienController(model, view)

        # Hiển thị tất cả dữ liệu của bảng sinhvien
        #controller.show_all_sinhvien1()
        controller.them_sinhvien("Trung dep trai")
        # Hiển thị tất cả dữ liệu của bảng sinh

        #controller.show_all_sinhvien()
    except db_exceptions.DatabaseConnection as err:
        print(err)

if __name__ == "__main__":
    start()
