import pytest
from electricity import calculate_electricity_bill  # Import từ file electricity.py
import pandas as pd

# Định nghĩa file output
output_file = "test_results.csv"

# Tạo file CSV với tiêu đề ngay từ đầu
columns = ["Test ID", "kWh", "Household Type", "Expected Output", "Actual Output", "Passed"]
df = pd.DataFrame(columns=columns)
df.to_csv(output_file, index=False, encoding="utf-8")

@pytest.mark.parametrize("test_id, kwh, household_type, expected", [
    ("TC1", 5000, "family", "Đầu vào không hợp lệ"),
    ("TC2", 50, "residential", 83900),
    ("TC3", 80, "business", 209000),
    ("TC4", 180, "business", 505000),
    ("TC5", 300, "business", 915000)
])
def test_calculate_electricity_bill(test_id, kwh, household_type, expected):
    result = calculate_electricity_bill(kwh, household_type)
    passed = result == expected
    
    # Ghi kết quả vào file ngay sau mỗi lần kiểm thử
    df = pd.DataFrame([[test_id, kwh, household_type, expected, result, passed]], columns=columns)
    df.to_csv(output_file, mode='a', header=False, index=False, encoding="utf-8")
    
    assert passed

if __name__ == "__main__":
    # Chạy pytest nhưng không chặn quá trình ghi file
    pytest.main(["-v", "--tb=short", "--disable-warnings"])
    
    print(f"\n===== KẾT QUẢ KIỂM THỬ =====\nĐã lưu kết quả vào {output_file}")