import serial
import time

def read_serial_line():
    port = "COM6"
    baudrate = 9600

    try:
        ser = serial.Serial(port, baudrate, timeout=1)
    except serial.SerialException as e:
        print(f"시리얼 포트 열기 실패: {e}")
        return

    time.sleep(2)
    print(f"[INFO] {port} 연결 완료")

    # 로그 파일 열기
    imu1_log = open("imu1_log.csv", "w")
    imu2_log = open("imu2_log.csv", "w")

    try:
        while True:
            raw = ser.readline()
            if not raw:
                continue

            line = raw.decode('utf-8', errors='ignore').strip()

            if line.startswith("IMU1,"):
                label = "IMU1"
                line = line[5:]
                target_log = imu1_log
            elif line.startswith("IMU2,"):
                label = "IMU2"
                line = line[5:]
                target_log = imu2_log
            else:
                continue  # 센서 라벨 없으면 건너뜀

            parts = line.split(',')
            try:
                values = [float(p) for p in parts]
            except ValueError:
                print(f"[WARN] 파싱 실패: {line}")
                continue

            # 데이터 출력
            print(f"[{label}] {values}")

            # 로그 파일에 저장
            timestamp = time.time()
            csv_line = f"{timestamp}," + ",".join([str(v) for v in values]) + "\n"
            target_log.write(csv_line)

    except KeyboardInterrupt:
        print("\n[INFO] 수신 종료")

    finally:
        ser.close()
        imu1_log.close()
        imu2_log.close()
        print("[INFO] 포트 닫힘, 로그 저장 완료")



