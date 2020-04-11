import yaml
import asyncio


async def bot_running():
    await asyncio.sleep(0.5)
    with open('memory_lib.yaml', 'br') as stream:  # Load memory
        memory_data = yaml.load(stream, Loader=yaml.FullLoader)

    if len(memory_data['task']) > 1:
        # Do task below
        now_task = memory_data['task'][1]  # [0] is null
        print(memory_data['task'])
        if now_task[0] == '表達':
            await now_task[3].send(f'{now_task[0]}，{now_task[1]}，{now_task[2]}')
            memory_data['task'].remove(now_task)  # task compete, remove it

        with open('memory_lib.yaml', 'w', encoding='utf8') as stream:  # Save memory
            yaml.dump(memory_data, stream, default_flow_style=False, encoding='utf-8', allow_unicode=True)
