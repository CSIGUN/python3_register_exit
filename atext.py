import time
import atexit

def handle_exit():
	print("atexit.register()에 등록된 함수 호출 완료")

atexit.register(handle_exit)

while True:
	print("작업중 .. ")
	time.sleep(1)
