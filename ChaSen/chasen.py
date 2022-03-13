import subprocess
import time

def strip_cmd_injection(instr):
    inj = [";", "|", "&", "`", "(", ")", "$", "<", ">", "*", "?", "{", "}", "[", "]", "!", "\n"]
    for s in inj:
        instr = instr.replace(s, "")
    instr = instr.replace("", "")
    return instr

def chasen(arg):
    arg = strip_cmd_injection(arg)
    cmd = "echo {0} | chasen -iw".format(arg)
    subprocess.Popen("chcp 65001", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.1) # chcp 65001の反映待ち
    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if stderr != b'':
        raise(Exception(stderr.decode('utf-8')))

    try:
        lines = stdout.decode('utf-8').split("\n")
    except:
        raise(Exception(stderr.decode('utf-8')))

    for line in lines:
        if (line == "EOS"):
            break
        yield line.split("\t")

if __name__ == '__main__':
    line = "'テストです。出来ていますか？'"
    for cha in chasen(line):
        print(cha)

# b"'\t'\t'\t\xe8\xa8\x98\xe5\x8f\xb7-\xe4\xb8\x80\xe8\x88\xac\t\t\n\x82\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\n\xb1\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\n\x82\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\n\xcc\x81\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\nA\t\xe3\x82\xa8\xe3\x82\xa4\tA\t\xe8\xa8\x98\xe5\x8f\xb7-\xe3\x82\xa2\xe3\x83\xab\xe3\x83\x95\xe3\x82\xa1\xe3\x83\x99\xe3\x83\x83\xe3\x83\x88\t\t\n\x96\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\n\xf0\x97\xa7\x82\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\n\xbd\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\n\x82\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\n\xb8\t\t\t\xe6\x9c\xaa\xe7\x9f\xa5\xe8\xaa\x9e\t\t\n'\t'\t'\t\xe8\xa8\x98\xe5\x8f\xb7-\xe4\xb8\x80\xe8\x88\xac\t\t\nEOS\n"
# b"'\t'\t'\t\xe8\xa8\x98\xe5\x8f\xb7-\xe4\xb8\x80\xe8\x88\xac\t\t\n\xe3\x81\x93\xe3\x81\xae\t\xe3\x82\xb3\xe3\x83\x8e\t\xe3\x81\x93\xe3\x81\xae\t\xe9\x80\xa3\xe4\xbd\x93\xe8\xa9\x9e\t\t\n\xe3\x80\x81\t\xe3\x80\x81\t\xe3\x80\x81\t\xe8\xa8\x98\xe5\x8f\xb7-\xe8\xaa\xad\xe7\x82\xb9\t\t\n\xe5\xbd\xb9\xe7\xab\x8b\xe3\x81\x9f\t\xe3\x83\xa4\xe3\x82\xaf\xe3\x83\x80\xe3\x82\xbf\t\xe5\xbd\xb9\xe7\xab\x8b\xe3\x81\xa4\t\xe5\x8b\x95\xe8\xa9\x9e-\xe8\x87\xaa\xe7\xab\x8b\t\xe4\xba\x94\xe6\xae\xb5\xe3\x83\xbb\xe3\x82\xbf\xe8\xa1\x8c\t\xe6\x9c\xaa\xe7\x84\xb6\xe5\xbd\xa2\n\xe3\x81\x9a\t\xe3\x82\xba\t\xe3\x81\xac\t\xe5\x8a\xa9\xe5\x8b\x95\xe8\xa9\x9e\t\xe7\x89\xb9\xe6\xae\x8a\xe3\x83\xbb\xe3\x83\x8c\t\xe9\x80\xa3\xe7\x94\xa8\xe3\x83\x8b\xe6\x8e\xa5\xe7\xb6\x9a\n'\t'\t'\t\xe8\xa8\x98\xe5\x8f\xb7-\xe4\xb8\x80\xe8\x88\xac\t\t\nEOS\n"

# '	'	'	記号-一般\t\t\n
# この	コノ	この	連体詞\t\t\n
# 、	、	、	記号-読点\t\t\n
# 役立た	ヤクダタ	役立つ	動詞-自立	五段・タ行	未然形\n
# ず	ズ	ぬ	助動詞	特殊・ヌ	連用ニ接続\n
# '	'	'	記号-一般\t\t\n
# EOS\n










