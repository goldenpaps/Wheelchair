#import serial
import pynmea2
from openai import openai

# Configure the serial port
GPS_PORT = "COM7"  #  COM_ on Windows
BAUD_RATE = 38400  # specific to gps module


if __name__ == "__main__":
    read_gps()



def read_gps():
    try:
        # Open the serial port
        with serial.Serial(GPS_PORT, BAUD_RATE, timeout=1) as ser:,
            while True:
                line = ser.readline().decode('utf-8', errors='ignore')  # Read GPS data
                if line.startswith('$GPGGA') or line.startswith('$GPRMC'):  # Focus on essential NMEA sentences
                    try:
                        msg = pynmea2.parse(line)  # Parse the GPS sentence
                        print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}, Time: {msg.timestamp}")

				try: 
					client = OpenAI(
 					api_key="sk-proj-yog_Wv_yPE5GYOVMZgYBbLMwlvjIe2Fnco4UDbs7N22ymvmItASs3vQmLk3HmhrPim4tRSGa-																		eT3BlbkFJXPsQN4ecTqOLoCR1ZjtXH9iM2Kl07dDJ8MuXDsf3XYPUekigMeFYQHylKpZqER42uI-x7y0GYA")

					completion = client.chat.completions.create(
  					model="gpt-4o-mini",
  					store=True,
  					messages=[
    					{"role": "user", "Latitude: {msg.latitude}, Longitude: {msg.longitude}, Time: {msg.timestamp}": "Based on the coordinates i am providing, what is the best way to get to (BLANK)?"}
  					]
					)

				except Exception as e:
					return f"Error communication with OpenAI: {e}"

print(completion.choices[0].message);
                    except pynmea2.ParseError:
                        print("Failed to parse GPS data")
    except serial.SerialException:
        print("Could not open serial port")
