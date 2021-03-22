import os
import random
import subprocess


class Blive():

    def start(self):
        while True:
            try:
                # 获取随机文件，播放
                musicPath = '/home/pi/sharedir/livemusic/'
                randomMusic = self.getRandomFile(musicPath)
                musicName = os.path.basename(randomMusic)
                self.playMusic({
                    'name': musicName,
                    'filename': musicPath + randomMusic
                }, True)
            except Exception as e:
                exit(1)

    # 播放音乐
    def playMusic(self, music, autoPlay=False):
        imagePath = '/home/pi/ss.jpg'
        rtmp_addr = '直播平台推流码和推流地址'
        # 开始播放
        command = 'ffmpeg -re -loop 1 -f image2 -i "{}"  -i "{}" -vf drawtext=fontfile=/usr/share/fonts/chinese/SIMSUN.TTC:fontsize=16:fontcolor=#FFFFFF:text="正在播放\n\t{}" -c:a aac -c:v libx264  -shortest -r 25 -f flv "{}"'.format(
            imagePath,
            music['filename'], music['name'], rtmp_addr)
        process = subprocess.Popen(args=command, cwd=os.getcwd(), shell=True)
        process.wait()
        print('播放完成')

    # 获取随机文件
    def getRandomFile(self, path):
        fileList = os.listdir(path)
        if len(fileList) == 0:
            raise Exception('无法获取随机文件，%s为空' % path)
        index = random.randint(0, len(fileList) - 1)
        return fileList[index]


if __name__ == '__main__':
    blive = Blive()
    blive.start()
