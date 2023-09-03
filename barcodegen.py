# import EAN13 and Code128 from barcode module
from barcode import EAN13, Code128
  
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter


# Take the input data from the user and assign it to variable data
data = input("Enter bardcode data: ") 

# Check the contents of the data variable if numeric
data_chk = data.isnumeric()
  
# Check if the bar code data is numeric
if data_chk:
    # Check if the length of the number of digits is greater than 0 and not greater than 13
    if len(data) <= 13 and len(data) > 0:
        # create an object of EAN13 class and 
        # pass the number with the ImageWriter() as the writer
        bar_code = EAN13(data, writer=ImageWriter())
        # Save the barcode image
        bar_code.save("barcode_num")
    else:
        print('The number of digits in this bar code should not exceed 13')
else:
    # create an object of Code128 class  to generate barcode from alphanumeric data and 
    # pass the number with the ImageWriter() as the writer
    bar_code = Code128(data, writer=ImageWriter())
    # Save the barcode image
    bar_code.save("barcode_alphanum")