import discord
from discord.ext import commands

# 봇 설정
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 봇이 준비되었을 때 실행
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 간단한 명령어 예제
@bot.command()
async def hello(ctx):
    await ctx.send("안녕하세요!")
    
access_token = os.environ["BOT_TOKEN"]    
    
bot.run(access_token)