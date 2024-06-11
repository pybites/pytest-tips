from time import sleep

def call_api():
    sleep(60)  # faking a timeout
    return dict(
        status=200,
        response=[1, 2, 3]
    )
