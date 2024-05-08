from IMPORT import *

def main():
    start=dt.datetime.now()
    while True:
        error=False
        for tf in HYPER.timeframe :
            prcs=subprocess.run(f'ps -fA | grep {tf}',shell=True,capture_output=True)
            text=prcs.stdout.decode('utf8').split('\n')
            if len(text)!=6:
                error=True
        prcs=subprocess.run(f'ps -fA | grep Trading/data.py',shell=True,capture_output=True)
        text=prcs.stdout.decode('utf8').split('\n')
        if len(text)!=4:
            error=True
        if error:
            error_str=F.time_delta(start)
            raise Exception('The computer has stopped some application without/with python error:\n'+error_str)
        sleep(60)
if __name__=='__main__':
    try:
        main()
    except Exception as e:
        error_str=str(e)
        ERROR.send_error(error_str)
        raise
