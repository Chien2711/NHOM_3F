# Phân tích Giỏ hàng (Market Basket Analysis) - Lab 1

**Môn học:** Khai phá dữ liệu (Data Mining)
**Sinh viên thực hiện:** [Điền Tên Bạn Vào Đây]

## 1. Giới thiệu
Dự án này áp dụng thuật toán **Apriori** trên bộ dữ liệu bán lẻ trực tuyến (Online Retail) để tìm ra các quy luật kết hợp sản phẩm (Association Rules), hỗ trợ chiến lược bán chéo (Cross-selling).

## 2. Cấu trúc dự án
Dự án tuân thủ mô hình Hướng đối tượng (OOP):
- `src/`: Chứa thư viện xử lý dữ liệu (`DataCleaner`, `BasketPreparer`).
- `notebooks/`: Chứa notebook thực thi.
- `data/`: Dữ liệu đầu vào.

## 3. Kết quả nổi bật (Highlights)
- **Combo Cốc sứ:** Phát hiện cặp sản phẩm `COFFEE MUG APPLES DESIGN` và `PEARS DESIGN` có chỉ số Lift > 50.
- **Bộ Móc khóa:** Khách hàng có xu hướng mua trọn bộ móc khóa cho gia đình (Cửa trước, Cửa sau, Gara).

## 4. Hướng dẫn chạy
Cài đặt thư viện:
pip install -r requirements.txt