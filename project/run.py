#현재는 imu_reader.py 모듈만 실행 중

from imu_reader import read_serial_line


try:
    while True:
        line=read_serial_line()
        print(line)
        

except KeyboardInterrupt:     
     print("\n[INFO] Program stopped by user.")    
