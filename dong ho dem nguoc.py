# Nhập thư viện PySimpleGUI và thời gian
import PySimpleGUI as sg
import time

# Hàm để định dạng thời gian
def format_time(seconds):
  # Tính số giờ, phút và giây
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  seconds = seconds % 60
  # Trả về chuỗi thời gian có dạng hh:mm:ss
  return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Tạo một cửa sổ với một nút bắt đầu và một nút dừng
window = sg.Window("Đồng hồ đếm ngược", [[sg.Button("Bắt đầu"), sg.Button("Dừng")], [sg.Text(format_time(0), key="timer", size=(10, 1), font=("Arial", 20))]])

# Khởi tạo các biến
running = False # Biến để kiểm tra trạng thái đếm ngược
seconds = 0 # Biến để lưu số giây cần đếm ngược
start_time = 0 # Biến để lưu thời gian bắt đầu đếm ngược

# Lặp cho đến khi đóng cửa sổ
while True:
  # Cập nhật giao diện cửa sổ
  window.refresh()
  # Lấy sự kiện và giá trị từ cửa sổ
  event, values = window.read(timeout=10)
  # Nếu sự kiện là đóng cửa sổ hoặc nhấn nút thoát thì thoát khỏi vòng lặp
  if event in (sg.WIN_CLOSED, "Thoát"):
    break
  # Nếu sự kiện là nhấn nút bắt đầu thì bắt đầu đếm ngược
  elif event == "Bắt đầu":
    # Nhập số giây cần đếm ngược
    seconds = int(sg.popup_get_text("Nhập số giây: "))
    # Đặt trạng thái đếm ngược là True
    running = True
    # Lấy thời gian bắt đầu đếm ngược
    start_time = time.time()
  # Nếu sự kiện là nhấn nút dừng thì dừng đếm ngược
  elif event == "Dừng":
    # Đặt trạng thái đếm ngược là False
    running = False
  # Nếu đang đếm ngược thì cập nhật thời gian hiển thị
  if running:
    # Tính số giây còn lại
   
    remaining = seconds - int(time.time() - start_time)
    # Nếu số giây còn lại lớn hơn 0 thì cập nhật thời gian hiển thị
    if remaining > 0:
      window["timer"].update(format_time(remaining))
    # Nếu không thì hiển thị thông báo hết giờ và dừng đếm ngược
    else:
      window["timer"].update("Hết giờ!")
      sg.popup("Hết giờ!")
      running = False

# Đóng cửa sổ
window.close()