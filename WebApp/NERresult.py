import Token_P_C
import handle_inout
def response(text1):
    Token_P_C.token_text(text1)
    rs=handle_inout.load_test()
    return rs
