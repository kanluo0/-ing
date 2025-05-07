# pyautogui库用于自动化鼠标键盘事件
import pyautogui
# 用于控制滚轮事件频率，使其更加自然
import time

# 该方法用于获取目标图像所在位置，只要没找到图像就一直找
def get_position(word):
    up_left = None
    while up_left == None:
        up_left = pyautogui.locateCenterOnScreen('../automation/template/{}.png'.format(word),confidence=0.95)
    return up_left

# 单击
def click(position):
    pyautogui.click(position[0],position[1],button='left')

#选择刷本的类型
input('1:基础材料 2:遗器本 3周本')
type = input('今天刷什么类型副本')
if type==1:
    input('1:角色经验 2:武器经验 3金钱')
elif type==2:
    input('1:大公套 2:猎人套 3:钟表套')
elif type==3:
    input('1:末日兽 2:可可利亚 3金钱')
material = input(f'今天想刷{type}中的哪个副本')
input('1:基础材料 2:遗器本 3周本')
frequency = int(input(f'今天想刷几次?'))

# 在开始菜单中选择星穹铁道
click(get_position('xing_tie'))
print('星铁已经就绪')

# 虽然UI已经出现，但是程序还未准备就绪，需要等待
time.sleep(1)
# 于启动器界面启动游戏
click(get_position('qi_dong'))
print('星穹铁道，启动！')

# 于游戏界面开始游戏
click(get_position('start'))
print('开始游戏！')

# 于游戏中点击esc键打开菜单
if get_position('main') != None:
    pyautogui.hotkey('esc')
print('打开菜单')

# 于菜单界面打开指南
click(get_position('guide'))
print('打开指南')

if pyautogui.locateCenterOnScreen('../automation/template/today_task.png', grayscale=True) != None:
    click(get_position('today_task'))

# 找到欲拖拽目标type
pyautogui.moveTo(get_position('gloden_flower'))
print('找到预定滚动目标')

# 金花
if type == 'gloden_flower':
    click(get_position('gloden_flower'))
    print('找到预定目标')
    # 金花_经验
    if material == '1':
        pyautogui.click(get_position('exp')[0] + 500, get_position('exp')[1] + 100)
    # 金花_光锥经验
    elif material == '2':
        pyautogui.click(get_position('weapon_exp')[0] + 500, get_position('exp')[1] + 100)
    # 金花_信用点
    elif material == '3':
        pyautogui.click(get_position('credit_point')[0] + 500, get_position('exp')[1] + 100)

# 遗器本
elif type == '2':
    click(get_position('yiqi'))
    print('找到预定目标')

    # 没找到预定目标material就往下滚动列表
    while pyautogui.locateCenterOnScreen('../automation/template/yiqi', confidence=0.99) == None:
        pyautogui.scroll(-50)
        time.sleep(0.5)
    
    # 大公套
    if material == '1':
        pyautogui.click(get_position('dagong')[0] + 500, get_position('dagong')[1])
    # 猎人套
    elif material == '2':
        #滚动找到要刷的遗器本
        while pyautogui.locateCenterOnScreen('../automation/template/guaidao', confidence=0.99) == None:
         pyautogui.scroll(-50)
        time.sleep(0.5)
        pyautogui.click(get_position('guaidao')[0] + 500, get_position('guaidao')[1])
    # 钟表套
    elif material == '3':
        while pyautogui.locateCenterOnScreen('../automation/template/shiren', confidence=0.99) == None:
         pyautogui.scroll(-50)
        time.sleep(0.5)
        pyautogui.click(get_position('shiren')[0] + 500, get_position('shiren')[1])
   
# 每周副本
elif type == '3':
    click(get_position('weekly_copy'))
    print('找到预定目标')
    # 找到欲拖拽目标material
    pyautogui.moveTo(get_position('doomsday_beast'))
    print('找到预定滚动目标')

    # 没找到预定目标material就往下滚动列表
    while pyautogui.locateCenterOnScreen('../automation/template/yiqi', confidence=0.99) == None:
        pyautogui.scroll(-50)
        time.sleep(0.5)
    
    # 末日兽
    if material == '1':
        pyautogui.click(get_position('nothingness')[0] + 500, get_position('nothingness')[1])

    #可可利亚
    if material == '2':
        while pyautogui.locateCenterOnScreen('../automation/template/cocolia', confidence=0.99) == None:
         pyautogui.scroll(-50)
        time.sleep(0.5)
        pyautogui.click(get_position('cocolia')[0] + 500, get_position('cocolia')[1])

    #幻胧
    if material == '3':
        while pyautogui.locateCenterOnScreen('../automation/template/hazy', confidence=0.99) == None:
         pyautogui.scroll(-50)
        time.sleep(0.5)
        pyautogui.click(get_position('hazy')[0] + 500, get_position('hazy')[1])

# 进入战斗
click(get_position('enter_fighting'))

# 开始战斗（编队页面）
click(get_position('start_fighting'))

# 根据战斗次数决定循环次数
for i in range(frequency-1):
    # 再打一次
    click(get_position('fight_again'))