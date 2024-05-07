from IMPORT import *

def main():
    while True:
        prcs=subprocess.run('ps -fA | grep .py',shell=True,capture_output=True)
        text=prcs.stdout.decode('utf8').split('\n')
        start=dt.datetime.now()
        if len(HYPER.timeframe)*3+5!=len(text):
            error_str=F.time_delta(start)
            print(len(text),len(HYPER.timeframe)*3+6,text)
            raise Exception('The computer has stopped some application without/with python error:\n'+error_str)
        sleep(5)
if __name__=='__main__':
    try:
        main()
    except Exception as e:
        error_str=str(e)
        ERROR.send_error(error_str)
        raise
