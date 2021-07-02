import time
import pyautogui as pag


class LoopException(Exception):  # 返回错误信息，循环超时
    pass


image_App = "Button/App.png"
image_StartLearn = "Button/StartLearn.png"
image_StartReview = "Button/StartReview.png"
image_Remember = "Button/Remember.png"
image_LearnNewWords = "Button/LearnNewWords.png"
image_Know = "Button/Know.png"
image_StartTest = "Button/StartTest.png"
image_remind = "Button/remind.png"
image_translation = "Button/translation.png"


# 在模拟器中打开app
def open_app(image):
    s_time = time.time()  # 记录当前时间
    while pag.locateOnScreen(image, grayscale=True, confidence=0.9) is None:
        pag.PAUSE = 1
        e_time = time.time()  # 记录时间
        if e_time - s_time > 60:  # 查询时间过长，返回异常信息
            raise LoopException("未找到App")
    button = pag.locateOnScreen(image, grayscale=True, confidence=0.9)
    pag.click(button)
    if pag.locateOnScreen(image, grayscale=True, confidence=0.9) is not None:  # 点击之后发现按钮依然存在，再次点击，此种情况容易出现在有广告的时候
        open_app(image)
    else:
        print("App已经打开")
        pag.PAUSE = 3


# 点击开始学词
def start_learn(image):
    s_time = time.time()
    while pag.locateOnScreen(image, grayscale=True, confidence=0.8) is None:
        pag.PAUSE = 1
        e_time = time.time()
        if e_time - s_time > 60:
            raise LoopException("未找到Go去学词")
    button = pag.locateOnScreen(image, grayscale=True, confidence=0.8)
    pag.click(button)

    if pag.locateOnScreen(image, grayscale=True, confidence=0.8) is not None:
        start_learn(image)
    else:
        print("开始背词")


# 开始复习
def review(image, image_remind):
    s_time = time.time()
    while pag.locateOnScreen(image, grayscale=True, confidence=0.8) is None:
        pag.PAUSE = 1
        e_time = time.time()
        if e_time - s_time > 60:
            raise LoopException("未找到认识")
    button = pag.locateOnScreen(image, grayscale=True, confidence=0.9)
    button_remind = pag.locateOnScreen(image_remind, grayscale=True, confidence=0.8)
    j = 0
    while button is not None:
        button = pag.locateOnScreen(image, grayscale=True, confidence=0.9)
        print("”认识“按钮在", button)
        pag.click(button)
        button_remind = pag.locateOnScreen(image_remind, grayscale=True, confidence=0.8)
        print("”提示“按钮在", button_remind)
        pag.click(button_remind)
        pag.PAUSE = 5
        j = j + 1
        print("已经复习", j)
    print("全部复习完")


# 开始学习新词
def learn(image_know, image_test, num, image_translation):
    groupNum = 0  # 记录学习的轮数
    wordNum = 1  # 记录学习单词的个数
    while groupNum < num:
        # 判断按钮是否出现，因为软件可能有延迟
        while pag.locateOnScreen(image_know, confidence=0.8) is None:
            pag.PAUSE = 5
            print("未找到“认识”")
        # 出现之后，锁定这个按钮的位置
        button = pag.locateOnScreen(image_know, grayscale=True, confidence=0.8)
        while button is not None:
            button_translation = pag.locateOnScreen(image_translation, grayscale=True, confidence=0.9)
            pag.click(button_translation)
            print("”释义“按钮在", button_translation)
            pag.click(button_translation)

            button = pag.locateOnScreen(image_know, grayscale=True, confidence=0.8)
            pag.click(button)
            print("”认识“按钮在", button)

            print("已学习第", wordNum, "个词")
            wordNum = wordNum + 1
            pag.PAUSE = 3  # 防止图像还未完全显示出来就进行搜索的问题
        # 当这个按钮消失，进入到测试环节
        # 判断按钮是否出现
        while pag.locateOnScreen(image_test, grayscale=True, confidence=0.8) is None:
            pag.PAUSE = 1
            print("未找到“开始测试”")
        # 出现了之后点击开始测试
        button_test = pag.locateOnScreen(image_test, grayscale=True, confidence=0.8)
        pag.click(button_test)
        print("”测试按钮在“", button_test)
        groupNum += 1
        print("已经学完第", groupNum, "组")
    print("全部学完")


# review(image_Remember, image_remind)
# learn(image_Know, image_StartTest, 12, image_translation,)
