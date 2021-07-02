# download opencv-python to use confidence parameter

import pyautogui as pag
import os
from function import open_app
from function import start_learn
from function import learn
from function import review
from function import LoopException


# main
def main():
    # 学习组数
    learnGroup = 12

    # 打开模拟器，需要管理员启动ide
    app_dir = r'C:\Program Files (x86)\MuMu\emulator\nemu\EmulatorShell\NemuPlayer.exe'
    os.startfile(app_dir)

    # 导入按钮的图片
    image_App = "Button/App.png"
    image_StartLearn = "Button/StartLearn.png"
    image_StartReview = "Button/StartReview.png"
    image_Remember = "Button/Remember.png"
    image_LearnNewWords = "Button/LearnNewWords.png"
    image_Know = "Button/Know.png"
    image_StartTest = "Button/StartTest.png"
    image_remind = "Button/remind.png"
    image_translation = "Button/translation.png"

    try:
        open_app(image_App)
        start_learn(image_StartLearn)
        pag.PAUSE = 10  # 等待一段时间，防止因为软件卡顿而没进入复习
        button_start = pag.locateOnScreen(image_StartReview, grayscale=True, confidence=0.8)
        print(button_start)
        if button_start is not None:  # 判断是否有单词需要复习
            button_StartReview = pag.locateOnScreen(image_StartReview, grayscale=True, confidence=0.9)
            pag.click(button_StartReview)
            print("开始复习")
            review(image_Remember,image_remind)
            while pag.locateOnScreen(image_LearnNewWords, grayscale=True, confidence=0.9) is None:  # 复习完成开始学习新单词
                pag.PAUSE = 1
            button_learn_new_words = pag.locateOnScreen(image_LearnNewWords, grayscale=True, confidence=0.9)
            pag.click(button_learn_new_words)
            print("学习新词")
            learn(image_Know, image_StartTest, int(learnGroup), image_translation)
        else:
            print("学习新词")
            learn(image_Know, image_StartTest, int(learnGroup), image_translation)

    except LoopException as error:      # 返回错误信息
        print(error)


# 运行
if __name__ == '__main__':
    main()
