import random
from discord.ext import commands
from discord.ext.commands import BucketType, CommandOnCooldown
from cogs.counter import get_count, update_count


class CommandCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # 處理 "?" 訊息與特定關鍵字
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content in ["?", "？"]:
            await message.channel.send(random.choice
            ([
                "?",
                "蛤",
                "三小"
            ]))

        if message.content in ["我想聽公告", "!公告"]:
            await message.channel.send(random.choice
            ([
                "5/16阿奈奈我ㄉ媽咪新衣裝公告!!要記得來看唷!!",
            ]))
          
        if message.content in ["早安", "早ㄤㄤ", "早", "炸"]:
            await message.channel.send(random.choice
            ([
                "早ㄤㄤ(σ′▽‵)′▽‵)σ",
                "早安壓",
                "炸",
                "都幾點了還睡!!",
                "早啊！"
            ]))

        if message.content in ["晚安", "晚ㄤㄤ", "888", "睡覺ㄌ"]:
            await message.channel.send(random.choice
            ([
                "睡啥起來嗨＼＼\\٩( 'ω' )و //／／",
                "晚安啦晚安",
                "好ㄝ睡覺888",
                "真ㄉ該睡ㄌ都幾點ㄌ",
                "晚安安安安安"
            ]))

        if "777" in message.content:
            await message.channel.send("7777777")

        if "666" in message.content:
            await message.channel.send("6666666")

        if "555" in message.content:
            await message.channel.send("5555555")

        if "想買" in message.content:
            await message.channel.send(f"{message.author.mention} 買買買一定要買ㄉㄅ")

        if "可愛" in message.content:
            await message.channel.send(random.choice
            ([
                "真ㄉ好可愛我哭ㄌ...",
                "怎麼會這麼可愛...",
                "救命我瘋掉...",
                "歐買尬超可愛...",
                "齁好可愛..."
            ]))
            
        if message.content in ["好好笑", "www", "笑死"]:
            await message.channel.send(random.choice
            ([
                "ㄏㄏ",
                "笑死",
                "哈哈哈哈哈",
                "www",
                "好荒謬"
            ]))

        if message.content in ["好耶", "好ㄝ"]:
            await message.channel.send(random.choice
            ([
                "好ㄝ",
                "好耶"
            ]))
        
        if message.content in ["87", "笨蛋", "傻b", "白癡", "笨"]:
            await message.channel.send(random.choice
            ([
                "大笨蛋",
                "好笨",
                "笨蛋",
                "笨死ㄌ"
            ]))

        if message.content == "ㄐㄐ":
            count = get_count("ㄐㄐ") + 1
            update_count("ㄐㄐ", count)
            await message.channel.send(f"你第{count}次說ㄐㄐ了！")

        if message.content == "🍪":
            count = get_count("🍪") + 1
            update_count("🍪", count)
            await message.channel.send(f"紗愛吃ㄌ第{count}片餅乾🍪")

    # 靜默處理冷卻錯誤
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            return  # 冷卻中就什麼都不做
        raise error  # 其他錯誤繼續丟出來

    @commands.command(name="開台")
    @commands.cooldown(1, 2.0, BucketType.default)
    async def probiotic(self, ctx):
        count = get_count("開台") + 1
        update_count("開台", count)
        await ctx.send(f"你已經第{count}次叫我開台ㄌ救命")

    @commands.command(name="男娘")
    @commands.cooldown(1, 2.0, BucketType.default)
    async def buy(self, ctx, *args):
        if len(args) != 1:
            await ctx.send("用法錯誤！正確格式：`!男娘 A`")
            return
        A = args[0]
        await ctx.send(f"我就知道{A}最喜歡男娘對吧!!又被抓包!!")

    @commands.command(name="骰子")
    @commands.cooldown(1, 2.0, BucketType.default)
    async def dice(self, ctx):
        result = random.choice(["該", "不該", "該", "不該", "該", "不該", "該", "不該", "該", "不該"])
        await ctx.send(f"{ctx.author.mention}我覺得你{result}")

    @commands.command(name="選")
    @commands.cooldown(1, 2.0, BucketType.default)
    async def choose(self, ctx, *options):
        if len(options) < 2:
            await ctx.send("請提供至少兩個選項，例如：`!選 A B 或是更多選項`")
            return
        choice = random.choice(options)
        await ctx.send(f"{ctx.author.mention} 我感覺{choice}最好!!")


    @commands.command(name="指令")
    @commands.cooldown(1, 2.0, BucketType.default)
    async def show_commands(self, ctx):
        commands_list = """```txt

目前可用指令：

1. ㄐㄐ : 一個ㄐㄐ計數器
2. !開台 : 催我開台 嗚嗚
3. 🍪 : 餵紗愛吃餅乾~
4. !男娘 (名稱) : 又誰喜歡男娘
5. !骰子 : 猶豫不決就來骰骰子!!
6. !選 : 輸入猶豫ㄉ選項!!像是決定午餐吃啥ㄅ!!
7. !公告 : or打我想聽公告
8. !指令 : 查看指令

```"""
        await ctx.send(commands_list)


async def setup(bot):
    await bot.add_cog(CommandCog(bot))
