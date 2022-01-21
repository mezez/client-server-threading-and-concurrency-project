import socket

def read_line(f):
    '''
    Reads one line from f, using \r\n as the end-of-line separator.
    Returns None when the connection is closed.
    Blocks until a line is received.

    This function does not read ahead, meaning it does is suitable to read just after read_line.
    '''
    res = b""
    was_r = False
    while True:
        b = f.recv(1)
        if len(b) == 0:
            return None
        if b == b"\n" and was_r:
            break
        if was_r:
            res += b"\r";
        if b == b"\r":
            was_r = True;
        else:
            was_r = False;
            res += b;
    return res.decode("utf-8")
