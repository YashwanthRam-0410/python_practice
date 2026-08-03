import time

def timer(start_count):
    while start_count:
        print(f"Bomb will blast in {start_count} seconds")
        time.sleep(1)
        start_count-=1
    print("Blast off!")

timer(5)