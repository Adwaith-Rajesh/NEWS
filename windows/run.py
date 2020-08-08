
try:
    from main import MainWindow

except ImportError:
    from .main import MainWindow

finally:
    import socket
    import pymsgbox


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


if is_connected():
    m = MainWindow()

else:
    pymsgbox.alert(text='Your PC is not connected to the internet !', title='Connection Error',
                   button=pymsgbox.OK_TEXT)

