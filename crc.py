def xor(dividend, divisor):
    """ XOR two binary numbers """
    result = ''
    for i in range(len(dividend)):
        result += '1' if dividend[i] != divisor[i] else '0'
    return result

def crc_remainder(message, divisor):
    """ Calculate CRC remainder for a given message and divisor """
    message = message + '0' * (len(divisor) - 1)  # Append zeros to message
    message_len = len(message)
    divisor_len = len(divisor)
    
    # Perform long division using XOR operation
    for i in range(message_len - divisor_len + 1):
        if message[i] == '1':  # If the current bit is 1, perform XOR
            message = message[:i] + xor(message[i:i+divisor_len], divisor) + message[i+divisor_len:]
    
    return message[-(divisor_len - 1):]  # Return the remainder (CRC)

def crc_check(message, divisor):
    """ Check if the received message is correct or contains an error """
    remainder = crc_remainder(message, divisor)
    if '1' in remainder:
        return False  # Error detected
    return True  # No error detected

# User input for message and divisor
message = input("Enter the binary message: ")
divisor = input("Enter the binary divisor (e.g., 1011 for x^3 + x + 1): ")

# Step 1: Append CRC to message before transmission
remainder = crc_remainder(message, divisor)
transmitted_message = message + remainder  # Complete message with CRC

print(f"Original Message: {message}")
print(f"Calculated CRC: {remainder}")
print(f"Transmitted Message: {transmitted_message}")

# Step 2: Simulate receiving the message and checking for errors
received_message = input("Enter the received message (with CRC): ")

# Check for errors in the received message
if crc_check(received_message, divisor):
    print("No error detected.")
else:
    print("Error detected in the received message.")
