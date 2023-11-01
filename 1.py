import time

def book_system(name, roll_number):
    start_time = time.time()
    end_time = start_time + 600  # 10 minutes in seconds

    print("Booking System...")
    time.sleep(2)  # Simulating some processing time

    current_time = time.time()

    if current_time <= end_time:
        print("Booking Successful!")
        print(f"Name: {name}")
        print(f"Roll Number: {roll_number}")
        print(f"Booking Time: {time.ctime(start_time)} - {time.ctime(current_time)}")

        remaining_time = int(end_time - current_time)
        while remaining_time > 0:
            mins, secs = divmod(remaining_time, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(f"Time remaining: {timeformat}", end='\r')
            time.sleep(1)
            current_time = time.time()
            remaining_time = int(end_time - current_time)

        print("\nBooking Time Expired. Session Ended.")
    else:
        print("Booking Cancelled. Time Exceeded 10 minutes.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    roll_number = input("Enter your roll number: ")
    book_system(name, roll_number)
