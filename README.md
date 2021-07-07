# Example1
- Như em tìm hiểu được thì việc sử dụng multiprocess sẽ tốn bộ nhớ hơn nhưng đảm bảo chương trình chạy mượt mà hơn.
Vì nếu 1 thread trong Process bị lỗi thì cả Process đó bị treo hoặc crash. Và execution time của chương trình multilprocess chạy nhanh hơn chương trình multilthread

- Từ Example trên em test trên máy thì execution time
  + Thread : 1.7600479125976562 s
  + Process: 1.6164443492889404 s
