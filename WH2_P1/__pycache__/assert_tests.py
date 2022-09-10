#Task 3 assert testing
# import morse
# def test_encode_us(s):
#     assert morse.encode(s) == '... --- ...', "Should be ... --- ..."
#     print("Everything passed")

import morse
def test_encode_us():
    assert morse.encode('us') == '..- ...', "Should be ..- ..."
    
if __name__ == "__main__":
    test_encode_us()
    print('Everything passed')




