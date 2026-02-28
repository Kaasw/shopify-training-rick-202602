# Shopify Basics Documentation (Template)

## 1) Core Entities
### Product
Definition:
  Sản phẩm người bán tạo ra trên cửa hàng để bán cho customer

Key fields: 
  title: tên của sp
  productOptions (Optional): tạo các variant cho sp

### Variant
Definition:
  Biến thể của sản phẩm, chẳng hạn 1 sản phẩm có thể có nhiều màu sắc, chất liệu khác nhau.

Key fields:
  productId: cần thiết để gán variant đấy với sản phẩm
  options: chi tiết về variant đó, tên và các giá trị của variant tùy người bán đặt

### Collection (Smart / Custom)
Definition: 
  Group các product với nhau, ví dụ như clothes summer set thì có quần đùi áo cọc,...

Custom Collection: 
  Các product sẽ được add vào collection thủ công, tùy theo ý người bán

Smart Collection: 
  Set rules cho các product, sau đó hệ thống tự động nhét toàn bộ các product đó vào collection. Một rules ví dụ rule contain từ toilet ở trong title, khi đó tất cả các product có chữ toilet trong title sẽ được đưa vào collection.

Key fields:
  title: tên của collection
  description/descriptionHtml: thông tin mô tả collecton đó
  products: list id các products cần được thêm vào (Nếu đang tạo custom collection)
  ruleSet: rule do người bán định nghĩa để add vào smart collection.

### Customer
Definition: Người mua và sử dụng web bán hàng.

Key fields:
  firstName, lastName: tên của người bán
  phone: sdt 
  email 

### Order / Draft Order
Definition:
  Order: 1 đơn hàng user tạo ra khi tự mua hàng trên web
draftOrder: order được tạo bởi người bán cho khách hàng 

Key fields:
  customer: khách hàng đặt customer đó (nếu không có guest checkout)
  displayFinancialStatus: Trạng thái thanh toán của order
  name: Tên order
  price: có các giá như giá ship, giá tổng order, thuế

---

## 2) Entity Relationships
- Product -> Variants:
  Variant thuộc về product, product tạo trên web luôn có default là 1 variant do hệ thống tạo nếu khi tạo không thêm productOptions gì.
- Product -> Collection:
  Collection chứa các product id
- Customer -> Order:
  Khi customer tạo order hoặc được tạo draft order thì order sẽ chứa thông tin của customer đấy 
---

## 3) GraphQL Basics
- What is GraphQL?
   Là 1 dạng query language. GraphQL chỉ có 1 endpoint duy nhất nên client không cần phải tốn công viết nhiều request để gửi tới các endpoint khác nhau khi thao tác với data.
- Query vs Mutation:
    Mutation: Tạo và thay đổi data
    Query: Xem data
- Variables usage:
    Được gửi độc lập so với query, giống với cách truyền tham số vào hàm, giúp code dễ đọc và thao tác dễ hơn
- Handling errors:
  - HTTP errors
      Tùy theo status code mà có cách khắc phục
  - GraphQL errors
  - `userErrors`: message lỗi được trả về chi tiết, giúp user biết được chính xác vấn đề ở đâu, ví dụ như message ghi permission denied thì là do access token không có scope để sửa data đó. 