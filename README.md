README.md for Server Manager (backstage)
===
- Auto_pull.py  
Is for auto pull the repo on GitHub, and manage them easier.

- Server_Manage_System.py  
Is for auto record the status of the server. And analysis them.

## Todo list
- Symbol ignore.

# Based-on Discord Server Manager  (BDSM)

```
Bots -+
      |-- name -str
      |-- emotions -dict -+
      |                   |- happyness -float
      |                   |- boring -float
      |                   +- shame -float
      |-- tasks -list
      +-- behaviors -+
                     |- communicate _affected by emotions_ -+
                     |                                      |- say _str_way_  -+
                     |                                      |                  |- object -+
                     |                                      |                  |          |- everyone
                     |                                      |                  |          |- bot
                     |                                      |                  |          +- admin
                     |                                      |                  +- content -str ()
                     |                                      +- say _thought_  -+
                     |                                                         +- thought -> text
                     +- os_command
```

## construct
- Bots

## Bots

- Bots
    - name -str
    - emotions -dict
        - happyness -float
        - boring -float
        - shame -float
    - tasks -list
    - behaviors
        - communicate _affected by emotions_
            - say _str_way_
                - object
                    - everyone
                    - bot
                    - admin
                - content -str ()
            - say _thought_
                - thought -> text
        - os_command


## bot.say(gist):

types
- 表達 -表達意見
    - 贊成 
        - 好
        - 
    - 反對
- 事件 -某件事發生
    - 錯誤(程序)

## bot.run():

1. do task
    1. 如回覆訊息
2. runtime + 1

## bot.tasks:

tasks.task:
- priority
- execute time (estimated)

example_tasks: _task_
- communicate 
- watch
- execute


## First Bot

Riza_I

## Function

- 接收來自管理員的指令
- Watch autoPull


## Conversation protocol v0.3

對話由二至三部分組成，由全型逗號分開

第一部分，類別，如，`提問`、`表達`
```
type_list = ['提問', '表達']
```
第二部分，名詞，即是物件，如`伺服器`、`你`、`我`
```
object_list = ['autoPull', 'Riza']
obhect_refer_dict = {'自動更新程式': 'autoPull', '我': 'Riza', 'Riza_I': 'Riza'}
```
第三部分，狀態，如`運作良好`
```
status_list = ['提問', '表達']
status_refer_dict = {}
```

### 第二類別

類型，指令

格式
```
指令，[物件]，[動作]
```

## bot.recv_convers():  # v0.1

1. 解析訊息
    1. 轉換字詞至關鍵字
    2. 去除虛字及符號
2. 反應
    1. 如更新記憶、增加任務等

## task

type:
- 表達
- 檢查 arg4 ('檢查', msg_object, msg_status, reply=channel_id)